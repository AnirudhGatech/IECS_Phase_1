<div align="center">

# 🔍 GTSearch  
**A Semantic Search Engine Tailored for Georgia Tech**

</div>

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Scrapy](https://img.shields.io/badge/Scrapy-Crawling-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-informational?style=for-the-badge&logo=openai)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple?style=for-the-badge&logo=pinecone)
![Render](https://img.shields.io/badge/Render-Hosting-007bff?style=for-the-badge&logo=render)

</div>

---

## 📌 Overview

**GTSearch** is a domain-specific semantic search engine focused on Georgia Tech-related content. I built it to solve the problem of inaccurate or irrelevant results returned by general-purpose search engines and LLMs when answering academic or institutional queries.

The system combines intelligent web crawling, vector similarity-based filtering, and GPT-powered response generation—all built, tuned, and deployed by me.

---

## 🧠 Features

- 🔎 Georgia Tech-specific semantic search
- 🌐 Web crawler using Scrapy + FastEmbed for filtering
- 📦 Vector storage and search with Pinecone
- 💬 Contextual response generation using OpenAI GPT-3.5
- 🖥️ Full-stack web integration with Flask + React
- ☁️ Deployed on Render with continuous delivery support

---

## 🏗️ System Architecture

### 📘 Crawling Module  
<img width="1440" alt="Crawler Design" src="https://github.com/kslohith/gtsearch/assets/32676813/11f09439-ca89-42ab-afdf-957bad5d33fa">

This module starts with seed URLs and filters crawled text based on semantic similarity with a Georgia Tech knowledge base embedding.

---

### 📗 Retrieval-Augmented Generation (RAG) Module  
<img width="1440" alt="RAG Flow" src="https://github.com/kslohith/gtsearch/assets/32676813/6025f4c4-f127-4761-8b65-a76a963f02bd">

For every user query, top-k relevant documents are retrieved from Pinecone and passed as context to GPT-3.5 to generate the final response.

---

## 🛠️ Installation & Usage

### 🔧 Install Dependencies
```bash
pip install scrapy flask fastembed openai pinecone-client
