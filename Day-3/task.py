{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4mRL1J0a7QX5KZxJ8EkQB",
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
        "<a href=\"https://colab.research.google.com/github/Sowmya-bandaru/24P31A4405_DriveReady_OPC_2026/blob/main/Day-3/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "UiN2nXOXHK1a"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -qU langchain langchain-groq"
      ],
      "metadata": {
        "id": "riDSC30axHUE"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import csv\n",
        "\n",
        "from google.colab import userdata\n",
        "from langchain_groq import ChatGroq\n",
        "from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain.agents import create_agent"
      ],
      "metadata": {
        "id": "eqxpiKfOFlU8"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "os.environ[\"GROQ_API_KEY\"] = userdata.get(\"GROQ_API_KEY\")\n",
        "llm = ChatGroq(\n",
        "    model=\"openai/gpt-oss-120b\",\n",
        "    temperature=0.3\n",
        ")\n",
        "\n",
        "print(\"Groq model connected successfully!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yDNackBNFq-I",
        "outputId": "4b2d7754-383c-4278-bcda-200819234547"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Groq model connected successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "SYSTEM = \"\"\"ROLE: You are the friendly assistant for Sweet Crumbs Home Bakery.\n",
        "\n",
        "FACTS:\n",
        "Plum cake Rs 500.\n",
        "Chocolate cake Rs 650.\n",
        "Cupcake Rs 80 each.\n",
        "Orders need 24 hours' notice.\n",
        "All cakes have eggless versions.\n",
        "\n",
        "RULES:\n",
        "Never promise a delivery time or place.\n",
        "If it isn't in FACTS, say \"I'll check with the owner.\"\n",
        "Work out totals carefully.\n",
        "\n",
        "FORMAT:\n",
        "Under 50 words, friendly, English or Telugu matching the customer.\n",
        "\"\"\""
      ],
      "metadata": {
        "id": "F8EUvSCuFvqq"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "prompt = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", SYSTEM),\n",
        "    MessagesPlaceholder(\"history\"),\n",
        "    (\"human\", \"{question}\")\n",
        "])\n",
        "\n",
        "chain = prompt | llm | StrOutputParser()\n",
        "\n",
        "print(\"Bakery assistant chain created!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QotWhDu3GM82",
        "outputId": "18967c07-58aa-4672-ae25-1b439464bf09"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bakery assistant chain created!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "history = []\n",
        "\n",
        "\n",
        "def ask(question: str) -> str:\n",
        "    \"\"\"Ask the bakery assistant a question and remember the conversation.\"\"\"\n",
        "\n",
        "    answer = chain.invoke({\n",
        "        \"history\": history,\n",
        "        \"question\": question\n",
        "    })\n",
        "\n",
        "    history.extend([\n",
        "        (\"human\", question),\n",
        "        (\"ai\", answer)\n",
        "    ])\n",
        "\n",
        "    return answer\n",
        "\n"
      ],
      "metadata": {
        "id": "r22MAflZGXLx"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nMemory demonstration:\")\n",
        "\n",
        "print(ask(\"Hi, I'm Ravi. Do you make eggless cakes?\"))\n",
        "\n",
        "print(ask(\"What's my name?\"))\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nvuDapsAGpyp",
        "outputId": "b414e6d2-0ad8-4b91-a97a-11b0188f62df"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Memory demonstration:\n",
            "Hi Ravi! 😊 Yes, we offer egg‑less versions of all our cakes – plum, chocolate, cupcakes and more. Let me know which one you’d like, and I’ll help you with the details!\n",
            "Your name is Ravi.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nConversation History:\")\n",
        "\n",
        "for message in history:\n",
        "    print(message)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kea0i8VUGwBE",
        "outputId": "ee75eb40-b46f-472d-ae3b-5ee60e794819"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Conversation History:\n",
            "('human', \"Hi, I'm Ravi. Do you make eggless cakes?\")\n",
            "('ai', 'Hi Ravi! 😊 Yes, we offer egg‑less versions of all our cakes – plum, chocolate, cupcakes and more. Let me know which one you’d like, and I’ll help you with the details!')\n",
            "('human', \"What's my name?\")\n",
            "('ai', 'Your name is Ravi.')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def run_tests(path: str = \"test.csv\") -> None:\n",
        "    \"\"\"Run chatbot tests using the provided CSV file.\"\"\"\n",
        "\n",
        "    with open(path, \"r\", encoding=\"utf-8\") as file:\n",
        "        rows = list(csv.DictReader(file))\n",
        "\n",
        "    if not rows:\n",
        "        print(\"No test cases found.\")\n",
        "        return\n",
        "\n",
        "    passed = 0\n",
        "\n",
        "    for row in rows:\n",
        "\n",
        "        answer = chain.invoke({\n",
        "            \"history\": [],\n",
        "            \"question\": row[\"question\"]\n",
        "        })\n",
        "\n",
        "        expected = row[\"must_include\"]\n",
        "\n",
        "        ok = expected.lower() in answer.lower()\n",
        "\n",
        "        if ok:\n",
        "            passed += 1\n",
        "\n",
        "        print(\n",
        "            \"PASS\" if ok else \"FAIL\",\n",
        "            \"|\",\n",
        "            row[\"question\"],\n",
        "            \"->\",\n",
        "            answer[:100]\n",
        "        )\n",
        "\n",
        "    percentage = (passed / len(rows)) * 100\n",
        "\n",
        "    print(\n",
        "        f\"\\n{passed}/{len(rows)} tests passed \"\n",
        "        f\"({percentage:.0f}%)\"\n",
        "    )\n"
      ],
      "metadata": {
        "id": "-GPpmQrsG08s"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nRunning Chatbot Tests:\")\n",
        "\n",
        "run_tests()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9NK7-BcGG37C",
        "outputId": "d34daf46-b085-465f-8840-4c26420c5e50"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Running Chatbot Tests:\n",
            "PASS | How much is a plum cake? -> A plum cake costs Rs 500. (We also have an eggless version if you prefer!)\n",
            "FAIL | Do you make eggless cakes? -> Yes! All our cakes – plum, chocolate, and cupcakes – are available in egg‑less versions. Let us know\n",
            "FAIL | Can I get a cake today evening? -> I'll check with the owner and get back to you!\n",
            "PASS | Do you deliver to Kakinada? -> I'll check with the owner.\n",
            "PASS | What is the price of 6 cupcakes? -> Sure! Six cupcakes will cost ₹480. Let me know if you’d like to add anything else!\n",
            "\n",
            "3/5 tests passed (60%)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 8. CREATE YOUR FIRST LANGCHAIN AGENT\n",
        "# --------------------------------------------------\n",
        "\n",
        "agent_order = create_agent(\n",
        "    model=llm,\n",
        "    tools=[],\n",
        "    system_prompt=SYSTEM\n",
        ")"
      ],
      "metadata": {
        "id": "fJxPwlkTHQpk"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nTesting LangChain Agent:\")\n",
        "\n",
        "result_order = agent_order.invoke({\n",
        "    \"messages\": [\n",
        "        {\n",
        "            \"role\": \"user\",\n",
        "            \"content\": \"Do you make eggless cakes?\"\n",
        "        }\n",
        "    ]\n",
        "})\n",
        "\n",
        "print(result_order[\"messages\"][-1].content)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hynM7UZnHWSx",
        "outputId": "dcd6f452-98e9-403f-f198-c8f8a7d59470"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Testing LangChain Agent:\n",
            "Yes! All our cakes – plum, chocolate and cupcakes – are available in egg‑less versions. Let us know which one you’d like!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result_order = agent_order.invoke({\n",
        "    \"messages\": [\n",
        "        {\n",
        "            \"role\": \"user\",\n",
        "            \"content\": \"What is the price of a chocolate cake?\"\n",
        "        }\n",
        "    ]\n",
        "})\n",
        "\n",
        "print(result_order[\"messages\"][-1].content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E8MN5SawHcNa",
        "outputId": "4290566a-924a-40da-fdc3-3a8f32e7be27"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The chocolate cake costs Rs 650. 😊\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 1: Rewrite the system prompt for your own business\n",
        "SYSTEM_TASK1 = \"\"\"\n",
        "ROLE: You are a friendly assistant for Smart Stationery.\n",
        "\n",
        "FACTS:\n",
        "Notebook costs Rs 50.\n",
        "Pen costs Rs 10.\n",
        "Pencil costs Rs 5.\n",
        "School bags cost Rs 500.\n",
        "Orders are accepted during working hours.\n",
        "\n",
        "RULES:\n",
        "Never invent product prices.\n",
        "If you don't know something, say \"I'll check with the shop owner.\"\n",
        "\n",
        "FORMAT:\n",
        "Reply politely in under 50 words.\n",
        "Use English or Telugu according to the customer.\n",
        "\"\"\"\n",
        "\n",
        "prompt_task1 = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", SYSTEM_TASK1),\n",
        "    MessagesPlaceholder(\"history\"),\n",
        "    (\"human\", \"{question}\")\n",
        "])\n",
        "\n",
        "chain_task1 = prompt_task1 | llm | StrOutputParser()\n",
        "\n",
        "print(chain_task1.invoke({\n",
        "    \"history\": [],\n",
        "    \"question\": \"What is the price of a notebook and pen?\"\n",
        "}))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bpvgMDQiHtdS",
        "outputId": "bcbbd004-5674-4a3e-f3f9-1cd0f3d91f72"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A notebook costs Rs 50 and a pen costs Rs 10.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 2: Create 10 customer test cases\n",
        "test_cases = [\n",
        "    {\n",
        "        \"question\": \"What is the price of a notebook?\",\n",
        "        \"must_include\": \"50\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"How much does a pen cost?\",\n",
        "        \"must_include\": \"10\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"What is the price of a pencil?\",\n",
        "        \"must_include\": \"5\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"How much is a school bag?\",\n",
        "        \"must_include\": \"500\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"Do you sell notebooks?\",\n",
        "        \"must_include\": \"notebook\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"What is the price of a pen and pencil?\",\n",
        "        \"must_include\": \"15\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"How much do two notebooks cost?\",\n",
        "        \"must_include\": \"100\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"Do you sell school bags?\",\n",
        "        \"must_include\": \"school bag\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"What is the price of an eraser?\",\n",
        "        \"must_include\": \"check with the shop owner\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"Can I buy a notebook?\",\n",
        "        \"must_include\": \"notebook\"\n",
        "    }\n",
        "]\n",
        "\n",
        "\n",
        "passed = 0\n",
        "\n",
        "for test in test_cases:\n",
        "\n",
        "    answer = chain_task1.invoke({\n",
        "        \"history\": [],\n",
        "        \"question\": test[\"question\"]\n",
        "    })\n",
        "\n",
        "    expected = test[\"must_include\"]\n",
        "\n",
        "    result = expected.lower() in answer.lower()\n",
        "\n",
        "    if result:\n",
        "        passed += 1\n",
        "\n",
        "    print(\n",
        "        \"PASS\" if result else \"FAIL\",\n",
        "        \"|\",\n",
        "        test[\"question\"],\n",
        "        \"->\",\n",
        "        answer\n",
        "    )\n",
        "\n",
        "print(\"\\nTotal tests:\", len(test_cases))\n",
        "print(\"Passed:\", passed)\n",
        "print(\"Pass percentage:\", (passed / len(test_cases)) * 100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e5yB0r_sHz9s",
        "outputId": "610c6d01-fb47-43ea-a65a-8c52379c2f6a"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PASS | What is the price of a notebook? -> A notebook costs Rs 50.\n",
            "PASS | How much does a pen cost? -> A pen costs Rs 10.\n",
            "PASS | What is the price of a pencil? -> A pencil costs Rs 5.\n",
            "PASS | How much is a school bag? -> A school bag costs Rs 500. Let us know if you’d like to place an order!\n",
            "PASS | Do you sell notebooks? -> Yes, we sell notebooks. Each notebook is priced at Rs 50. Let us know if you’d like to place an order or need information about our pens, pencils, or school bags!\n",
            "FAIL | What is the price of a pen and pencil? -> A pen costs Rs 10 and a pencil costs Rs 5.\n",
            "PASS | How much do two notebooks cost? -> Two notebooks will cost Rs 100.\n",
            "PASS | Do you sell school bags? -> Yes, we have school bags available for Rs 500 each. You can place an order during our working hours. Let us know if you’d like to purchase one!\n",
            "PASS | What is the price of an eraser? -> I’m not sure about the eraser price at the moment. I’ll check with the shop owner and get back to you.\n",
            "PASS | Can I buy a notebook? -> Sure! A notebook is available for Rs 50. Let us know the quantity you need, and we’ll arrange it during our working hours.\n",
            "\n",
            "Total tests: 10\n",
            "Passed: 9\n",
            "Pass percentage: 90.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 3: Change one prompt instruction and compare results\n",
        "SYSTEM_TASK3 = SYSTEM_TASK1.replace(\n",
        "    \"under 50 words\",\n",
        "    \"under 15 words\"\n",
        ")\n",
        "\n",
        "prompt_task3 = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", SYSTEM_TASK3),\n",
        "    MessagesPlaceholder(\"history\"),\n",
        "    (\"human\", \"{question}\")\n",
        "])\n",
        "\n",
        "chain_task3 = prompt_task3 | llm | StrOutputParser()\n",
        "\n",
        "\n",
        "question = \"What are the prices of notebooks, pens and pencils?\"\n",
        "\n",
        "print(\"Original prompt response:\")\n",
        "\n",
        "answer1 = chain_task1.invoke({\n",
        "    \"history\": [],\n",
        "    \"question\": question\n",
        "})\n",
        "\n",
        "print(answer1)\n",
        "\n",
        "\n",
        "print(\"\\nModified prompt response:\")\n",
        "\n",
        "answer2 = chain_task3.invoke({\n",
        "    \"history\": [],\n",
        "    \"question\": question\n",
        "})\n",
        "\n",
        "print(answer2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vna0sgIQH7Q4",
        "outputId": "90afc0b8-0589-425b-8883-7f328a630f63"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original prompt response:\n",
            "Sure!  \n",
            "- Notebook: Rs 50 each  \n",
            "- Pen: Rs 10 each  \n",
            "- Pencil: Rs 5 each  \n",
            "\n",
            "Let me know if you need anything else!\n",
            "\n",
            "Modified prompt response:\n",
            "Notebook: Rs 50, Pen: Rs 10, Pencil: Rs 5.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 4: Change temperature to 1.0 and run tests twice\n",
        "llm_high = ChatGroq(\n",
        "    model=\"openai/gpt-oss-120b\",\n",
        "    temperature=1.0\n",
        ")\n",
        "\n",
        "chain_high = prompt_task1 | llm_high | StrOutputParser()\n",
        "\n",
        "\n",
        "question = \"Suggest a notebook for a college student.\"\n",
        "\n",
        "print(\"First response:\")\n",
        "\n",
        "response1 = chain_high.invoke({\n",
        "    \"history\": [],\n",
        "    \"question\": question\n",
        "})\n",
        "\n",
        "print(response1)\n",
        "\n",
        "\n",
        "print(\"\\nSecond response:\")\n",
        "\n",
        "response2 = chain_high.invoke({\n",
        "    \"history\": [],\n",
        "    \"question\": question\n",
        "})\n",
        "\n",
        "print(response2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rqqfRIg2IB_l",
        "outputId": "1f1f3176-03c2-46f1-9e1e-6ffcc7e7ce09"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First response:\n",
            "For a college student, we recommend our durable, 200‑page ruled notebook—perfect for lectures and notes. It’s compact, has a sturdy cover, and costs just Rs 50. Let us know if you’d like to place an order!\n",
            "\n",
            "Second response:\n",
            "We recommend our durable college notebook – A4 size with 80 gsm paper, sturdy binding, and a soft‑cover design. It’s perfect for notes, assignments and project work, and it’s just Rs 50. Let us know if you’d like to place an order!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 5: Classify three business jobs\n",
        "business_tasks = [\n",
        "    {\n",
        "        \"task\": \"Calculate the total price of products\",\n",
        "        \"type\": \"Plain Python code\"\n",
        "    },\n",
        "    {\n",
        "        \"task\": \"Answer customer questions about products\",\n",
        "        \"type\": \"One LLM call\"\n",
        "    },\n",
        "    {\n",
        "        \"task\": \"Check stock, calculate bills and prepare orders using tools\",\n",
        "        \"type\": \"AI Agent\"\n",
        "    }\n",
        "]\n",
        "\n",
        "for item in business_tasks:\n",
        "    print(\"Task:\", item[\"task\"])\n",
        "    print(\"Category:\", item[\"type\"])\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uxTzZCyWIHW0",
        "outputId": "c04a63e0-0c55-4bf0-8f8d-d95cfaa13cb1"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Task: Calculate the total price of products\n",
            "Category: Plain Python code\n",
            "\n",
            "Task: Answer customer questions about products\n",
            "Category: One LLM call\n",
            "\n",
            "Task: Check stock, calculate bills and prepare orders using tools\n",
            "Category: AI Agent\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#two Python functions with type hints and docstrings\n",
        "def get_price(item: str) -> int:\n",
        "    \"\"\"Return the price of a bakery item.\"\"\"\n",
        "\n",
        "    menu = {\n",
        "        \"plum cake\": 500,\n",
        "        \"chocolate cake\": 650,\n",
        "        \"cupcake\": 80\n",
        "    }\n",
        "\n",
        "    return menu.get(item.lower(), 0)\n",
        "\n",
        "\n",
        "print(get_price(\"plum cake\"))\n",
        "print(get_price(\"cupcake\"))\n",
        "print(get_price(\"chocolate cake\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BDcY5Eb9ISBH",
        "outputId": "8f81ef7e-d35c-4d46-c0dd-b89272b14222"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "500\n",
            "80\n",
            "650\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Check product availability\n",
        "def is_available(item: str) -> bool:\n",
        "    \"\"\"Check whether a bakery item is available.\"\"\"\n",
        "\n",
        "    menu = [\n",
        "        \"plum cake\",\n",
        "        \"chocolate cake\",\n",
        "        \"cupcake\"\n",
        "    ]\n",
        "\n",
        "    return item.lower() in menu\n",
        "\n",
        "\n",
        "print(is_available(\"plum cake\"))\n",
        "print(is_available(\"donut\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CJMZyFGeIW8_",
        "outputId": "d8f0dee4-933d-4420-debf-34957d10046a"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n"
          ]
        }
      ]
    }
  ]
}