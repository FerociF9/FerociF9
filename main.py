import tkinter as tk

# Maak een venster
window = tk.Tk()
window.title("GUI met knoppen")

# Maak functies voor de knoppen
def new_game_function():
  print("De knop 'New Game' is ingedrukt!")

def load_game_function():
  print("De knop 'Load Game' is ingedrukt!")

def options_function():
  print("De knop 'Options' is ingedrukt!")

# Maak knoppen
new_game_button = tk.Button(text="New Game", command=new_game_function)
load_game_button = tk.Button(text="Load Game", command=load_game_function)
options_button = tk.Button(text="Options", command=options_function)

# Plaats knoppen in het venster
new_game_button.pack(side=tk.BOTTOM)
load_game_button.pack(side=tk.BOTTOM)
options_button.pack(side=tk.BOTTOM)

# Stel de grootte van het venster in
window.geometry("400x200")

# Start de GUI
window.mainloop()
