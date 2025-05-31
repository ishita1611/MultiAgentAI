# agents/email_agent.py

from memory.redis_memory import SharedMemory

class EmailAgent:
    def __init__(self, memory: SharedMemory):
        self.memory = memory

    def process(self, email_text: str):
        # Super basic NLP vibes for demo
        sender = self.extract_sender(email_text)
        intent = self.extract_intent(email_text)
        urgency = self.extract_urgency(email_text)

        # Store in memory
        self.memory.log("email_data", {
            "sender": sender,
            "intent": intent,
            "urgency": urgency,
            "format": "Email"
        })

        return {
            "sender": sender,
            "intent": intent,
            "urgency": urgency
        }

    def extract_sender(self, text: str):
        if "From:" in text:
            return text.split("From:")[1].split("\n")[0].strip()
        return "Unknown Sender"

    def extract_intent(self, text: str):
        if "quote" in text.lower():
            return "RFQ"
        elif "complaint" in text.lower():
            return "Complaint"
        elif "invoice" in text.lower():
            return "Invoice"
        else:
            return "General Inquiry"

    def extract_urgency(self, text: str):
        return "High" if "urgent" in text.lower() else "Normal"
