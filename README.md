# Face Identification Using ResNet18

This project presents a robust deep learning pipeline for **face identification**, capable of classifying facial images into specific individual identities. Built on top of a pre-trained ResNet18 architecture and trained with custom data, the model excels at distinguishing subtle facial features unique to each person.

# Model Weight

Model weight (.pth file) are stored on google drive due to file size limits.

## Download Model Weights here

https://drive.google.com/file/d/1mwe6DG6YM7J8VV5nGg9xYWgWwP71TeMJ/view?usp=sharing

---

## 🚀 Overview

- **Framework:** PyTorch
- **Backbone:** ResNet18 (pre-trained on ImageNet)
- **Task:** Multi-class face identification
- **Environment:** Google Colab

The pipeline leverages transfer learning to efficiently recognize individual identities, utilizing datasets organized in folder structures where each folder represents a separate person.

---

## ⚙️ How It Works

### 🗂️ Data Loading

- Automatically scans `train` and `val` directories.
- Maps each identity folder to a unique numeric label.

---

### 🖼️ Preprocessing

- Resizes all images to **224 × 224 pixels.**
- Normalizes pixel values using ImageNet mean and standard deviation.
- Includes optional data augmentation for improved generalization.

---

### 🧠 Model Architecture

- Adopts a ResNet18 backbone for feature extraction.
- Replaces the final fully connected layer to match the number of identities in the dataset.

---

### 🎯 Training Process

- **Loss Function:** Cross-Entropy Loss
- **Optimizer:** Adam
- Supports fine-tuning of deeper ResNet layers for enhanced feature discrimination.

---

### ✅ Validation

- Evaluates model performance on unseen validation images.
- Calculates accuracy metrics to monitor learning progress.
- Accuracy = 100 %

---

## 💡 Key Insights

- Face identification demands **fine-grained feature recognition** far beyond basic image classification tasks.
- Freezing all ResNet18 layers may suffice for broader tasks (like gender classification), but is typically **inadequate for identity recognition.**
- Fine-tuning deeper layers significantly boosts the model’s ability to distinguish subtle identity-specific features.

---

## 📈 Recommended Improvements

- Incorporate face detection before identification to isolate facial regions.
- Experiment with deeper architectures (e.g., ResNet50) for potentially higher accuracy.
- Apply advanced augmentation techniques for greater robustness against variations.
- Explore deployment options (APIs, web applications) for real-world integration.

---

**This project demonstrates the effectiveness of deep learning for personalized face recognition and provides a solid foundation for further development and experimentation.**

