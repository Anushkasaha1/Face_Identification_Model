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

#TASK-B

Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
^C


Using device: cuda


/usr/local/lib/python3.11/dist-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.


  warnings.warn(
/usr/local/lib/python3.11/dist-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=ResNet18_Weights.IMAGENET1K_V1`. You can also use `weights=ResNet18_Weights.DEFAULT` to get the most up-to-date weights.
  warnings.warn(msg)

  
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth


100%|██████████| 44.7M/44.7M [00:00<00:00, 180MB/s]

🔁 Epoch 1/20
Training: 100%|██████████| 587/587 [02:23<00:00,  4.10it/s]

🔁 Epoch 2/20
Training: 100%|██████████| 587/587 [02:18<00:00,  4.25it/s]

🔁 Epoch 3/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.26it/s]

🔁 Epoch 4/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.28it/s]

🔁 Epoch 5/20
Training: 100%|██████████| 587/587 [02:18<00:00,  4.25it/s]

🔁 Epoch 6/20
Training: 100%|██████████| 587/587 [02:15<00:00,  4.34it/s]

🔁 Epoch 7/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.28it/s]

🔁 Epoch 8/20
Training: 100%|██████████| 587/587 [02:16<00:00,  4.29it/s]

🔁 Epoch 9/20
Training: 100%|██████████| 587/587 [02:15<00:00,  4.33it/s]

🔁 Epoch 10/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.28it/s]

🔁 Epoch 11/20
Training: 100%|██████████| 587/587 [02:15<00:00,  4.35it/s]

🔁 Epoch 12/20
Training: 100%|██████████| 587/587 [02:16<00:00,  4.29it/s]

🔁 Epoch 13/20
Training: 100%|██████████| 587/587 [02:16<00:00,  4.29it/s]

🔁 Epoch 14/20
Training: 100%|██████████| 587/587 [02:14<00:00,  4.36it/s]

🔁 Epoch 15/20
Training: 100%|██████████| 587/587 [02:16<00:00,  4.31it/s]

🔁 Epoch 16/20
Training: 100%|██████████| 587/587 [02:15<00:00,  4.34it/s]

🔁 Epoch 17/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.28it/s]

🔁 Epoch 18/20
Training: 100%|██████████| 587/587 [02:17<00:00,  4.27it/s]

🔁 Epoch 19/20
Training: 100%|██████████| 587/587 [02:14<00:00,  4.35it/s]

🔁 Epoch 20/20
Training: 100%|██████████| 587/587 [02:15<00:00,  4.33it/s]

✅ Validation Accuracy: 100.00%
✅ Model saved as face_identification_model.pth
Model saved successfully


---

**This project demonstrates the effectiveness of deep learning for personalized face recognition and provides a solid foundation for further development and experimentation.**

