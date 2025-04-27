import streamlit as st
from openai import OpenAI
import os

# Set page config
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📱")

# Get API key
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found. Please set it in Streamlit secrets or environment variables.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit interface
st.title("LinkedIn Post Generator")

# User inputs
company_name = st.text_input("Company Name")
product_service = st.text_input("Product/Service")
target_audience = st.text_input("Target Audience")
tone_of_voice = st.selectbox("Tone of Voice", ["Professional", "Casual", "Humorous"])
number_of_posts = st.slider("Number of Posts", 1, 10)

# Button to generate posts
if st.button("Generate Posts"):
    if not all([company_name, product_service, target_audience]):
        st.warning("Please fill in all required fields.")
        st.stop()
        
    try:
        with st.spinner("Generating posts..."):
            posts = []
            for _ in range(number_of_posts):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"Generate a {tone_of_voice.lower()} LinkedIn post for {company_name} about {product_service} targeting {target_audience}. Include relevant hashtags and emojis."}
                    ]
                )
                post = response.choices[0].message.content
                posts.append(post)

        # Display generated posts
        for i, post in enumerate(posts, start=1):
            st.subheader(f"Post {i}")
            st.write(post)
            st.divider()
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")