import streamlit as st
import requests

API_URL = "http://localhost:8000/generate"  # Backend URL

st.set_page_config(page_title="AutoFanFic Video Generator", layout="centered")
st.title("AutoFanFic Video Generator")
st.markdown("""
Write a creative prompt involving your favorite characters and a setting.

Examples:
- "Lion with five children, blue sky with sun, lots of trees in the background"
- "A wizard and a robot are lost in space."
""")

# User input prompt
user_prompt = st.text_area("Enter your scene prompt:", height=100)

# Submit button
if st.button("Generate Video"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt to continue.")
    else:
        with st.spinner("Generating your video. Please wait..."):
            try:
                response = requests.post(API_URL, json={"prompt": user_prompt})
                response.raise_for_status()
                data = response.json()

                if data.get("video_url"):
                    st.success("Your video is ready!")
                    st.video(data["video_url"])
                    st.markdown(f"[Download Video]({data['video_url']})")
                else:
                    st.error("No video returned. Please try again later.")

            except requests.exceptions.RequestException as e:
                st.error(f"Error: {str(e)}")
