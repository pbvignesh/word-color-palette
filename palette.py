import tkinter as tk
import hashlib

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def get_md5_color(word: str):
    """
    Gets the RGB value of a given word's md5 hash

    Args:
        word (str): The word for which the RGB value is to be calculated

    Returns:
        rgb (tuple): The RGB value as a tuple
    """
    byte_encoded_word = word.encode()
    md5_hash = hashlib.md5(byte_encoded_word).hexdigest()

    red = int(md5_hash[:2], 16)
    green = int(md5_hash[2:4], 16)
    blue = int(md5_hash[4:6], 16)

    return (red, green, blue)

def process_file(file):
    """
    Process the text file and read its contents

    Args:
        file (file): The file object

    Returns:
        colors (array): The RGB color array for each word
    """
    try:
        with open(file, "r") as input_file:
            words = input_file.read().split()
        colors = [get_md5_color(word) for word in words]
        return colors
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {e}")

def create_palette(colors):
    """
    Creates a palette image from a given set of colors

    Args:
        colors (array): The array of colors

    Returns:
        image (Image): The palette image
    """
    no_of_colors = len(colors)
    image = Image.new("RGB", (400, 400), "white")
    for i in range(0, 400):
        for j in range(0, 400):
            color_index = ((10 * i) + j) % no_of_colors
            image.putpixel((i, j), colors[color_index])

    return image

def open_file():
    """
    Opens the file and displays the palette image
    """
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file:
        messagebox.showwarning("Invalid File", "Please select a valid .txt file")
        return

    colors = process_file(file)
    print("No of colors: " + str(len(colors)))
    if not colors:
        messagebox.showerror("Error", "No valid data found in the file")
        return

    palette = create_palette(colors)
    palette.show()

# Create the GUI Application Window
root_window = tk.Tk()
root_window.title("Color Palette Generator")
root_window.geometry("600x600")

# Create a button close to the top for the file upload
file_upload_button = tk.Button(root_window, text="Upload File", command=open_file)
file_upload_button.pack(pady=20)

root_window.mainloop()
