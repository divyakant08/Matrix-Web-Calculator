
# 🚀 Matrix Solver (Flask & NumPy Web Application)

A lightweight, responsive web-based linear algebra calculator built using **Python (Flask)** and **NumPy**. This application provides an intuitive graphical interface for performing core matrix operations instantly through any web browser.

---

## ✨ Features

- **Interactive Grid:** Dynamically adjustable rows and columns for matrix configuration.
- **Core Operations:** Supports Transpose, Determinant, Inverse, Rank, and Trace.
- **Robust Error Handling:** Handles empty fields, non-numeric entries, singular matrix inversions, and dimension mismatches.
- **Modern UI/UX:** Clean, minimalist styling with a responsive layout.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, NumPy
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **Development Tool:** Visual Studio Code

---

## 📂 Project Structure

```text
Matrix Solver/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── app.py
```

---

## ⚙️ Installation & Quick Start

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/divyakant08/flask-numpy-matrix-calculator.git
cd Matrix-Solver
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install Flask numpy
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

Visit the following URL:

```text
http://127.0.0.1:5000/
```

---

## 💡 Usage

1. Enter the desired number of **Rows** and **Columns** (up to 5 × 5).
2. Select a **Linear Algebra Operation** from the dropdown menu.
3. Enter numerical values into the matrix grid.
4. Click **Compute Result** to view the output instantly.

---

## 👨‍💻 Author

**Divyakant**

GitHub: [@divyakant08](https://github.com/divyakant08)
