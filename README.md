# README.md

# LinkedIn Post Generator

This project is a simple Streamlit application that generates LinkedIn posts based on user inputs. It utilizes the OpenAI GPT model to create engaging content tailored to the specified tone of voice.

## Features

- User inputs for:
  - Company name
  - Product/service
  - Target audience
  - Tone of voice (Professional, Casual, Humorous)
  - Number of posts (1 to 10)
- Generates LinkedIn posts with relevant hashtags and emojis.
- Clean and simple interface.

## Requirements

- Python 3.x
- Streamlit
- OpenAI

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd linkedin-post-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `src` directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```
   streamlit run src/app.py
   ```

5. Open your browser and go to `http://localhost:8501` to view the app.

## Usage

- Enter the required information in the input fields.
- Click the button to generate LinkedIn posts.
- The generated posts will be displayed on the page.

## License

This project is licensed under the MIT License.