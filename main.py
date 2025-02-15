import os
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from PIL import Image
import img2pdf

# Define the colors to remove and a tolerance for slight variations
target_colors = [
    (245, 245, 245),  # #f5f5f5
    (230, 230, 230),  # #e6e6e6
    (236, 236, 236),  # #ececec
    (214, 214, 214)   # #d6d6d6
]

tolerance = 15  # Adjust this to remove slightly different shades

def remove_lines(image):
    """ Removes grid lines by detecting and replacing target colors """
    img_array = np.array(image)

    # Create a mask where pixels are close to target colors
    mask = np.zeros(img_array.shape[:2], dtype=np.uint8)

    for color in target_colors:
        lower_bound = np.array([max(0, c - tolerance) for c in color], dtype=np.uint8)
        upper_bound = np.array([min(255, c + tolerance) for c in color], dtype=np.uint8)

        color_mask = cv2.inRange(img_array, lower_bound, upper_bound)
        mask = cv2.bitwise_or(mask, color_mask)

    # Replace detected pixels with white (or transparent if needed)
    img_array[mask == 255] = [255, 255, 255]  # Replace with white

    return Image.fromarray(img_array)

def process_pdf(input_pdf):
    """ Converts PDF to images, removes grid lines, and saves back to PDF """
    output_pdf = os.path.splitext(input_pdf)[0] + "_line_filtered.pdf"
    
    try:
        print("Processing PDF, please wait...")
        images = convert_from_path(input_pdf, dpi=300)  # Convert PDF pages to images
        cleaned_images = [remove_lines(img) for img in images]  # Process each page

        # Save cleaned images back to a PDF
        cleaned_images[0].save(output_pdf, save_all=True, append_images=cleaned_images[1:], resolution=300)

        print(f"Processed PDF saved as: {output_pdf}")
        messagebox.showinfo("Success", f"Processed PDF saved as:\n{output_pdf}")
    except Exception as e:
        print("Error processing PDF:", str(e))
        messagebox.showerror("Error", str(e))

# Open file picker to select a PDF file
root = tk.Tk()
root.withdraw()  # Hide the root window

input_pdf = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

if input_pdf:
    process_pdf(input_pdf)
else:
    print("No file selected.")
