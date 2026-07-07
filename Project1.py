responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Nice to meet you.",
    "hey": "Hey! How are you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm a Rule-Based AI Chatbot.",
    "who created you": "I was created using Python.",
    "help": "You can greet me or ask simple questions.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a great day!",
    "exit": "Exiting chatbot...",
    "quit": "Exiting chatbot..."
}

print("Rule-Based AI Chatbot")
print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot:", responses.get(user_input))
        break

    response = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", response)