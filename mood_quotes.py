import random

# Welcome message
print("Welcome to the Mood-Based Quote Generator!")
print("Select your mood:")
print("1. Happy")
print("2. Sad")
print("3. Angry")
print("4. Lazy")
print("5. Motivated")

# Ask user for input
choice = input("Enter the number of your mood: ")

# Dictionary of quotes
quotes = {
    "1": ["Smile, it's free therapy!", "Keep shining!", "Happiness looks good on you!"],
    "2": ["It's okay to feel down.", "You're stronger than you think.", "Better days are coming."],
    "3": ["Take a deep breath.", "Choose peace.", "Don’t let anger control you."],
    "4": ["Even small steps matter.", "You can rest, but don’t quit.", "Progress over perfection."],
    "5": ["Believe in yourself!", "Push your limits!", "You are capable of amazing things!"]
}

# Show quote
if choice in quotes:
    print("\nHere's a quote for you:")
    print(random.choice(quotes[choice]))
else:
    print("Invalid choice. Please enter a number between 1 and 5.")