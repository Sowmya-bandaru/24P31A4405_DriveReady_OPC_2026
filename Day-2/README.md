# Day 2 – Prompts, Memory and Python for AI Agents 🤖

## Project Overview

This project is part of the **Drive Ready – AI Agents | One Person Company (OPC) Initiative**.

In Day 2, I learned how to improve an AI chatbot using better prompts, conversation history, and Python concepts.

I worked on the **Sweet Crumbs Home Bakery Assistant**, an AI-powered chatbot that answers customer questions, remembers previous conversations, and provides information about bakery orders and prices.

## Technologies Used

- Python
- Google Colab
- LangChain
- LangChain Groq
- Groq API
- GPT-OSS 120B
- JSON

## Concepts Learned

During Day 2, I learned about the following concepts:

1. **Messages and Roles:** Understanding system, user, and assistant messages in an AI conversation.
2. **System Prompt:** Giving the AI clear instructions using Role, Facts, Rules, and Format.
3. **Few-Shot Prompting:** Providing example questions and answers to guide the model's responses.
4. **JSON:** Converting customer messages into structured data that Python can process.
5. **Conversation Memory:** Maintaining chat history so the chatbot can remember previous messages.
6. **Python Dictionaries:** Storing information using key-value pairs.
7. **Functions and Type Hints:** Creating reusable functions with input and output types.
8. **Decorators:** Adding extra functionality to an existing function.
9. **Exception Handling:** Using `try` and `except` to handle errors without stopping the program unexpectedly.

## Project Features

- Answers customer questions about bakery products.
- Provides cake prices from a predefined menu.
- Explains the 24-hour advance ordering requirement.
- Provides information about eggless cake options.
- Remembers customer names and previous orders during a conversation.
- Maintains recent conversation history.
- Calculates the total price based on the selected item and quantity.
- Handles API errors with friendly messages.
- Uses structured data to manage customer orders.

## Bakery Menu

The chatbot uses the following predefined menu:

| Item           | Price |
| -------------- | ----: |
| Plum Cake      |  ₹500 |
| Chocolate Cake |  ₹650 |
| Cupcake        |   ₹80 |

## How It Works

1. Connects to the Groq API using an API key stored in Google Colab Secrets.
2. Initializes the GPT-OSS 120B model.
3. Creates a system prompt containing bakery details, prices, and rules.
4. Stores bakery products and prices in a Python dictionary.
5. Uses functions to calculate order prices.
6. Maintains conversation history by sending previous messages to the model.
7. Uses JSON to represent customer order details in a structured format.
8. Handles errors using `try` and `except` blocks.

## Installation

Install the required packages in Google Colab:

```python
!pip install -q langchain-groq groq
```

## API Key Configuration

The Groq API key is stored securely in Google Colab Secrets with the name `GROQ_API_KEY`.

Retrieve it using:

```python
from google.colab import userdata

api_key = userdata.get("GROQ_API_KEY")
```

Never share or upload your actual API key to GitHub.

## Example

**Customer Conversation:**

Customer: Hi, my name is Ravi.

Assistant: Nice to meet you, Ravi! What would you like to order?

Customer: I need 2 chocolate cakes.

Assistant: Noted! Orders need 24 hours' notice. Anything else?

Customer: What did I order?

**Assistant Response:**

You asked for 2 chocolate cakes.

**Total Price:**

2 × ₹650 = ₹1,300

*The chatbot uses conversation history to identify the customer's previous order.*

## Experiments Performed

As part of this task, I explored the following experiments:

- **System Prompt Experiment:** Observed how changing or removing prompt instructions affects chatbot responses.
- **Few-Shot Prompting:** Used example customer messages to classify new messages as orders, questions, or complaints.
- **JSON Experiment:** Converted customer order details into structured JSON data.
- **Memory Experiment:** Tested how conversation history helps the chatbot remember customer information.
- **Dictionary Experiment:** Stored bakery menu items and prices using Python dictionaries.
- **Function Experiment:** Created a function to calculate the total price of bakery items.
- **Decorator Experiment:** Used a decorator to display function execution details.
- **Exception Handling Experiment:** Tested how `try` and `except` handle errors.

## Project Structure

```text
24P31A4405_DriveReady_OPC_2026/
│
├── Day-1/
│   ├── task.py
│   └── README.md
│
└── Day-2/
    ├── task.py
    └── README.md
```

## What I Learned

By completing Day 2, I understood how to make an AI chatbot more useful by providing clear instructions and maintaining conversation history.

I also learned how Python dictionaries, functions, decorators, JSON, and exception handling can be used while developing AI applications.

## Author

**Sowmya Bandaru**

**Project:** Day 2 – Prompts, Memory and Python for AI Agents

**Program:** Drive Ready – AI Agents | OPC Initiative
