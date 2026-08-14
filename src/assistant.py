print("🤖 Hello! I am Nova, your AI Assistant.")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Nova: Hello! How can I help you?")

    elif user.lower() == "bye":
        print("Nova: Goodbye! 👋")
        break

    else:
        print("Nova: I am still learning!")