import streamlit as st
import requests

st.title("📝 Text Summarizer (with FastAPI backend)")
st.write("Enter your text below and get an AI-generated summary.")

text_input = st.text_area("Your Text:", height=200, placeholder="Paste your text here...")

if st.button("Generate Summary"):
    if text_input.strip():
        with st.spinner("Contacting FastAPI backend..."):
            try:
                response = requests.get(
                    "http://localhost:8080/predict",
                    params={"text": text_input},
                    timeout=60
                )
                if response.status_code == 200:
                    summary = response.text
                    st.markdown("### Summary:")
                    st.success(summary)
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter some text to summarize.")

st.markdown("---")
st.caption("Frontend: Streamlit | Backend: FastAPI")