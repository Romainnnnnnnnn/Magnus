import Image_acquisition
from class_Magnus import Magnus

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
# -> pip install torchsummary
from torchsummary import summary
print(torch.cuda.is_available())


model_path = ".\\model\\magnus_model.pth"
Data = Image_acquisition.acquire_grid_images()

# Instantiate the model, use the GPU if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Magnus().to(device)
model.load_state_dict(torch.load(model_path))
model.eval()  # Set the model to evaluation mode


#Data = np.stack((NewData1,NewData2,NewData3), axis = 0)

# Preprocess the Data
Data_tensor = torch.tensor(Data, dtype=torch.float32).permute(0, 3, 1, 2).to(device) / 255.0  # Normalize to [0, 1]

# Set the model to evaluation mode
model.eval()

# Perform prediction
with torch.no_grad():
    y_sigmoid = model(Data_tensor)
    y_pred = torch.argmax(y_sigmoid, axis=-1).cpu().numpy()

print(y_pred)