Day 4 – Tools, Structured Output and Google Sheets 

Project Overview

This project demonstrates how to build a tool-enabled AI agent for Sweet Crumbs Home Bakery using LangChain and Groq.

Unlike a basic chatbot, this AI agent can use Python functions (tools) to check product prices, verify bakery opening hours, validate customer orders, and save confirmed orders to Google Sheets.

Technologies Used

Python

Google Colab

LangChain

LangChain Groq

Groq API

GPT-OSS

Pydantic

Google Sheets

gspread

Features

AI agent with multiple tools

Automatic product price calculation

Bakery opening-hours checking

Customer order handling

Pydantic-based data validation

Saving confirmed orders to Google Sheets

Conversation history and memory

Tool execution and error handling

Bakery Menu

Product

Price

Plum Cake

Rs 500

Chocolate Cake

Rs 650

Cupcake

Rs 80

Tools Created

get_price() – Calculates the total price of bakery products.

is_open() – Checks the bakery's opening hours.

log_order() – Validates and saves customer orders to Google Sheets.

Concepts Learned

Why AI agents need tools

Function calling

Creating tools using the @tool decorator

Writing meaningful tool names and docstrings

Creating agents using create_agent()

Handling rate limits and tool errors

Structured output using Pydantic

Data validation using BaseModel and Field

Google Sheets integration using gspread

Saving customer orders automatically

Google Sheets Integration

The project connects to Google Sheets and creates an order record containing:

Customer name

Product name

Quantity

Pickup date

Eggless preference

Total price

Project Structure

Day-4/
│
├── task.py
└── README.md

How to Run

Open the notebook in Google Colab.

Install the required Python packages.

Add your GROQ_API_KEY to Colab Secrets.

Authenticate your Google account.

Run the tool and agent creation cells.

Test customer questions and order handling.

Check Google Sheets to verify saved orders.

Learning Outcome

Through this project, I learned how to extend a basic chatbot into a tool-enabled AI agent, create Python tools, validate structured data using Pydantic, and integrate Google Sheets to store customer orders automatically.

Author

B.Tech Data Science Student
