import tkinter as tk
from tkinter import messagebox
import random

def generate_random_content():
    # Generate a random word
    random_word = get_random_word()

    # Create the message
    message = f"{random_word}? I hardly know her?!"

    return message

def get_random_word():
    # Replace this list with your own set of words
    words = ["apple", "banana", "carrot", "dog", "elephant", "flower", "guitar", "happiness", "island", "jazz", "kangaroo", "laughter", "mountain", "notebook", "ocean", "penguin", "quasar", "rainbow", "sunset", "tiger", "umbrella", "violin", "whisper", "xylophone", "yoga",  "runner", "baker", "dancer", "writer", "singer", "driver", "jogger", "gardener", "swimmer", "engineer", "painter", "biker", "designer", "photographer", "explorer", "farmer", "programmer", "hiker", "sculptor", "builder", "doctor", "waiter", "officer", "traveler", "manager", "hustler"]

    # Choose a random word from the list
    return random.choice(words)

def show_random_content():
    content = generate_random_content()
    messagebox.showinfo("Random Content", content)

# Create the main window
app = tk.Tk()
app.title("Random Word Generator")

# Create and pack a button
button = tk.Button(app, text="Generate Random Content", command=show_random_content)
button.pack(padx=20, pady=20)

# Run the application
app.mainloop()
