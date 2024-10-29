import tkinter as tk
from black_hole import BlackHole  # Import the BlackHole class or other needed functions

def start_simulation():
    # Add code here to call the simulation with user-set parameters
    offset = offset_entry.get()
    # Create BlackHole instance and run simulation with offset
    # Example: black_hole = BlackHole(offset=offset)
    # black_hole.run_simulation()
    print("Simulation started with offset:", offset)

# Set up the main GUI window
root = tk.Tk()
root.title("Black Hole Simulation")

# Offset Entry
tk.Label(root, text="Offset").grid(row=0, column=0)
offset_entry = tk.Entry(root)
offset_entry.grid(row=0, column=1)

# Start Button
start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.grid(row=1, column=0, columnspan=2)

# Run the GUI loop
root.mainloop()
