# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y1I3OHnIAQi9D0JDK6LrhTgivBjp8E_a
"""

from google.colab import drive
drive.mount('/content/drive')


!unzip -oq "/content/drive/MyDrive/faceRecognitionp_project/Comys_Hackathon5.zip" -d /content/

!cp -r "/content/drive/MyDrive/faceRecognitionp_project/Comys_Hackathon5/Task_B" /content/

from torchvision import models
import torch
import os
import torch.nn as nn
from torchvision import transforms
from PIL import Image
print(os.listdir("/content"))
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
    transforms.RandomHorizontalFlip()
])
train_dir = "/content/Comys_Hackathon5/Task_B/train"
val_dir = "/content/Comys_Hackathon5/Task_B/val"


all_paths = set(os.listdir(train_dir)) | set(os.listdir(val_dir))
all_paths = sorted(list(all_paths))     # consistent ordering
label_to_index = {label: idx for idx, label in enumerate(all_paths)}
index_to_label = {idx: label for label, idx in label_to_index.items()}


img=Image.open('img.jpg')
img=Image.open('img.jpg').convert('RGB')
img=transform(img)
img = img.unsqueeze(0).to(device)

model=models.resnet18(weights=None)
for name, param in model.named_parameters():
    if "layer4" not in name:
        param.requires_grad = False


n_classes = len(label_to_index)
model.fc = nn.Sequential(
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(512, n_classes)
)
pro_path="/content/face_identification_model .pth"

model.load_state_dict(torch.load(pro_path, map_location=device))
model=model.to(device)
model.eval()

output=model(img)

_,predicted=torch.max(output.data,1)
predicted_name=index_to_label[predicted.item()]
print(f"the predicted name is:{predicted_name}")