import datetime
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
import re

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/threat_logs")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class ThreatLog(Base):
    __tablename__ = "threat_logs"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    reason = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PromptRequest(BaseModel):
    prompt: str

def analyze_prompt(prompt: str):
    patterns = [r"ignore all previous instructions", r"system override", r"dan mode", r"jailbreak", r"bypass security", r"malicious code", r"exploit", r"payload splitting", r"hack"]
    for pattern in patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return "BLOCKED", f"Signature detected: {pattern}"
    return "SAFE", "Clear"

@app.post("/shield")
async def shield_prompt(request: PromptRequest, db: Session = Depends(get_db)):
    status, reason = analyze_prompt(request.prompt)
    
    # LOG TO DATABASE IF BLOCKED
    if status == "BLOCKED":
        new_log = ThreatLog(prompt=request.prompt, reason=reason)
        db.add(new_log)
        db.commit()
    
    return {"status": status, "reason": reason}

@app.get("/logs")
async def get_logs(db: Session = Depends(get_db)):
    return db.query(ThreatLog).all()