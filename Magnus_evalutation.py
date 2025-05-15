import Image_acquisition
from class_Magnus import Magnus

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary
print(torch.cuda.is_available())


model_path = ".\\model\\magnus_model.pth"

# Instantiate the model, use the GPU if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Magnus().to(device)

model.load_state_dict(torch.load(model_path)) # Load the model weights
model.eval()  # Set the model to evaluation mode


#Data = np.stack((NewData1,NewData2,NewData3), axis = 0)
Data = Image_acquisition.acquire_grid_images()

# Preprocess the Data
Data_tensor = torch.tensor(Data, dtype=torch.float32).permute(0, 3, 1, 2).to(device) / 255.0  # Normalize to [0, 1]

model.eval() # Set the model to evaluation mode

# Perform prediction
with torch.no_grad():
    y_sigmoid = model(Data_tensor)
    y_pred = torch.argmax(y_sigmoid, axis=-1).cpu().numpy()

print(y_pred)

# Map predictions to corresponding names
labels = ['--', 'BB', 'BK', 'BN', 'BP', 'BQ', 'BR', 'WB', 'WK', 'WN', 'WP', 'WQ', 'WR']
y_pred_labels = [labels[pred] for pred in y_pred]

print(y_pred_labels)


