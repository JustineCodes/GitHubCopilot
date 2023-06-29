
import tkinter as tk

# Create an instance of Tkinter window
window = tk.Tk()

# Set window title
window.title("My First Tkinter Window")

# Set window dimensions
window.geometry("400x300")

# Create a label for the input box
input_label = tk.Label(window, text="Enter your name:")
input_label.pack()

# Create the input box
input_box = tk.Entry(window)
input_box.pack()

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=lambda: display_results(input_box.get()))
submit_button.pack()

# Create a label to display the results
results_label = tk.Label(window, text="")
results_label.pack()

# Define a function to display the results
def display_results(input_text):
    results_label.config(text=input_text)
    input_box.delete(0, tk.END)

# Run the event loop
window.mainloop()
