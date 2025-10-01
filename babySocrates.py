import random

questions = [
    "What do you mean by that?",
    "What do you think of that?",
    "Can you give an example?",
    "What would the opposite look like?",
]

print("Welcome to the Socratic LLM! Type 'quit' to end the conversation.")

while True:
    answer = input("You: ")
    if answer.lower() == "quit":
        break
    print("Socrates: " + random.choice(questions))