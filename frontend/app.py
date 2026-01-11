import streamlit as st
import requests
import pandas as pd

st.sidebar.title("Threat Intelligence")
if st.sidebar.button("Refresh Logs"):
    # In a full app, this would fetch from the Database
    # For now, we show you've designed the UI for it
    mock_data = {
        "Timestamp": ["2026-01-10 14:20", "2026-01-10 15:45"],
        "Attack Type": ["Jailbreak", "Payload Splitting"],
        "Severity": ["High", "Medium"]
    }
    st.sidebar.table(pd.DataFrame(mock_data))
st.set_page_config(page_title="AI-Shield Gateway", page_icon="🛡️")
st.title("🛡️ AI-Shield: Secure Prompt Gateway")

prompt = st.text_area("Enter your AI Prompt:", placeholder="Ask me anything...")

if st.button("Submit Securely"):
    if prompt:
        # Send to our Dockerized Backend
        with st.spinner("Analyzing for threats..."):
            try:
                response = requests.post("http://backend:8000/shield", json={"prompt": prompt})
                data = response.json()
                
                if data["status"] == "SAFE":
                    st.success("✅ Prompt Cleared! Sending to LLM...")
                    st.info(f"Analysis: {data['reason']}")
                else:
                    st.error(f"🚨 Security Alert: {data['reason']}")
            except Exception as e:
                st.error("Could not connect to the Security Backend.")