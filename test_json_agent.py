from agents.json_agent import JSONAgent
from memory.redis_memory import SharedMemory

# Setup
memory = SharedMemory()
agent = JSONAgent(memory)

# Sample input JSON dict
sample_json = {
    "id": "INV123",
    "date": "2025-05-30",
    "customer": "Queen I Co.",
    "items": [
        {"product": "AI Model", "qty": 2, "price": 1500},
        {"product": "Data Set", "qty": 1, "price": 800}
    ],
    "total_amount": 3800
}

result = agent.process(sample_json)
print("Result:", result)
