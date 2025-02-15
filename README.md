# PDF Grid Line Remover

## 🌟 Description

**PDF Grid Line Remover** is a lightweight Python tool that removes grid lines from PDFs, particularly those created using digital note-taking apps. It detects and erases background lines of predefined colors while keeping handwritten notes or text intact.

## 🚀 Features

- 🌟 Converts PDFs to images for processing
- 🎨 Removes grid lines based on color filtering
- 📂 Automatically saves a cleaned version with `_line_filtered` appended
- 🖱 Simple file picker (no manual file path input needed)
- 📑 Supports multi-page PDFs

## 📦 Installation

Make sure you have Python installed, then install the required dependencies:

```bash
pip install pdf2image opencv-python numpy img2pdf pillow tk
```

## 🛠️ Usage

Run the script and select a PDF file when prompted:

```bash
python remove_grid_lines.py
```

The processed PDF will be saved as:

```
original_filename_line_filtered.pdf
```

## ⚙️ How It Works

1. Opens a **file picker** to select a PDF.
2. Converts the PDF into images using `pdf2image`.
3. Detects and **removes grid lines** using OpenCV.
4. Converts the cleaned images back into a **new PDF**.
5. Saves the result with `_line_filtered.pdf` appended.

## 🖼️ Example

**Input (Original PDF)**  
Contains faint grid lines in the background.

**Output (Processed PDF)**  
The grid lines are removed while keeping the handwriting intact.

## 📝 Supported Colors for Removal

The tool removes lines in these approximate colors (with tolerance):

- `#f5f5f5`
- `#e6e6e6`
- `#ececec`
- `#d6d6d6`

If any additional colors are detected in your file, you can tweak the script to adjust the filtering.

## 🤝 Contributions

Feel free to open issues or contribute improvements via pull requests.

## 📚 License

This project is licensed under the MIT License.
