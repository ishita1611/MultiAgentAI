# Multi-Agent AI System

This project is a multi-agent AI system that accepts inputs in PDF, JSON, or Email format, classifies the format and intent, and routes it to the appropriate agent. It maintains shared context for chaining and traceability.

## Features
- Classifies input format and intent
- Routes to Email or JSON agent
- Extracts relevant info and stores it in shared memory
- Supports user input via Streamlit UI (optional)

## Folder Structure
- `agents/` - Agent modules (Classifier, Email, JSON)
- `memory/` - Shared memory implementation
- `samples/` - Sample input files
- `logs/` - Sample output logs and screenshots
- `main.py` - Main orchestration script
- `app.py` - Streamlit UI script (if used)

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Run the main program  
   `python main.py`

3. (Optional) Run the Streamlit UI  
   `streamlit run app.py`

## Sample Inputs
- Email sample in `samples/email_sample.txt`
- JSON sample in `samples/json_sample.json`

## Screenshots
Check `logs/` folder for output screenshots.

