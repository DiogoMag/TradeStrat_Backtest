import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("600x600")

# Create the labels
asset_label = tk.Label(window, text="Asset", font=("Arial", 16))
position_label = tk.Label(window, text="Position", font=("Arial", 16))
entry_amount_label = tk.Label(window, text="Entry Amount", font=("Arial", 16))
entry_price_label = tk.Label(window, text="Entry Price", font=("Arial", 16))

# Create the input boxes
asset_entry = tk.Entry(window, font=("Arial", 16))
position_entry = tk.Entry(window, font=("Arial", 16))
entry_amount_entry = tk.Entry(window, font=("Arial", 16))
entry_price_entry = tk.Entry(window, font=("Arial", 16))

# Pack the labels and input boxes horizontally
asset_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
asset_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
position_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
position_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
entry_amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")
entry_price_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_price_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Define the function to print the user inputs as a dictionary
def print_user_inputs():
    user_inputs = {
        "Asset": asset_entry.get(),
        "Position": position_entry.get(),
        "Entry Amount": float(entry_amount_entry.get()),
        "Entry Price": float(entry_price_entry.get())
    }
    print(user_inputs)

# Create the submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 16), command=print_user_inputs)

# Place the submit button at the bottom of the window using grid()
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Define the function to close the window
def close_window():
    window.destroy()

# Create the exit button
exit_button = tk.Button(window, text="Exit", font=("Arial", 16), command=close_window)

# Place the exit button below the submit button using grid()
exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()
