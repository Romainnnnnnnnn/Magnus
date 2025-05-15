import magnus_model_predictions
import image_acquisition

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary
print(torch.cuda.is_available())

if __name__ == "__main__":
    model, device = magnus_model_predictions.init_model("C:\\Users\\SD\\Desktop\\M1 - Q2\\Systèmes intelligents\\Magnus\\model\\Magnus_model.pth") # Path to the model weights
    
    image_acquisition.initialize_camera() # Initialize the camera
    Data = image_acquisition.acquire_grid_images()

    y_pred = magnus_model_predictions.model_predict(model, device, Data)

    chess_grid_predicted = magnus_model_predictions.traduce_pred(y_pred)

    print(chess_grid_predicted)