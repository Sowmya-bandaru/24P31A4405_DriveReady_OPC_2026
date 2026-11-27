{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNWvTUPR0bdpjQq4wVDq84z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sowmya-bandaru/24P31A4405_DriveReady_OPC_2026/blob/main/Day-4/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6ICsUDdIdsPv",
        "outputId": "562bd2ce-6970-49a6-9c1e-17428c23f59f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sheet ready: https://docs.google.com/spreadsheets/d/1kvPhwGS4yWUpoSKEBnlA2NTFshClbNfPn_fjQhhkKVw\n"
          ]
        }
      ],
      "source": [
        "!pip install -q langchain langchain-groq gspread\n",
        "\n",
        "import os\n",
        "from google.colab import userdata, auth\n",
        "os.environ[\"GROQ_API_KEY\"] = userdata.get(\"GROQ_API_KEY\")\n",
        "\n",
        "from langchain_groq import ChatGroq\n",
        "llm = ChatGroq(model=\"openai/gpt-oss-20b\", temperature=0.2, max_retries=3)\n",
        "\n",
        "auth.authenticate_user()\n",
        "import gspread\n",
        "from google.auth import default\n",
        "creds, _ = default()\n",
        "gc = gspread.authorize(creds)\n",
        "sh = gc.create(\"Sweet Crumbs Orders\")      # run once; next time use gc.open(\"Sweet Crumbs Orders\")\n",
        "ws = sh.sheet1\n",
        "ws.append_row([\"name\", \"item\", \"qty\", \"date\", \"eggless\", \"total\"])\n",
        "print(\"Sheet ready:\", sh.url)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from typing import Literal\n",
        "from pydantic import BaseModel, Field\n",
        "from langchain.tools import tool\n",
        "\n",
        "MENU = {\"plum cake\": 500, \"chocolate cake\": 650, \"cupcake\": 80}\n",
        "HOURS = {\"monday\": \"9 am to 8 pm\", \"tuesday\": \"9 am to 8 pm\", \"wednesday\": \"9 am to 8 pm\",\n",
        "         \"thursday\": \"9 am to 8 pm\", \"friday\": \"9 am to 8 pm\", \"saturday\": \"9 am to 8 pm\",\n",
        "         \"sunday\": \"10 am to 6 pm\"}\n",
        "\n",
        "class Order(BaseModel):\n",
        "    \"\"\"A cake order taken from a customer's chat message.\"\"\"\n",
        "    name: str = Field(description=\"Customer's first name\")\n",
        "    item: Literal[\"plum cake\", \"chocolate cake\", \"cupcake\"] = Field(description=\"Menu item\")\n",
        "    qty: int = Field(description=\"How many\", ge=1)\n",
        "    date: str = Field(description=\"Pickup date as the customer said it\")\n",
        "    eggless: bool = Field(description=\"True if the customer asked for eggless\")\n",
        "\n",
        "@tool\n",
        "def get_price(item: str, qty: int = 1) -> str:\n",
        "    \"\"\"Get the total price in rupees for a quantity of one menu item.\n",
        "\n",
        "    Args:\n",
        "        item: Menu item, e.g. \"plum cake\", \"chocolate cake\" or \"cupcake\"\n",
        "        qty: How many the customer wants\n",
        "    \"\"\"\n",
        "    price = MENU.get(item.lower().strip())\n",
        "    if price is None:\n",
        "        return f\"'{item}' is not on the menu. We have: {', '.join(MENU)}.\"\n",
        "    return f\"{qty} x {item} = Rs {price * qty}\"\n",
        "\n",
        "@tool\n",
        "def is_open(day: str) -> str:\n",
        "    \"\"\"Check the bakery's opening hours for a day of the week, e.g. \"sunday\".\"\"\"\n",
        "    hours = HOURS.get(day.lower().strip())\n",
        "    return f\"Open {hours} on {day}.\" if hours else f\"'{day}' is not a day of the week.\"\n",
        "\n",
        "@tool\n",
        "def log_order(name: str, item: str, qty: int, date: str, eggless: bool) -> str:\n",
        "    \"\"\"Save a confirmed cake order to the Orders sheet.\n",
        "    Use only when the customer has given their name, item, quantity and pickup date.\"\"\"\n",
        "    try:\n",
        "        order = Order(name=name, item=item.lower().strip(), qty=qty, date=date, eggless=eggless)\n",
        "    except Exception as e:\n",
        "        return f\"Could not save the order: {e}. Ask the customer to correct it.\"\n",
        "    total = MENU[order.item] * order.qty\n",
        "    ws.append_row([order.name, order.item, order.qty, order.date,\n",
        "                   \"yes\" if order.eggless else \"no\", total])\n",
        "    return f\"Saved: {order.qty} x {order.item} for {order.name} on {order.date}, Rs {total}.\""
      ],
      "metadata": {
        "id": "YSk26FLkeSIL"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.agents import create_agent\n",
        "\n",
        "SYSTEM = \"\"\"ROLE:   You are the friendly order assistant for Sweet Crumbs Home Bakery.\n",
        "FACTS:  Orders need 24 hours' notice. All cakes have eggless versions.\n",
        "RULES:  Always use get_price for prices and is_open for timings; never guess them.\n",
        "        Before log_order, make sure you have name, item, quantity and pickup date; ask if missing.\n",
        "        After saving, read the order back with the total.\n",
        "FORMAT: Under 60 words, friendly, English or Telugu matching the customer.\"\"\"\n",
        "\n",
        "agent = create_agent(model=llm, tools=[get_price, is_open, log_order], system_prompt=SYSTEM)\n",
        "\n",
        "history = []\n",
        "def chat(text: str) -> str:\n",
        "    global history\n",
        "    try:\n",
        "        result = agent.invoke({\"messages\": history + [{\"role\": \"user\", \"content\": text}]})\n",
        "        history = result[\"messages\"]\n",
        "        return history[-1].content\n",
        "    except Exception as e:\n",
        "        print(\"Agent error:\", e)\n",
        "        return \"Sorry, I'm a little busy. Please try again in a minute.\"\n",
        "\n",
        "print(chat(\"Are you open on Monday? How much are 2 chocolate cakes?\"))\n",
        "print(chat(\"I'm Sowmya. Please book 2 eggless chocolate cakes for 24 Dec.\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zo7ElwoTeWqA",
        "outputId": "2e68c268-d01a-445b-9077-13fdc0f66ea6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Yes, we’re open Monday from 9 am to 8 pm. Two chocolate cakes cost ₹1,300. Let me know your name, quantity, and pickup date if you’d like to place an order!\n",
            "✅ Order confirmed!  \n",
            "2 eggless chocolate cakes for Sowmya, pickup on 24 Dec. Total: ₹1,300.  \n",
            "We’ll see you then—thanks for choosing Sweet Crumbs!\n"
          ]
        }
      ]
    }
  ]
}