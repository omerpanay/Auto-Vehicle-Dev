# Autonom Car Dev

This repository provides a modular, deep learning-based perception system for autonomous vehicles. It includes solutions for lane detection, road segmentation, person and car detection, traffic sign recognition, and traffic light detection. Each module is self-contained and can be used independently or as part of the integrated pipeline.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Model and Video Files](#model-and-video-files)
- [Dataset](#dataset)
- [Results and Metrics](#results-and-metrics)
- [Project Report](#project-report)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
This project aims to provide a comprehensive perception stack for autonomous driving, leveraging state-of-the-art deep learning models for:
- **Lane Detection**
- **Road Segmentation**
- **Person and Car Detection**
- **Traffic Sign Recognition**
- **Traffic Light Detection**

The system is designed for both real-time and offline (video-based) analysis. Each module can be trained, evaluated, and used independently, or combined using the main execution script.

---

## Folder Structure
```
Autonom-Car-Dev/
│
├── execute models/
│   ├── main.py
│   ├── lane_segmentation.pt
│   ├── person_and_car_detection.pt
│   ├── road_segmentation.pt
│   ├── traffic_sign.pt
│   ├── traffic_light.pt
│   ├── output_processed.mp4
│   └── utils/
│
├── Lane Det/
│   ├── Lane Segmentation.ipynb
│   ├── train_batches.png
│   ├── F1_Confidence_Curve.png
│   ├── confusion_matrix_normalized.png
│   └── result.png
│
├── Person and Car Detection/
│   ├── detect.py
│   └── coco_classes.txt
│
├── Road Segmentation/
│   ├── Road Segmentation.ipynb
│   ├── train_batches.png
│   ├── PR_Curve.png
│   ├── conf_matrix_norm.png
│   └── results.png
│
├── Traffic Sign/
│   ├── Traffic Sign Detection.ipynb
│   ├── train_batches.png
│   ├── PR_and_F1_Curve.png
│   ├── conf_matrix_norm.png
│   └── results.png
│
├── Traffic Light/
│   ├── Traffic Light Detection.ipynb
│   ├── train_batches.png
│   ├── PR_and_F1_Curve.png
│   ├── conf_matrix_norm.png
│   └── results.png
│
├── Representation.pdf
└── README.md
```

---

## Installation

1. **Python**
   - Requires Python 3.7 or higher.

2. **Dependencies**
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```
   - If `requirements.txt` is not available, main dependencies include:
     - torch
     - torchvision
     - opencv-python
     - numpy
     - matplotlib
     - (and others as used in the notebooks)

---

## Usage

### 1. Download Model Files
Model files (`.pt`) are not included in this repository due to their size. Download them from [MODEL_LINK] and place them in the `execute models/` directory:
- lane_segmentation.pt
- person_and_car_detection.pt
- road_segmentation.pt
- traffic_sign.pt
- traffic_light.pt

### 2. (Optional) Download Output Video
The processed output video (`output_processed.mp4`) is also not included due to GitHub's file size limits. Download it from [VIDEO_LINK] and place it in the `execute models/` directory.

### 3. Run the Main Pipeline
To run the integrated perception pipeline:
```bash
python "execute models/main.py"
```

### 4. Run Individual Modules
Each module has its own Jupyter notebook for training, evaluation, and visualization:
- **Lane Detection:** `Lane Det/Lane Segmentation.ipynb`
- **Road Segmentation:** `Road Segmentation/Road Segmentation.ipynb`
- **Traffic Sign Recognition:** `Traffic Sign/Traffic Sign Detection.ipynb`
- **Traffic Light Detection:** `Traffic Light/Traffic Light Detection.ipynb`
- **Person and Car Detection:** `Person and Car Detection/detect.py`

---

## Modules

### Lane Detection
- Deep learning-based lane segmentation.
- Training and evaluation in the notebook.

**Results:**

![Lane Detection Result](Lane%20Det/result.png)
*output of lane segmentation.*

![Lane Detection Confusion Matrix](Lane%20Det/confusion_matrix_normalized.png)
*Normalized confusion matrix for lane segmentation model.*

---

### Road Segmentation
- Semantic segmentation of drivable road area.
- Training, evaluation, and metrics in the notebook.

**Results:**

![Road Segmentation Result](Road%20Segmentation/results.png)
*output of road segmentation.*

![Road Segmentation Confusion Matrix](Road%20Segmentation/conf_matrix_norm.png)
*Normalized confusion matrix for road segmentation model.*

![Road Segmentation PR Curve](Road%20Segmentation/PR_Curve.png)
*Precision-Recall curve for road segmentation.*

---

### Person and Car Detection
- Object detection using pre-trained models (e.g., YOLO).
- `detect.py` for inference; `coco_classes.txt` for class labels.

---

### Traffic Sign Recognition
- Detection and classification of traffic signs.
- Notebook includes training, evaluation, and visualization.

**Results:**

![Traffic Sign Detection Result](Traffic%20Sign/results.png)
*output of traffic sign detection.*

![Traffic Sign Confusion Matrix](Traffic%20Sign/conf_matrix_norm.png)
*Normalized confusion matrix for traffic sign detection.*

![Traffic Sign PR and F1 Curve](Traffic%20Sign/PR_and_F1_Curve.png)
*Precision-Recall and F1 Score curves for traffic sign detection.*

---

### Traffic Light Detection
- Detection and state classification (red/yellow/green) of traffic lights.
- Notebook includes all steps and result images.

**Results:**

![Traffic Light Detection Result](Traffic%20Light/results.png)
*output of traffic light detection.*

![Traffic Light Confusion Matrix](Traffic%20Light/conf_matrix_norm.png)
*Normalized confusion matrix for traffic light detection.*

![Traffic Light PR and F1 Curve](Traffic%20Light/PR_and_F1_Curve.png)
*Precision-Recall and F1 Score curves for traffic light detection.*

---

## Model and Video Files
- **Model Files (.pt):** Not included in the repository. Download from [https://drive.google.com/drive/folders/1WnN1khMFUZvGs2huXPGwB-RgITNsT6x8?usp=sharing].
- **Output Video:** Not included due to size. Download from [https://drive.google.com/file/d/1kjLw8CYi9w-BCvs8nGK25XrdhimGQwLF/view?usp=sharing].



## Dataset
- **Note:** The dataset used in this project could not be uploaded to GitHub due to its large size. However, it was previously shared via email.

---

## Results and Metrics
Each module directory contains:
- **Result Images:** Visualizations of predictions and outputs.
- **Metric Plots:** Curves and matrices (e.g., F1, PR, confusion matrix) for model evaluation.

---

## Project Report
- **Representation.pdf:** Contains a detailed project report, methodology, and results summary. Recommended for an in-depth understanding of the project.

---

## Contributing
1. Fork the repository and create a new branch.
2. Make your changes.
3. Submit a pull request.

---

## License
MIT License

