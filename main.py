import json
from agents.classifier_agent import ClassifierAgent
from memory.redis_memory import SharedMemory

def main():
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)

    # Get user input for Email or JSON
    choice = input("Choose input type (email/json): ").strip().lower()

    if choice == "email":
        user_input = input("Paste your email content:\n")
    elif choice == "json":
        user_input = input("Paste your JSON data:\n")
        try:
            user_input = json.loads(user_input)
        except json.JSONDecodeError:
            print("Oops! That JSON is invalid. Fix it and try again.")
            return
    else:
        print("Invalid choice, queen! Choose 'email' or 'json'.")
        return

    fmt, intent, result = classifier.process(user_input, source_id="user-input")
    print(f"\nFormat: {fmt}\nIntent: {intent}\nAgent Output: {result}")

if __name__ == "__main__":
    main()
