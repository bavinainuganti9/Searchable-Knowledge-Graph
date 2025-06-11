# Searchable Knowledge Graph

## Overview / Description
GraphIQ is a full-stack application that extracts entities and relationships from unstructured PDFs and websites, builds a Neo4j knowledge graph, and allows users to search and explore connections between people, places, events, and concepts.

## Features
- Upload PDFs and extract named entities using NLP  
- Crawl websites to extract clean text and entities  
- Use spaCy for named entity recognition and relationship extraction  
- Store entities and relations in a Neo4j graph database  
- Search and explore data via semantic queries and Neo4j visualization tools  

## Architecture
Backend: Python FastAPI app with endpoints for PDF upload and URL crawling  
NLP: spaCy for entity extraction; PyMuPDF and BeautifulSoup for document parsing  
Graph DB: Neo4j accessed via official Python driver for storage and querying  
Frontend: React + Tailwind CSS with Neo4j JavaScript driver for graph exploration  

## Tech Stack
Frontend: React, Tailwind CSS, Axios, Neo4j JavaScript Driver  
Backend: Python, FastAPI, spaCy, PyMuPDF, BeautifulSoup  
Graph DB: Neo4j  
