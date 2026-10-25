# 🌿 Plant Disease Recognition System

An AI-powered computer vision system capable of identifying **38 different classes** of plant leaf diseases using Convolutional Neural Networks (CNN) and providing an interactive web dashboard built with **Streamlit**.

---

## 🚀 Features

- **High Accuracy Detection:** Trained on over 87,000 augmented leaf images from the New Plant Diseases (PlantVillage) dataset.
- **38 Classes Supported:** Covers healthy and diseased conditions for Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato.
- **⚡ 1-Click Setup & Launch:** Windows batch scripts (`run.bat` and `setup.bat`) automatically configure Python dependencies, download pre-trained model weights, and launch the dashboard.
- **Interactive Web Interface:** Upload any plant leaf image to instantly preview and receive prediction results with confidence percentages.
- **Sample Test Images Included:** Comes with pre-bundled sample leaf images in `sample_test_images/` for instant testing.

---

## 📂 Project Structure

```text
├── main.py                             # Streamlit dashboard application
├── download_model.py                   # Automatic model weight downloader (~90MB)
├── run.bat                             # 1-Click setup & launch script for Windows
├── setup.bat                           # 1-Click dependency setup script
├── requirements.txt                    # Project dependencies
├── home_page.jpeg                      # Cover banner for the dashboard
├── Train_plant_disease.ipynb           # Model training notebook (CNN architecture & training)
├── Test_plant_disease.ipynb            # Model evaluation & confusion matrix notebook
├── training_hist.json                  # Saved training loss/accuracy metrics (10 epochs)
├── sample_test_images/                 # Real test leaf images for quick testing
│   ├── Apple_Cedar_apple_rust.JPG
│   ├── Apple_healthy.JPG
│   ├── Corn_Common_rust.JPG
│   └── Tomato_Early_blight.JPG
├── .gitignore                          # Git ignore configuration
└── README.md                           # Documentation
```

---

## ⚡ 1-Click Setup & Run (Windows)

Simply **double-click** `run.bat` in File Explorer, or open your terminal and run:

```cmd
run.bat
```

What `run.bat` does automatically:
1. Verifies your Python installation.
2. Installs all required packages from `requirements.txt`.
3. Verifies and downloads `trained_plant_disease_model.keras` (~90 MB) if missing.
4. Starts the Streamlit server and opens `http://localhost:8501` in your default browser.

---

## 🛠️ Manual Installation

If you prefer setting up manually using a Python virtual environment:

### 1. Clone your repository:
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Download pre-trained model weights:
```bash
python download_model.py
```

### 5. Launch the Streamlit application:
```bash
streamlit run main.py
```

---

## 🧠 Model Architecture & Training

The model uses a 5-stage Convolutional Neural Network (CNN):
- **Input:** $128 \times 128 \times 3$ RGB leaf images
- **Feature Extraction:** 5 Convolutional blocks (each with 2x Conv2D + ReLU + MaxPooling2D) with filter counts: 32 → 64 → 128 → 256 → 512
- **Regularization:** Dropout (0.25 and 0.40) to mitigate overfitting
- **Classification:** Flatten → Dense (1500 units, ReLU) → Dense (38 units, Softmax)
- **Dataset:** [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---

## 📤 Pushing to Your GitHub Repository

To push this project to your own GitHub account:

### Step 1: Create a new repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g., `plant-disease-prediction`).
3. Leave "Initialize with README" **unchecked** (since this project already includes one).
4. Click **Create repository**.

### Step 2: Initialize Git and Push

Open a terminal or command prompt in this project folder and run:

```cmd
git init
git add .
git commit -m "Initial commit: Plant Disease Recognition System with 1-click launcher"
git branch -M main
git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/<YOUR-REPO-NAME>.git
git push -u origin main
```

> [!TIP]
> By default, `.gitignore` excludes the 90 MB binary model weights file (`trained_plant_disease_model.keras`) because `run.bat` and `download_model.py` automatically download it upon running. If you want to commit the model directly to GitHub, simply comment out the `trained_plant_disease_model.keras` line in `.gitignore`.

---

## 📄 License
This project is for educational and research purposes.
