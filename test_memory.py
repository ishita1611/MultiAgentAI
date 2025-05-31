from memory.redis_memory import SharedMemory

mem = SharedMemory()

# Save some info
mem.log("queen-i", {
    "sender": "Ishita",
    "intent": "Complaint",
    "format": "Email"
})

# Fetch it
data = mem.get("queen-i")
print("MEMORY SAYS:", data)
