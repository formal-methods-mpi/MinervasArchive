# Minerva's Archive

## Introduction

Minerva's Archive is a Python-based application that facilitates discussions about research reports from the Max Planck Institute for Human Development and the staff associated with them. This application interprets questions posed in natural language and offers relevant responses, backed by the content of specified documents. It leverages language model-based agents to generate accurate responses to user queries. Please be aware that the application is designed to respond only to questions concerning the Max Planck Institute for Human Development.

## Getting Started

Get the `.env` file set up:

```
git clone --depth 1 https://github.com/formal-methods-mpi/MinervasArchive
cd MinervasArchive
cp .env.example .env
```

Add an Open AI API key from https://portal.azure.com/ (click on the deployment, then under Keys and Endpoints)

```
nano .env
```

Start the container:

```
docker compose up
```

## How It Works

The agent within this application follows a structured process to generate responses to your inquiries:

1. Question: The application identifies the user's question.
2. Thought: The agent contemplates the necessary steps to answer the question. If an answer isn't readily available, it will promptly communicate this to the user.
2. Action: The agent selects an appropriate tool from a predefined set to formulate the answer.
2. Observation: The result of the action is analyzed by the agent, which assesses whether additional information is required to answer the question.
2. Repeat: This process is repeated up to three times if the agent deems the observation unsatisfactory.
2. Final Answer: The agent provides the answer (if feasible) and references the consulted documents.

## Local Development

Follow these steps to install the Minerva's Archive application:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Obtain an API key from OpenAI and incorporate it into the `.env` file in the project directory.

### Usage

Follow these steps to use the Minerva's Archive application:

1. Verify that you have installed the required dependencies and added the OpenAI API key to the `.env` file.
2. Build the vectordatabase: `python scrapingXMLfaiss.py`
2. Run the `main.py` file using the Streamlit CLI with the following command: `streamlit run app.py`
2. The application will launch in your default web browser, presenting the user interface.
2. Use the chat interface to ask questions in natural language pertaining to the Max Planck Institute for Human Development.

## Updating GHCR Image

1. Bump the version number in `docker-compose.yml` under `image:` and note the new IMAGENAME
2. Build the image locally: `docker compose build --no-cache`
3. Get a GitHub token with permision `packages:write`
4. Upload:
   ```
   export CR_PAT=YOUR_TOKEN
   echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
   docker push ghcr.io/formal-methods-mpi/minervasarchive:latest
   ```

## License

Minerva's Archive is licensed under the [MIT License](https://opensource.org/licenses/MIT) and incorporates code fragments from the original GitHub repository [ask-multiple-pdfs](https://github.com/alejandro-ao/ask-multiple-pdfs) licensed under the MIT License.
