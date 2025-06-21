import tkinter as tk
import random

quotes = {
    "Happy": ["Smile, it's free therapy!", "Keep shining!", "Happiness looks good on you!"],
    "Sad": ["It's okay to feel down.", "You're stronger than you think.", "Better days are coming."],
    "Angry": ["Take a deep breath.", "Choose peace.", "Don’t let anger control you."],
    "Lazy": ["Even small steps matter.", "You can rest, but don’t quit.", "Progress over perfection."],
    "Motivated": ["Believe in yourself!", "Push your limits!", "You are capable of amazing things!"]
}

def show_quote(mood):
    quote = random.choice(quotes[mood])
    result_label.config(text=f"Here's a quote for you:\n{quote}")
    with open("your_mood_quote.txt", "w") as f:
        f.write(f"Your mood: {mood}\nQuote: {quote}")

root = tk.Tk()
root.title("Mood-Based Quote Generator")
root.geometry("400x350")

heading = tk.Label(root, text="Select Your Mood", font=("Arial", 16, "bold"))
heading.pack(pady=10)

for mood in quotes:
    btn = tk.Button(root, text=mood, width=20, font=("Arial", 12), command=lambda m=mood: show_quote(m))
    btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, pady=20)
result_label.pack()

root.mainloop()