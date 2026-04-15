import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# -------------------------------
# Load embedding model
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------------
# In-memory storage
# -------------------------------
if "memories" not in st.session_state:
    st.session_state.memories = []

if "embeddings" not in st.session_state:
    st.session_state.embeddings = []

# -------------------------------
# Functions
# -------------------------------

def add_memory(text):
    embedding = model.encode([text])[0]
    st.session_state.memories.append(text)
    st.session_state.embeddings.append(embedding)

def search_memory(query):
    if not st.session_state.memories:
        return []

    query_embedding = model.encode([query])[0]
    embeddings = np.array(st.session_state.embeddings)

    similarities = np.dot(embeddings, query_embedding)
    top_indices = np.argsort(similarities)[
