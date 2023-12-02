from dotenv import load_dotenv
import os
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
)
import openai

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("API_TOKEN")


@app.route("/")
def index():
    """retruns index page"""
    return render_template("index.html")


def get_completion(prompt, model="gpt-3.5-turbo"):
    print(prompt)
    prompt_answer = f"""
        Perform the following actions:
        1 - I will give you the symptoms I have.
        2 - Specify one professional medical disease based on my symptoms. 
        3 - Provide a paragraph of information about the disease.
        4 - Answer in the formation part.

        Using the following format:
        Symptoms: <symptom name>
        Illness: <illness name> , <illness description>

        ```{prompt}```
    """
    messages = [{"role": "user", "content": prompt_answer}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


@app.route("/result")
def result():
    # Get the result from the URL parameter
    result = request.args.get("result", "")
    print(result)
    return render_template("result.html", result=result)


@app.route("/predict", methods=["POST"])
def predict():
    """test predict"""
    print(request.form)
    prompt = request.form.get("prompt")
    result = get_completion(prompt)

    # Redirect to the result page with the result as a parameter
    return redirect(url_for("result", result=result))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
