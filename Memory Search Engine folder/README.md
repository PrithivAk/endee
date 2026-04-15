streamlit
sentence-transformers
numpy
pandas
scikit-learn
tqdm
# 🧠 AI Memory Search Engine (Semantic Search using Endee)

## 📌 Project Overview
The AI Memory Search Engine is a lightweight system that allows users to store notes, ideas, and information, and later retrieve them intelligently using semantic search.

Unlike traditional keyword-based search, this system understands the meaning of user queries and returns the most relevant stored memories using vector embeddings.

This project demonstrates modern AI concepts such as embeddings, vector databases, and retrieval systems.

---

## 🚀 Features
- 🧠 Store personal memories (notes, ideas, tasks)
- 🔍 Semantic search (meaning-based retrieval)
- ⚡ Fast and efficient vector similarity search
- 💬 Simple and interactive UI using Streamlit
- 🔗 Designed to integrate with Endee vector database

---

## 🏗️ System Architecture

1. User inputs a memory (text)
2. Text is converted into embeddings
3. Embeddings are stored in a vector database (Endee)
4. User enters a query
5. Query is converted into embedding
6. System performs similarity search
7. Most relevant memories are retrieved and displayed

---

## 🧰 Tech Stack

- Python
- Streamlit (Frontend UI)
- Sentence Transformers (Embeddings)
- NumPy (Similarity Computation)
- Endee (Vector Database)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
