import openai
import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    posts = []
    for _ in range(number_of_posts):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate a {tone_of_voice.lower()} LinkedIn post for {company_name} about {product_service} targeting {target_audience}."}
            ]
        )
        post = response.choices[0].message.content
        posts.append(post)

    # Display generated posts
    for i, post in enumerate(posts, start=1):
        st.subheader(f"Post {i}")
        st.write(post)
        st.write("### Relevant Hashtags and Emojis")
        st.write("#LinkedIn #OpenAI 😊")