from agents.email_agent import EmailAgent
from memory.redis_memory import SharedMemory

if __name__ == "__main__":
    memory = SharedMemory()
    agent = EmailAgent(memory)

    email_content = """
    From: riya@client.com
    Subject: Urgent Quote Required

    Hi team, we urgently need a quote for 500 units.
    Please respond ASAP.
    """

    result = agent.process(email_content)
    print("📧 EMAIL AGENT SAYS:", result)
