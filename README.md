# 🎯 Real-Time Object Detection using YOLOv8

A deep learning-based object detection application built using **YOLOv8**, **PyTorch**, **OpenCV**, and **Streamlit**. The application allows users to upload images, detect multiple objects in real time, and visualize results with bounding boxes, confidence scores, charts, and downloadable detection reports.

---

## 📌 Project Overview

This project demonstrates the implementation of a real-time object detection system using the pre-trained YOLOv8 model. Users can upload an image through a Streamlit web interface, and the application detects objects, displays annotated results, confidence scores, and interactive visualizations.

---

## ✨ Features

- 📤 Upload images (JPG, JPEG, PNG)
- 🎯 Real-time object detection using YOLOv8
- 🖼️ Display original and detected images
- 📊 Detection summary dashboard
- 📋 Detection table with confidence scores
- 📈 Confidence progress bars
- 🥧 Object distribution pie chart
- 📊 Object count bar chart
- 📄 Detection report
- 📥 Download annotated image
- 💡 Detection insights and tips
- 🎨 Professional Streamlit user interface

---

## 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- Streamlit
- Pandas
- Plotly
- Pillow

---

## 📂 Project Structure

```text
YOLOv8-Object-Detection/
│
├── images/
├── models/
│   └── yolov8n.pt
│
├── notebooks/
│   └── YOLO_EDA.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   ├── detection.png
│   └── charts.png
│
├── app.py
├── detect.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/YOLOv8-Object-Detection.git
```

### Navigate to the project

```bash
cd YOLOv8-Object-Detection
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 🚀 Project Workflow

1. Upload an image.
2. Click **Detect Objects**.
3. YOLOv8 performs object detection.
4. Bounding boxes and labels are displayed.
5. Confidence scores are calculated.
6. Detection statistics are generated.
7. Charts visualize detected objects.
8. Download the annotated image.

---

## 📊 Model Used

**YOLOv8 Nano (YOLOv8n)**

YOLOv8 is one of the fastest and most accurate real-time object detection models developed by Ultralytics. The Nano version provides fast inference while maintaining good accuracy, making it suitable for lightweight applications.

---

## 📸 Screenshots

### 🏠 Home Page

```
Add screenshot: screenshots/home.png
```

### 📤 Upload Image

```
Add screenshot: screenshots/upload.png
```

### 🎯 Detection Result

```
Add screenshot: screenshots/detection.png
```

### 📊 Dashboard

```
Add screenshot: screenshots/charts.png
```

---

## 💼 Applications

- Autonomous Vehicles
- Smart Surveillance
- Retail Analytics
- Traffic Monitoring
- Inventory Management
- Industrial Automation
- Robotics
- Smart Cities

---

## 🔮 Future Improvements

- Webcam object detection
- Video object detection
- Confidence threshold adjustment
- Model selection (YOLOv8n, YOLOv8s, YOLOv8m)
- Export detection report as CSV
- Cloud deployment
- Mobile-friendly interface

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nayab Yaseen Khan**

Artificial Intelligence & Data Science Graduate

GitHub: https://github.com/nayabyaseenkhan

LinkedIn: https://linkedin.com/in/yaseenkhann

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.