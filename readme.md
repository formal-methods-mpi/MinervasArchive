# Minerva's Archive

## Introduction

Minerva's Archive is a Python-based application that facilitates discussions about research reports from the Max Planck Institute for Human Development and the staff associated with them. This application interprets questions posed in natural language and offers relevant responses, backed by the content of specified documents. It leverages language model-based agents to generate accurate responses to user queries. Please be aware that the application is designed to respond only to questions concerning the Max Planck Institute for Human Development.

## How It Works

The agent within this application follows a structured process to generate responses to your inquiries:

1. Question: The application identifies the user's question.

2. Thought: The agent contemplates the necessary steps to answer the question. If an answer isn't readily available, it will promptly communicate this to the user.

3. Action: The agent selects an appropriate tool from a predefined set to formulate the answer.

4. Observation: The result of the action is analyzed by the agent, which assesses whether additional information is required to answer the question.

5. Repeat: This process is repeated up to three times if the agent deems the observation unsatisfactory.

6. Final Answer: The agent provides the answer (if feasible) and references the consulted documents.

## Dependencies and Installation

Follow these steps to install the Minerva's Archive application:

1. Clone the repository to your local machine.

2. Install the necessary dependencies by running the following command:
   
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and incorporate it into the `.env` file in the project directory.

## Usage

Follow these steps to use the Minerva's Archive application:

1. Verify that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI with the following command:

   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, presenting the user interface.

4. Use the chat interface to ask questions in natural language pertaining to the Max Planck Institute for Human Development.

## License

Minerva's Archive is licensed under the [MIT License](https://opensource.org/licenses/MIT) and incorporates code fragments from the original GitHub repository [ask-multiple-pdfs](https://github.com/alejandro-ao/ask-multiple-pdfs) licensed under the MIT License.
