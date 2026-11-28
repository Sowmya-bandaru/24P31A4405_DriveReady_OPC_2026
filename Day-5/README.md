Day 5 – Memory and RAG

📌 Project Overview

As part of Day 5 of the Agentic AI Workshop, I learned about Memory and Retrieval-Augmented Generation (RAG) and how an AI agent can retrieve information from external documents before generating answers.

For the practical implementation, I built a PDF-based Question-Answering System using Python, Sentence Transformers, FAISS, and Groq LLM.

 I experimented with story, The Missing Coin, a one-page moral story. I uploaded it to my RAG system and tested the application by asking questions about the story.

📚 Topics Covered

1. Types of Memory

Learned about three types of memory used in AI agents:

Conversation Memory: Remembers messages within the current conversation.

Customer Memory: Stores information about users across conversations.

Knowledge Memory: Retrieves information from external documents and business knowledge sources.

2. Conversation Memory

Understanding checkpointers.

Understanding thread_id.

Maintaining separate conversation histories.

Learning how an agent remembers previous messages.

3. Embeddings

Understanding how text is converted into numerical vectors.

Learning semantic similarity.

Exploring Sentence Transformer embedding models.

Experimenting with all-MiniLM-L6-v2 and all-mpnet-base-v2.

4. Vector Databases

Understanding vector storage and similarity search.

Learning about ChromaDB.

Understanding how FAISS performs vector indexing and similarity search.

5. Chunking

Splitting large documents into smaller text segments.

Understanding chunk size and chunk overlap.

Using chunks to improve relevant information retrieval.

6. Retrieval-Augmented Generation (RAG)

Understanding the Retrieve, Augment, Generate workflow.

Retrieving relevant document content.

Providing retrieved context to an LLM.

Generating answers based on document information.

Reducing hallucinations by restricting answers to the provided context.

🛠️ Technologies Used

Python

Google Colab

PyMuPDF (PDF text extraction)

Tesseract OCR (text extraction from scanned pages)

Sentence Transformers

FAISS (vector indexing and similarity search)

NumPy

Groq API

GPT-OSS 20B (LLM)

⚙️ Implementation Workflow

PDF Upload: Upload a PDF document through Google Colab.

Text Extraction: Extract text using PyMuPDF. If a page contains no extractable text, use OCR.

Text Chunking: Divide the extracted text into smaller chunks using a chunk size of 500 characters and an overlap of 100 characters.

Embedding Generation: Convert text chunks into numerical vectors using all-MiniLM-L6-v2.

Vector Indexing: Store the embeddings in a FAISS index using IndexFlatIP.

Question Retrieval: Convert the user's question into an embedding and retrieve the top 3 relevant chunks.

Context Augmentation: Pass the retrieved document content along with the question to the LLM.

Answer Generation: Use Groq's GPT-OSS 20B model to generate an answer based only on the retrieved PDF context.

🔄 RAG Architecture

       Upload PDF Document
               |
               v
        Extract PDF Text
               |
               v
          Text Chunking
        (500 / 100 overlap)
               |
               v
       Generate Embeddings
      (Sentence Transformers)
               |
               v
        FAISS Vector Index
               |
               v
        User Asks Question
               |
               v
      Generate Query Embedding
               |
               v
       Retrieve Top 3 Chunks
               |
               v
       Provide Context to LLM
               |
               v
       Groq – GPT-OSS 20B
               |
               v
         Generate Answer

🧪 My Practical Experiment – The Missing Coin

For testing the RAG implementation, I used my own moral story PDF, The Missing Coin, instead of the Little Lantern document provided by the trainer.

I uploaded the PDF, allowed the system to extract and process its content, and asked questions to check whether the LLM could retrieve the correct information.

Sample Questions Tested

Who found the missing purse?

What was written on the folded note?

Why did Anika put a notice on the shop door?

How did Mr. Dev prove that the purse belonged to him?

Why did Mr. Dev need the money?

How did Anika's actions improve the shop's reputation?

I also tested questions about information that was not mentioned in the story to check whether the system could avoid generating unsupported answers.

🎯 What I Learned

Through this practical session, I learned:

How to build a basic RAG pipeline from scratch.

How to extract text from PDF documents.

How OCR helps process scanned PDF pages.

Why documents are divided into chunks before embedding generation.

How embedding models represent text as numerical vectors.

How FAISS indexes vectors and retrieves semantically similar content.

How to connect a Groq LLM to a custom document-retrieval pipeline.

How retrieved context helps an LLM answer questions using external knowledge.

Why an AI system should acknowledge missing information instead of hallucinating answers.

💡 Key Takeaway

This session helped me understand how an LLM can be connected to external knowledge sources instead of depending only on its pre-trained knowledge.

By experimenting with my own PDF document, I got practical experience in building and testing a document-based RAG application.

Day 5 Learning Outcome: Successfully implemented and experimented with a PDF-based RAG Question-Answering System using my own test document.
