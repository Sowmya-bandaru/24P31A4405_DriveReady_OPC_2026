# Day 1 – Introduction to LLMs and First API Call 🤖

## Project Overview

This project is part of the **Drive Ready – AI Agents | One Person Company (OPC) Initiative**.

In this task, I learned the basics of Large Language Models (LLMs) and how to connect an AI model using an API.

I created a simple AI-powered assistant for **Sweet Crumbs Home Bakery** using LangChain and Groq. The assistant answers customer questions based on the information and instructions provided in its system prompt.

## Technologies Used

- Python
- Google Colab
- LangChain
- LangChain Groq
- Groq API
- GPT-OSS 120B
- Prompt Guard

## Concepts Learned

During Day 1, I learned about:

1. **Large Language Models (LLMs):** AI models that understand and generate human-like text.
2. **Tokens:** Small pieces of text processed by an LLM.
3. **Temperature:** Controls how predictable or creative the model's responses are.
4. **Context Window:** The amount of information a model can process in one request.
5. **AI Hallucination:** When an AI model generates incorrect or made-up information.
6. **Memory in LLMs:** How conversation history can be provided to help a model remember earlier messages.
7. **AI Engineering:** Building applications using existing AI models and APIs.

## Project Features

- Answers customer questions about bakery orders.
- Explains the bakery's ordering policies.
- Informs customers that orders require 24 hours' advance notice.
- Provides information about eggless cake options.
- Avoids making promises about delivery times.
- Uses a system prompt to guide the assistant's responses.
- Includes a separate experiment using the Prompt Guard model.

## How It Works

1. Connects to the Groq API using an API key stored in Google Colab Secrets.
2. Initializes the GPT-OSS 120B model using LangChain's `ChatGroq`.
3. Creates a system prompt with the bakery's information and rules.
4. Uses an `ask()` function to send customer questions to the AI model.
5. Receives and displays the generated response.

## Installation

Install the required Python packages in Google Colab:

```python
!pip install -q langchain-groq groq
```

## API Key Configuration

The Groq API key is stored securely in Google Colab Secrets with the name `GROQ_API_KEY`.

It is accessed using:

```python
from google.colab import userdata

api_key = userdata.get("GROQ_API_KEY")
```

The API key is not directly written in the source code or uploaded to GitHub.

## Example

**Customer Question:**

Can I get an eggless cake?

**Assistant Response:**

Yes, we offer eggless versions of all our cakes. Please place your order at least 24 hours in advance.

*The response is based on the bakery information provided in the system prompt.*

## Experiments Performed

As part of this task, I also explored the following:

- **Temperature Experiment:** Compared responses using different temperature values.
- **Hallucination Experiment:** Observed how an AI model can generate unsupported information when facts are not provided.
- **Memory Experiment:** Compared separate API calls with calls that include previous conversation history.
- **Token Experiment:** Compared token usage for questions in English and Telugu.
- **Custom Business Assistant:** Created another simple assistant using information about a stationery store.
- **Prompt Guard Experiment:** Tested a separate Prompt Guard model with normal and potentially harmful or instruction-manipulating prompts.

## Project Structure

```text
Day-1/
│
├── task.py
└── README.md
```

## What I Learned

By completing this task, I understood how LLMs work at a basic level, how to connect an AI model using an API, and how system prompts help control the responses of an AI assistant.

I also learned about hallucinations, tokens, temperature, conversation history, and basic prompt safety testing.

## Future Improvements

- Add conversation memory to the bakery assistant.
- Integrate prompt safety checks into the assistant workflow.
- Add customer order management.
- Improve the assistant with more bakery-related information.

## Author

**Sowmya Bandaru**

**Project:** Day 1 – Introduction to LLMs and First API Call

**Program:** Drive Ready – AI Agents | OPC Initiative
