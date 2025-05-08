# Bank Sales Assistant - Generative AI

A virtual banking assistant based on Amazon Bedrock and Claude 3 Sonnet, implemented with Streamlit.

## 📋 Overview

This project implements a virtual assistant for the banking sector using Amazon Bedrock and Anthropic's Claude 3 Sonnet model. The application provides a conversational interface that can assist customers with information about banking products, financial services, and sales support.

## 🏗️ Architecture

```
iagenerativa/
├── app.py                # Main Streamlit application
├── agent.py              # Bedrock agent implementation
├── .env.dev              # Environment variables configuration file
└── README.md             # Project documentation
```

## 🚀 Features

- **Conversational interface**: Interactive chat with the banking assistant
- **Amazon Bedrock integration**: Uses advanced generative AI models
- **Intuitive user experience**: Easy-to-use Streamlit interface
- **Contextual responses**: The assistant can maintain conversation context

## 🔧 Requirements

- Python 3.8+
- AWS CLI configured with appropriate credentials
- Access to Amazon Bedrock with Claude 3 Sonnet model enabled
- Streamlit
- Boto3 (AWS SDK for Python)
- AutoGen

## ⚙️ Setup

1. Clone the repository:

```bash
git clone https://github.com/training-acn/iagenerativa.git
cd iagenerativa
```

2. Install dependencies:

```bash
pip install streamlit boto3 autogen
```

3. Configure AWS credentials:

Create an `.env` file in the project's root directory with the following variables:

```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
```

Make sure the AWS user has the necessary permissions to access Amazon Bedrock.

## 🏃‍♂️ Running the application

To start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`.

## 💻 Usage

1. Open the application in your browser
2. Type your question or request in the sidebar
3. Click "Send" to submit your message to the assistant
4. View the assistant's response in the main window

## 🧩 Main Components

### BedrockAgent (agent.py)

The `BedrockAgent` class manages the interaction with Amazon Bedrock:

- Initializes a connection to the Bedrock Runtime service
- Sends prompts to the Claude 3 Sonnet model
- Handles responses and errors

### Streamlit Application (app.py)

The user interface of the application:

- Configures the Streamlit page
- Initializes the Bedrock agent
- Manages session state and conversation history
- Displays the chat interface

## 🔒 Security

- AWS credentials are managed through environment variables
- Never store credentials directly in the code
- Make sure to properly configure IAM policies to limit access to AWS services

## 🛠️ Customization

### Changing the model

To use a different model, modify the `model_id` parameter when initializing the agent in `app.py`:

```python
agent = BedrockAgent(
    name='SalesAssistantAgent',
    model_id='anthropic.claude-3-sonnet-20240229-v1:0',  # Change to desired model ID
    region_name='us-east-1'
)
```

### Customizing the interface

You can modify the appearance of the Streamlit interface in `app.py` using Streamlit's styling features.

## 📈 Future Development

- Integration with knowledge base for specific banking product information
- Implementation of RAG (Retrieval-Augmented Generation) capabilities
- Addition of user authentication
- Multilingual support
- Integration with existing banking systems

## 📝 Notes

- This is a demonstration project and may require further development for production use
- Using Amazon Bedrock incurs usage-based costs
- Make sure to test the application in a secure environment before using it with sensitive data

## 📄 License

[Insert license information]

## 👥 Contributions

Contributions are welcome! Please open an issue or pull request for suggestions or improvements.

---

Developed for Generative AI training.
