{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPO+A9VqThjPMzD+XN6VOG6",
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
        "<a href=\"https://colab.research.google.com/github/Sowmya-bandaru/24P31A4405_DriveReady_OPC_2026/blob/main/Day-2/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "id": "sYH0-__0MShY"
      },
      "outputs": [],
      "source": [
        "!pip install -q langchain_groq"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_groq import ChatGroq\n",
        "from google.colab import userdata\n",
        "import os\n",
        "import json\n",
        "import functools"
      ],
      "metadata": {
        "id": "_kQwfB_lMZvd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    os.environ[\"GROQ_API_KEY\"] = userdata.get(\"GROQ_API_KEY\")\n",
        "except Exception:\n",
        "    print(\"Please add GROQ_API_KEY to your Colab Secrets.\")"
      ],
      "metadata": {
        "id": "zn2fuFQ3Ma2h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "llm = ChatGroq(\n",
        "    model=\"openai/gpt-oss-120b\",\n",
        "    temperature=0\n",
        ")"
      ],
      "metadata": {
        "id": "gjWX_ctSMdzT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "PzNjACKdgZwX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "response = llm.invoke([\n",
        "    (\"system\", \"You are a funny joker\"),\n",
        "    (\"human\", \"Tell me a joke\")\n",
        "])\n",
        "\n",
        "print(response.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ejrwWY3BMiHr",
        "outputId": "b40b8000-8801-477f-d916-80bfdc26da99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Why did the scarecrow become a stand‑up comedian?\n",
            "\n",
            "Because he was outstanding in his field… and finally got a *corn*ed audience! 😄\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "SYSTEM = \"\"\"ROLE: You are the assistant for Sweet Crumbs Home Bakery.\n",
        "\n",
        "FACTS:\n",
        "We bake to order. Orders need 24 hours' notice.\n",
        "All cakes have eggless versions.\n",
        "Plum cake Rs 500.\n",
        "Chocolate cake Rs 650.\n",
        "Cupcake Rs 80.\n",
        "\n",
        "RULES:\n",
        "Never promise a delivery time.\n",
        "If the answer isn't in FACTS, say \"I'll check with the owner.\"\n",
        "\n",
        "FORMAT:\n",
        "Under 50 words, friendly, English or Telugu matching the customer.\"\"\""
      ],
      "metadata": {
        "id": "BLiJz2zXMjYT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response = llm.invoke([\n",
        "    (\"system\", SYSTEM),\n",
        "    (\"human\", \"Can I get an eggless cake today evening?\")\n",
        "])\n",
        "\n",
        "print(response.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KemlJCA0MmIo",
        "outputId": "f5edaef8-f650-46a7-81c5-8e1cc05fbae9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "We do have egg‑less versions, but we need at least 24 hours’ notice for any cake. So we can’t prepare one for this evening. Let us know which cake you’d like, and we’ll schedule it for you!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "MENU = {\n",
        "    \"plum cake\": 500,\n",
        "    \"chocolate cake\": 650,\n",
        "    \"cupcake\": 80\n",
        "}"
      ],
      "metadata": {
        "id": "zO_y0tQbMoxJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(MENU[\"plum cake\"])\n",
        "\n",
        "print(MENU.get(\"donut\", \"donuts not available\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B9nl2LS7Mslc",
        "outputId": "244feea9-dc10-444f-9782-5ecce5e0af06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "500\n",
            "donuts not available\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "order = {\n",
        "    \"name\": \"Ravi\",\n",
        "    \"item\": \"plum cake\",\n",
        "    \"qty\": 2,\n",
        "    \"eggless\": True\n",
        "}\n",
        "\n",
        "print(order)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A-eRd_V1Mv1v",
        "outputId": "24a3ae6e-25a3-45c3-fa09-add410182961"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'Ravi', 'item': 'plum cake', 'qty': 2, 'eggless': True}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total = order[\"qty\"] * MENU[order[\"item\"]]\n",
        "\n",
        "print(\"Total price:\", total)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XOeLYT_oMyLt",
        "outputId": "6c7465ff-0156-4ffe-e3d4-03b384b58b57"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total price: 1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "text = json.dumps(order)\n",
        "\n",
        "print(text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xsan5ZWOM0rq",
        "outputId": "3206d245-64c8-4622-f4d7-9a431087111d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{\"name\": \"Ravi\", \"item\": \"plum cake\", \"qty\": 2, \"eggless\": true}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "back = json.loads(text)\n",
        "\n",
        "print(back)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fC5s0OqIM4Na",
        "outputId": "d21ab66e-da30-4350-9d94-6108b6e14145"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'Ravi', 'item': 'plum cake', 'qty': 2, 'eggless': True}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def get_price(item: str, qty: int = 1) -> int:\n",
        "    return MENU[item.lower().strip()] * qty\n",
        "\n",
        "print(get_price(\"cupcake\", 6))\n",
        "print(get_price(\"Plum Cake\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FS3SuHZRM8Dx",
        "outputId": "0437c6be-1486-4314-cfa5-c6012d319a4f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "480\n",
            "500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def get_price(item, qty=1):\n",
        "    \"\"\"Return the total price in rupees for qty of an item on the Sweet Crumbs menu.\"\"\"\n",
        "\n",
        "    return MENU[item.lower().strip()] * qty\n",
        "\n",
        "print(get_price(\"cupcake\", 6))\n",
        "print(get_price(\"Plum Cake\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ma0HVUmENDn1",
        "outputId": "9523aa0e-86f4-4b4e-9e0e-50cc81355d2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "480\n",
            "500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "print(a+b)\n",
        "print(\"hi\")"
      ],
      "metadata": {
        "id": "s9Vy0KAnNJcO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    a = 10\n",
        "    print(a + b)\n",
        "    print(\"hi\")\n",
        "\n",
        "except:\n",
        "    print(\"b is not defined\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1ns1fOKDNKih",
        "outputId": "70ef1409-58cd-42ea-c6de-b69573f1cc4b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "b is not defined\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def log_call(func):\n",
        "\n",
        "    @functools.wraps(func)\n",
        "    def wrapper(*args, **kwargs):\n",
        "\n",
        "        result = func(*args, **kwargs)\n",
        "\n",
        "        print(f\"[log] {func.__name__}{args} -> {result!r}\")\n",
        "\n",
        "        return result\n",
        "\n",
        "    return wrapper"
      ],
      "metadata": {
        "id": "cyUmU40xNM-i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "@log_call\n",
        "def get_price(item: str, qty: int = 1) -> int:\n",
        "\n",
        "    \"\"\"Return the total price in rupees for qty of an item on the menu.\"\"\"\n",
        "\n",
        "    return MENU[item.lower().strip()] * qty\n",
        "\n",
        "\n",
        "print(get_price(\"cupcake\", 6))\n",
        "print(get_price(\"Plum Cake\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ELC784CoNPfE",
        "outputId": "08f2d28b-c3a7-4bce-ffc9-0c934000c017"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[log] get_price('cupcake', 6) -> 480\n",
            "480\n",
            "[log] get_price('Plum Cake',) -> 500\n",
            "500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "history = [\n",
        "    (\"system\", SYSTEM)\n",
        "]\n",
        "\n",
        "MAX_TURNS = 8\n",
        "\n",
        "print(history)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zNlk33BZNRlm",
        "outputId": "ba1e0632-1c4e-4ba0-ff23-b9c8aaa9dd0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[('system', 'ROLE: You are the assistant for Sweet Crumbs Home Bakery.\\n\\nFACTS:\\nWe bake to order. Orders need 24 hours\\' notice.\\nAll cakes have eggless versions.\\nPlum cake Rs 500.\\nChocolate cake Rs 650.\\nCupcake Rs 80.\\n\\nRULES:\\nNever promise a delivery time.\\nIf the answer isn\\'t in FACTS, say \"I\\'ll check with the owner.\"\\n\\nFORMAT:\\nUnder 50 words, friendly, English or Telugu matching the customer.')]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def chat(user_text: str) -> str:\n",
        "\n",
        "    history.append((\"human\", user_text))\n",
        "\n",
        "    recent = [history[0]] + history[1:][-MAX_TURNS:]\n",
        "\n",
        "    try:\n",
        "        response = llm.invoke(recent)\n",
        "\n",
        "        reply = response.content\n",
        "\n",
        "    except Exception as error:\n",
        "\n",
        "        print(\"Error:\", error)\n",
        "\n",
        "        reply = \"I can't reach the server right now. Please try again shortly.\"\n",
        "\n",
        "    history.append((\"assistant\", reply))\n",
        "\n",
        "    return reply"
      ],
      "metadata": {
        "id": "jmFrD9ILNT_g"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "\n",
        "    text = input(\"You: \")\n",
        "\n",
        "    if text.lower().strip() in (\"bye\", \"exit\", \"quit\"):\n",
        "\n",
        "        print(\"Bot: Thank you for visiting Sweet Crumbs!\")\n",
        "\n",
        "        break\n",
        "\n",
        "    print(\"Bot:\", chat(text))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jRdQoiy3NWuL",
        "outputId": "498f67a2-15e4-4c32-b122-a9cf4455d819"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You: My name is Ravi.\n",
            "Bot: Got it, Ravi! How can I help you with a cake or cupcakes today?\n",
            "You: I want two chocolate cakes.\n",
            "Bot: Sure, Ravi! Two chocolate cakes will be Rs 1,300. We need at least 24 hours notice and can make them egg‑less if you like. Let me know your preferred pickup date.\n",
            "You: What is the price of chocolate cake?\n",
            "Bot: Chocolate cake costs Rs 650 each (egg‑less version is also available).\n",
            "You: Do you have eggless cakes?\n",
            "Bot: Yes, Ravi! All our cakes, including chocolate, plum, and cupcakes, are available in egg‑less versions. Let me know if you’d like to place an order!\n",
            "You: What is my name?\n",
            "Bot: I'll check with the owner.\n",
            "You: bye\n",
            "Bot: Thank you for visiting Sweet Crumbs!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# You: My name is Ravi.\n",
        "# You: I want two chocolate cakes.\n",
        "# You: What is the price of chocolate cake?\n",
        "# You: Do you have eggless cakes?\n",
        "# You: What is my name?\n",
        "# You: bye"
      ],
      "metadata": {
        "id": "I6yVArHHNZ-l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 1 — Add more products to the bakery menu\n",
        "MENU[\"vanilla cake\"] = 550\n",
        "MENU[\"brownie\"] = 120\n",
        "MENU[\"cookie\"] = 40\n",
        "\n",
        "print(\"Updated Bakery Menu:\")\n",
        "\n",
        "for item, price in MENU.items():\n",
        "    print(item, \":\", \"Rs.\", price)"
      ],
      "metadata": {
        "id": "riOvra4_NyYA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c9db638a-f574-4263-9309-cf443679b33e"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated Bakery Menu:\n",
            "plum cake : Rs. 500\n",
            "chocolate cake : Rs. 650\n",
            "cupcake : Rs. 80\n",
            "vanilla cake : Rs. 550\n",
            "brownie : Rs. 120\n",
            "cookie : Rs. 40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 2 — Take customer order details and calculate the bill\n",
        "customer_name = input(\"Enter customer name: \")\n",
        "\n",
        "item = input(\"Enter cake name: \").lower().strip()\n",
        "\n",
        "quantity = int(input(\"Enter quantity: \"))\n",
        "\n",
        "if item in MENU:\n",
        "\n",
        "    total = MENU[item] * quantity\n",
        "\n",
        "    order = {\n",
        "        \"name\": customer_name,\n",
        "        \"item\": item,\n",
        "        \"quantity\": quantity,\n",
        "        \"total\": total\n",
        "    }\n",
        "\n",
        "    print(\"\\nOrder Details:\")\n",
        "    print(order)\n",
        "\n",
        "else:\n",
        "    print(\"Sorry, this item is not available.\")"
      ],
      "metadata": {
        "id": "Gm4fHLhIOBvL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a90c60f3-a897-4aed-b2bc-996dd98564cc"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter customer name: sowmya\n",
            "Enter cake name: vanilla\n",
            "Enter quantity: 500\n",
            "Sorry, this item is not available.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 3 — Save an order in JSON format\n",
        "import json\n",
        "\n",
        "order = {\n",
        "    \"name\": \"Priya\",\n",
        "    \"item\": \"chocolate cake\",\n",
        "    \"quantity\": 2,\n",
        "    \"eggless\": True,\n",
        "    \"total\": 1300\n",
        "}\n",
        "\n",
        "json_data = json.dumps(order, indent=4)\n",
        "\n",
        "print(\"JSON Order:\")\n",
        "print(json_data)\n",
        "\n",
        "converted_order = json.loads(json_data)\n",
        "\n",
        "print(\"\\nConverted Python Dictionary:\")\n",
        "print(converted_order)"
      ],
      "metadata": {
        "id": "j7Ged6PiOLFN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d5c483b1-f259-4e73-9de6-8472c2d2c65a"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "JSON Order:\n",
            "{\n",
            "    \"name\": \"Priya\",\n",
            "    \"item\": \"chocolate cake\",\n",
            "    \"quantity\": 2,\n",
            "    \"eggless\": true,\n",
            "    \"total\": 1300\n",
            "}\n",
            "\n",
            "Converted Python Dictionary:\n",
            "{'name': 'Priya', 'item': 'chocolate cake', 'quantity': 2, 'eggless': True, 'total': 1300}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 4 — Handle invalid menu items\n",
        "def calculate_bill(item, quantity):\n",
        "\n",
        "    try:\n",
        "        item = item.lower().strip()\n",
        "\n",
        "        price = MENU[item]\n",
        "\n",
        "        total = price * quantity\n",
        "\n",
        "        print(\"Item:\", item)\n",
        "        print(\"Quantity:\", quantity)\n",
        "        print(\"Total price: Rs.\", total)\n",
        "\n",
        "    except KeyError:\n",
        "        print(\"Sorry, this item is not available.\")\n",
        "\n",
        "    except TypeError:\n",
        "        print(\"Please enter valid details.\")\n",
        "\n",
        "\n",
        "calculate_bill(\"chocolate cake\", 2)\n",
        "\n",
        "calculate_bill(\"pizza\", 1)"
      ],
      "metadata": {
        "id": "_sOewoKPOTEY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4d117d77-b083-446d-b88e-841b4120404a"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Item: chocolate cake\n",
            "Quantity: 2\n",
            "Total price: Rs. 1300\n",
            "Sorry, this item is not available.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 5 — Create a decorator to count function calls\n",
        "def count_calls(func):\n",
        "\n",
        "    count = 0\n",
        "\n",
        "    @functools.wraps(func)\n",
        "    def wrapper(*args, **kwargs):\n",
        "\n",
        "        nonlocal count\n",
        "\n",
        "        count += 1\n",
        "\n",
        "        print(\"Function called:\", count, \"times\")\n",
        "\n",
        "        return func(*args, **kwargs)\n",
        "\n",
        "    return wrapper\n",
        "\n",
        "\n",
        "@count_calls\n",
        "def bakery_message(name):\n",
        "\n",
        "    return \"Welcome to Sweet Crumbs, \" + name\n",
        "\n",
        "\n",
        "print(bakery_message(\"Ravi\"))\n",
        "print(bakery_message(\"Priya\"))\n",
        "print(bakery_message(\"Sowmya\"))"
      ],
      "metadata": {
        "id": "FSfb_rrgOWa7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a74a83ca-7391-4461-d554-2d8df023e295"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Function called: 1 times\n",
            "Welcome to Sweet Crumbs, Ravi\n",
            "Function called: 2 times\n",
            "Welcome to Sweet Crumbs, Priya\n",
            "Function called: 3 times\n",
            "Welcome to Sweet Crumbs, Sowmya\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 6 — Test chatbot memory with your own conversation\n",
        "history = [\n",
        "    (\"system\", SYSTEM)\n",
        "]\n",
        "\n",
        "print(chat(\"My name is Sowmya.\"))\n",
        "print(chat(\"I want one plum cake.\"))\n",
        "print(chat(\"What is my name?\"))\n",
        "print(chat(\"Which cake did I order?\"))"
      ],
      "metadata": {
        "id": "ph4b3yD8OdxE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d8572601-21e2-484d-ca7d-f2fd5eedf583"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi Sowmya! Nice to meet you. How can we help you today with our cakes or cupcakes?\n",
            "Great choice, Sowmya! A plum cake is ₹500 (egg‑less version also available). We’ll need at least 24 hours notice to bake it fresh. Let me know the size and any customization you’d like!\n",
            "I'll check with the owner.\n",
            "You ordered a plum cake.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 7 — Create a simple chatbot test set\n",
        "test_questions = [\n",
        "    \"What is the price of a plum cake?\",\n",
        "    \"Do you have eggless cakes?\",\n",
        "    \"How much does a cupcake cost?\",\n",
        "    \"Do you promise delivery today?\",\n",
        "    \"Do you sell pizza?\"\n",
        "]\n",
        "\n",
        "for question in test_questions:\n",
        "\n",
        "    print(\"Customer:\", question)\n",
        "\n",
        "    answer = chat(question)\n",
        "\n",
        "    print(\"Bot:\", answer)\n",
        "\n",
        "    print(\"-\" * 50)"
      ],
      "metadata": {
        "id": "m8zyTWSgOky5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fa80b546-f094-480e-ac1c-6a6a3d7401cb"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Customer: What is the price of a plum cake?\n",
            "Bot: A plum cake costs ₹500. (Egg‑less version is also ₹500.)\n",
            "--------------------------------------------------\n",
            "Customer: Do you have eggless cakes?\n",
            "Bot: Yes! Every cake we make, including plum, chocolate, and cupcakes, is also available in an egg‑less version. Let us know which one you’d like!\n",
            "--------------------------------------------------\n",
            "Customer: How much does a cupcake cost?\n",
            "Bot: A cupcake costs ₹80 (egg‑less version is the same price).\n",
            "--------------------------------------------------\n",
            "Customer: Do you promise delivery today?\n",
            "Bot: I'll check with the owner.\n",
            "--------------------------------------------------\n",
            "Customer: Do you sell pizza?\n",
            "Bot: I'll check with the owner.\n",
            "--------------------------------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "sVfDeJRnOriD"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}