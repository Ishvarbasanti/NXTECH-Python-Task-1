
import pyautogui
import tkinter as tk
from tkinter.filedialog import asksaveasfile

root = tk.Tk()
root.title("Take Screenshot")
root.geometry("300x300")

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def takeScreenshot():

    # Take the screenshot
    myscreenshot = pyautogui.screenshot()

    # Select a path location and file prompt
    save_path = asksaveasfile(defaultextension='.png')

    # Save the screenshot if a valid saved path location is selected
    if save_path:
        myscreenshot.save(save_path.name)

        # Create a button to trigger to capture the screenshot
myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)
canvas1.create_window(150, 150, window=myButton)

# Start the GUI event loop
root.mainloop()