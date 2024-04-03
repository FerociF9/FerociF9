import tkinter as tk

# Maakt een venster
window = tk.Tk()
window.title("Feroci Beta Software")

# Maak een functie voor de knop "Launch"
def launch_function():
  print("De knop 'Launch' is ingedrukt!")

# Maak een functie voor de knop "Exit"
def exit_function():
  window.destroy()

# Maak een knop "Launch"
launch_button = tk.Button(text="Launch", command=launch_function)
launch_button.pack()

# Maak een knop "Exit"
exit_button = tk.Button(text="Exit", command=exit_function)
exit_button.pack()

# Start de GUI
window.mainloop()
