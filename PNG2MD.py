import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import webp

# Function to convert PNG to WebP
def convert_png_to_webp(png_file):
    try:
        webp_file = os.path.splitext(png_file)[0] + '.webp'
        image = Image.open(png_file)
        image.save(webp_file, 'webp', quality=20, method=6)
        return webp_file
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert {png_file} to WebP: {e}")
        return None

# Function to encode WebP to Base64 and save as .md file
def encode_webp_to_base64(webp_file):
    if webp_file:
        with open(webp_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        markdown_string = f"Paste and cut image below\n\n![image](data:image/webp;base64,{encoded_string})"
        output_file_path = f"{os.path.splitext(webp_file)[0]}.md"
        with open(output_file_path, "w") as output_file:
            output_file.write(markdown_string)
        messagebox.showinfo("Success", f"Markdown file with Base64 encoded image saved to {output_file_path}")
    else:
        messagebox.showerror("Error", "WebP file not found for Base64 encoding.")

# Function to open file dialog and process PNG file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        webp_file = convert_png_to_webp(file_path)
        encode_webp_to_base64(webp_file)

# Create the GUI window
root = tk.Tk()
root.title("PNG to WebP and Base64 Converter")

# Create and place the button to select file
select_button = tk.Button(root, text="Select PNG File", command=select_file)
select_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
