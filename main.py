import tkinter as tk

# Deze code maakt het venster, import tkinter > tk hiervoor gebruikt
window = tk.Tk()
window.title("Feroci Alpha 0.1")

# Maak functies voor de knoppen TODO: functie toewijzen aan knoppen
#Exit_function heeft wel een functie BTW

def new_game_function():
  print("De knop 'New Game' is ingedrukt!")

def load_game_function():
  print("De knop 'Load Game' is ingedrukt!")

def options_function():
  print("De knop 'Options' is ingedrukt!")

def exit_function():
  window.destroy()

# Maakt daadwerkelijk de knoppen, en de variabelen
new_game_button = tk.Button(text="New Game", command=new_game_function)
load_game_button = tk.Button(text="Load Game", command=load_game_function)
options_button = tk.Button(text="Options", command=options_function)
exit_button = tk.Button(text="Exit", command=exit_function)

# Plaats knoppen in het venster
""""
plaats achter pack in de () de tekst side=tk.BOTTOM of side=tk.TOP om positie aan te passen
"""
new_game_button.pack()
load_game_button.pack()
options_button.pack()
exit_button.pack()

# Stel de grootte van het venster in 400x200 default
window.geometry("400x200")

# Start de GUI
window.mainloop()
