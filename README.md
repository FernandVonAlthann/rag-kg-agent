# rag-kg-agent

Overview

This project demonstrates a combined system featuring:

Retrieval-Augmented Generation (RAG) pipelines
Knowledge Graph (KG) support (mocked for now)
Agentic memory with planning and execution


# Installation & Setup

1. Clone or download the repository and navigate to its directory:
cd /path/to/rag-kg-agent
2. Create and activate a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
On Windows PowerShell, activate with:
```
.\venv\Scripts\Activate.ps1
```
3. Upgrade pip and install dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```

# Running the Project

Once dependencies are installed and the virtual environment is activated, run:
```
python main.py
```
You should see output indicating the retrieval pipeline, mock knowledge graph results, and agent loop execution.

# Notes

The knowledge graph is currently mocked; you can integrate a real Neo4j instance later if desired.
Dummy documents are embedded and stored in-memory for retrieval demonstration.
You can expand the project by adding real documents or integrating an actual KG.


# Troubleshooting

If pip command is not found, ensure you are using pip3 or install Python 3 from https://python.org.
To exit the virtual environment, run:
```
deactivate
```
