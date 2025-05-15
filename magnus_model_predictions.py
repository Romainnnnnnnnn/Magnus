from class_Magnus import Magnus
import image_acquisition

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary

def init_model(model_path):
    # Instantiate the model, use the GPU if possible
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Magnus().to(device)
    model.load_state_dict(torch.load(model_path)) # Load the model weights
    model.eval()  # Set the model to evaluation mode

    return model, device

def model_predict(model, device, data):

    # Preprocess the Data
    Data_tensor = torch.tensor(data, dtype=torch.float32).permute(0, 3, 1, 2).to(device) / 255.0  # Normalize to [0, 1]

    # Perform prediction
    with torch.no_grad():
        y_sigmoid = model(Data_tensor)
        y_pred = torch.argmax(y_sigmoid, axis=-1).cpu().numpy()

    return y_pred

def traduce_pred(y_pred):
    # Map predictions to corresponding names
    labels = ['--', 'BB', 'BK', 'BN', 'BP', 'BQ', 'BR', 'WB', 'WK', 'WN', 'WP', 'WQ', 'WR']
    y_pred_labels = [labels[pred] for pred in y_pred]
    #print(y_pred_labels)
    return y_pred_labels



if __name__ == "__main__":
    model, device = init_model("C:\\Users\\SD\\Desktop\\M1 - Q2\\Systèmes intelligents\\Magnus\\model\\Magnus_model.pth") # Path to the model weights

    image_acquisition.initialize_camera() # Initialize the camera
    Data = image_acquisition.acquire_grid_images()

    y_pred = model_predict(model, device, Data)

    print(traduce_pred(y_pred))

