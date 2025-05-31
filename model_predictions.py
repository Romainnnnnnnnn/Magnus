from model_class_Magnus import Magnus
import image_acquisition

import numpy as np
import torch
import cv2
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

def preprocess_images(data):
    processed = []
    for img in data:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        processed.append(img)
    return np.array(processed)

def model_predict(model, device, data):
    data = preprocess_images(data)
    Data_tensor = torch.tensor(data, dtype=torch.float32).permute(0, 3, 1, 2).to(device) / 255.0
    with torch.no_grad():
        y_logits = model(Data_tensor)
        y_pred = torch.argmax(y_logits, axis=-1).cpu().numpy()
    return y_pred

def traduce_pred(y_pred):
    # Map predictions to corresponding names
    labels = ['--', 'bb', 'bk', 'bn', 'bp', 'bq', 'br', 'wb', 'wk', 'wn', 'wp', 'wq', 'wr']
    #labels = ['--', 'BB', 'BK', 'BN', 'BP', 'BQ', 'BR', 'WB', 'WK', 'WN', 'WP', 'WQ', 'WR']
    y_pred_labels = [labels[pred] for pred in y_pred]
    #print(y_pred_labels)
    return y_pred_labels



if __name__ == "__main__":
    #model, device = init_model("C:\\Users\\SD\\Desktop\\M1 - Q2\\Systèmes intelligents\\Magnus\\model\\Magnus_model.pth")
    model, device = init_model("C:\\Projets\\Projet_Magnus\\venv\\Magnus\\model\\Magnus_model.pth")

    image_acquisition.initialize_camera()
    Data = image_acquisition.acquire_grid_images()

    y_pred = model_predict(model, device, Data)

    print(traduce_pred(y_pred))

