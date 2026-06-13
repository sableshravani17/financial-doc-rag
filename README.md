Financial Document Management System with RAG

Project Overview
This project is a Financial Document Management API built using FastAPI. It allows users to upload, manage, and retrieve financial documents. It also includes a RAG system for semantic search using embeddings and a vector database.

Features

Authentication
User registration
User login

Document Management
Upload financial documents in PDF format
Retrieve all documents
Retrieve document details
Delete documents
Search documents using metadata

Role Based Access Control
Roles include Admin, Analyst, Auditor, and Client
Assign roles to users
Manage user permissions

RAG Implementation
Extract text from uploaded documents
Split text into chunks
Generate embeddings using sentence transformer model
Store embeddings in FAISS vector database
Perform semantic search using query

RAG Pipeline
Document goes through text extraction, chunking, embedding generation, storage in vector database, search, and reranking to get top results

RAG APIs

POST /rag/index-document
Generate embeddings and store in vector database

POST /rag/search
Perform semantic search

GET /rag/context/{document_id}
Retrieve document chunks

DELETE /rag/remove-document/{document_id}
Remove document embeddings

Project Structure

project
routes folder
rag folder
uploads folder
main.py
models.py
schemas.py
database.py
auth.py

Installation and Setup

Install dependencies
pip install fastapi uvicorn faiss-cpu sentence-transformers PyPDF2 numpy python-multipart

Run the server
uvicorn main:app --reload

Open Swagger UI
http://127.0.0.1:8000/docs

How to Test

Step 1
Upload a document using /documents/upload

Step 2
Index the document using /rag/index-document with file path and document id

Step 3
Search using /rag/search with query like financial risk

Sample Input

file_path uploads/sample_invoice.pdf
document_id 1

query financial risk due to debt

Sample Output

Company has high financial risk due to debt
Invoice contains total amount and due date
Financial report shows revenue and profit

Key Concepts Used

FastAPI for backend API
FAISS for vector database
Sentence Transformers for embeddings
RAG for semantic search
RBAC for access control

Conclusion

This project demonstrates a complete backend system combining API development, document processing, semantic search using RAG, and role based access control.

Author
Shravani Sable
