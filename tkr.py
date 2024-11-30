from tkinter import *
window = Tk()
window.title("event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """print the charater associated to the key pressed"""
    print(event.char)
window.bind("<key>",handle_keypress)
def handle_click(event):
    print("n\The Button was clicked!!")

button= Button(text="click me!")
button.pack()    
button.bind("<Button-1",handle_click)
window.mainloop()