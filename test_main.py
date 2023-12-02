"""
Test goes here

"""
import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.getenv("API_TOKEN")


def test_html_files(directory="templates/"):
    """checks html files exists"""
    html_files = [f for f in os.listdir(directory) if f.endswith(".html")]

    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        assert os.path.exists(file_path) and os.path.isfile(file_path)


def test_openai_api():
    """Checks OpenAI API with a prompt"""
    test_prompt = "The answer to the universe is?"
    messages = [{"role": "user", "content": test_prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the engine based on your requirements
        messages=messages,
        temperature=0,
    )
    assert response.choices[0].message["content"] is not None


if __name__ == "__main__":
    test_html_files()
    test_openai_api()
