import os
import json
from memory.redis_memory import SharedMemory
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.email_agent = EmailAgent(self.memory)
        self.json_agent = JSONAgent(self.memory)

    def classify_format(self, data):
        if isinstance(data, dict):
            return "JSON"
        elif isinstance(data, str) and "Subject:" in data:
            return "Email"
        elif isinstance(data, bytes):
            return "PDF"
        return "Unknown"

    def detect_intent(self, content):
        keywords = {
            "invoice": "Invoice",
            "quote": "RFQ",
            "complaint": "Complaint",
            "regulation": "Regulation"
        }
        content_lower = str(content).lower()
        for word, intent in keywords.items():
            if word in content_lower:
                return intent
        return "Unknown"

    def process(self, content, source_id="input-001"):
        fmt = self.classify_format(content)
        intent = self.detect_intent(content)

        print(f"🧠 Detected Format: {fmt}, Intent: {intent}")

        self.memory.log(source_id, {
            "format": fmt,
            "intent": intent,
            "content_preview": str(content)[:100]
        })

        if fmt == "Email":
            print(f"Routing to EmailAgent...")
            agent_result = self.email_agent.process(content)
        elif fmt == "JSON":
            print(f"Routing to JSONAgent...")
            agent_result = self.json_agent.process(content)
        else:
            print(f"No agent available for format: {fmt}")
            agent_result = None

        return fmt, intent, agent_result
