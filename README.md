[![CI](https://github.com/nogibjj/tinayiluo_individual4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_individual4/actions/workflows/cicd.yml)
## Auto Scaling Flask App Using Azure Container Platform

[Hello Doctor Web Application](https://week13.calmisland-989659dc.westus2.azurecontainerapps.io)

### Goal
Construct an auto-scaling, publicly accessible container that incorporates a fully functional Large Language Model (LLM), utilizing Azure App Services and Flask for deployment and management. 

### Overview 
The project, "Hello Doctor," is a Flask web application integrated with OpenAI's LLM model, utilizing Docker for effective containerization. Here is a brief workflow overview of the Flask web application:

- User Input: Individuals input their symptoms into the application.

- Illness Search: The application processes these symptoms and searches for a corresponding illness using the AI model.

- Diagnostic Output: The web application then presents a detailed diagnostic of the identified illness to the user.

<img width="727" alt="Screen Shot 2023-12-06 at 12 35 54 PM" src="https://github.com/nogibjj/tinayiluo_individual4/assets/143360909/d79e6e93-f9ae-41f5-b73a-2a58115d2a26">

### Preparation: 

    - Use https://github.com/nogibjj/python-ruff-template
    
    - Gain access to user token via Open AI GPT-3.5 model

    - Input API_TOKEN into the `.env` file 

    - Specify installation requirements `requirements.txt`

    ```
    #devops
    black==22.3.0
    click==8.1.3 
    pytest==7.1.3
    pytest-cov==4.0.0
    #pylint==2.15.3
    #rust based linter
    ruff==0.0.284
    boto3==1.24.87
    #web
    fastapi==0.85.0
    uvicorn==0.18.3
    #others
    Flask==2.0.2
    gunicorn
    Werkzeug==2.2.2
    python-dotenv
    requests
    openai==0.28.1
    ```

    - install: `make install`

    - run: `python main.py` and navigate to the locally hosted website

    - Input API_TOKEN into Github to generate Secret

    - Build docker image: docker build --tag <insert image name> .

    - Login to azure cli: `az login`

    - Deploy Azuer web app: `az containerapp up --resource-group <insert resource group> --name <insert app name> --ingress external --target-port 50505 --source .`

    - Input API_TOKEN on Azure for Azure Configuration

    - View app via `container apps` and docker image via `container registry` in azure web portal 

### Key Components 

#### Flask Web Application:
- **Functionality:** The web app allows users to input prompts, which are then processed by the GPT-3.5 model to generate responses. The responses are displayed on a results page.

    - `main.py`:

        - Import Statements: The script imports necessary modules and functions. It uses dotenv to load environment variables, os for operating system interactions, and various components from Flask to handle web requests and responses. It also imports the openai module to interact with OpenAI's API.
        
        - Environment Variables: load_dotenv() loads environment variables from a .env file. This typically includes sensitive data like API keys.
        
        - Flask App Initialization: app = Flask(__name__) initializes a new Flask application. 
        
        - OpenAI API Key: Sets the OpenAI API key by fetching it from environment variables. This key is necessary for authenticating requests to OpenAI's services.
        
        - Index Route: The @app.route("/") decorator defines the root endpoint of the web application. When a user visits the root URL, the index() function renders and returns the index.html template.
        
        - get_completion Function: This function takes a user prompt and sends it to OpenAI's GPT-3.5 model. It formats the prompt, sends it to the model, and returns the generated response. The temperature parameter is set to 0, indicating no randomness in response generation.
        
        - Result Route: The @app.route("/result") endpoint is used to display results. It fetches results from URL parameters and renders them using the result.html template.
        
        - Predict Route: The @app.route("/predict", methods=["POST"]) endpoint handles prediction requests. It retrieves user input from a form, processes it through the get_completion function, and redirects to the result page with the generated output.

        - Main Block: The if __name__ == "__main__" block checks if the script is executed directly (not imported). If so, it runs the Flask app with debugging enabled on port 8000.

    - `test_main.py`: ensures the availability of HTML files needed for the web application and verifies that the OpenAI API integration is functioning correctly. 

- **HTML Templates:** The project contains HTML templates (`index.html`, `result.html`) providing a user-friendly interface.

    - `index.html`: this HTML page serves as a user interface for submitting symptoms to a Flask-based web application, which then uses an AI model for generating a diagnosis. The page is designed to be user-friendly and responsive, leveraging Bootstrap for styling and JavaScript for form handling and asynchronous server communication.

    - `result.html`: this HTML page serves as a simple, user-friendly interface for displaying the diagnostic results from the AI model. The use of Bootstrap ensures a clean layout, and the dynamic rendering of the result allows for a flexible display of information based on the AI model's output.

- **Static Image:** The project contains a `happy_doctor.ipg` image in the `static` folder providing a user-friendly website design. 

#### Open AI LLM Model Integration:
- **API Interaction:** The application interfaces with the Open AI LLM Model via API calls. It sends a the user input of illness symptons to get predictions.

- **Prediction Logic:** Based on model predictions, the app produces illness diagnostic to the user.

<img width="1440" alt="Screen Shot 2023-12-05 at 4 32 31 PM" src="https://github.com/nogibjj/tinayiluo_individual4/assets/143360909/43afd84d-de0e-490a-bd64-276dbd37e321">

#### Github Actions:
- **Makefile & CICD:** The workflow includes running a `Makefile` to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

#### Web App Optimization:
- **Gunicorn configuration file:** The `gunicorn.conf.py` optimize the performance and reliability of a Python web application in a production environment. It balances resource use with the ability to handle a significant number of concurrent requests.

#### Docker Containerization:
- **Dockerfile:** This Dockerfile containerizes a Flask app, setting up a Docker container with Python and Gunicorn to run the web application. It encapsulates the app's code and dependencies, simplifying deployment across different environments.

### DockerHub and Azure Container Apps Deployment:

- **Azure Container Registry :** The Docker image is hosted on Azure Container Registry

<img width="1440" alt="Screen Shot 2023-12-05 at 4 43 29 PM" src="https://github.com/nogibjj/tinayiluo_individual4/assets/143360909/30cec7c8-934a-4791-baad-c577ca5a7534">

<img width="1440" alt="Screen Shot 2023-12-06 at 4 05 29 PM" src="https://github.com/nogibjj/tinayiluo_individual4/assets/143360909/9261c0a9-3ded-4a56-aca1-d9c7551b7633">

- **Azure Container Apps Deployment:** The Flask app is successfully deployed on Azure Container Apps, providing a public endpoint for users to interact with the application.

<img width="1440" alt="Screen Shot 2023-12-06 at 4 14 36 PM" src="https://github.com/nogibjj/tinayiluo_individual4/assets/143360909/179ecf8e-18ff-4efd-b21b-67798835f038">

### Check Format and Test Errors: 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`


