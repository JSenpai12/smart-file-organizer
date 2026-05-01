# Smart File Organizer 📁

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A lightweight Python automation tool that organizes files inside a user-defined directory (such as the Downloads folder) into categorized folders based on file type.

This project helps reduce digital clutter and improves file management efficiency through automation.

---

## 🚀 Features

- 📂 User-defined target directory (e.g., Downloads folder)
- 🤖 Automatic file detection and categorization
- 🖼️ Supports images, documents, audio, videos, archives, and more
- ⚡ Fast and lightweight execution
- 🧠 Simple and beginner-friendly Python logic
- 🧹 Clean folder organization with minimal setup

---

## 🛠️ Technologies Used

- Python 3
- `os` module (file system navigation)
- `shutil` module (file operations)

---

## ⚙️ How It Works

1. The user inputs the path of the **Downloads folder (or any directory)**
2. The program scans all files inside the directory
3. It identifies each file type based on extension
4. Files are grouped into predefined categories
5. Each file is moved into its corresponding folder automatically

### Example Output

```

Before:

Downloads/
├── image.jpg
├── report.pdf
├── song.mp3

After:

Images/
├── image.jpg/
Documents/
├── report.pdf/
Audio/
├── song.mp3/


```

👉 The user provides the Downloads path, and the system automatically sorts everything into structured folders.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/JSenpai12/smart-file-organizer.git
