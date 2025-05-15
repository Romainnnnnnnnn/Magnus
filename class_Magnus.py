import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary

# Define the model
class Magnus(nn.Module):
    def __init__(self):
        super(Magnus, self).__init__()
        self.conv1 = nn.Conv2d(3, 8, kernel_size=3)  # Input: (batch_size, 3, 100, 100), Output: (batch_size, 8, 98, 98)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)  # Output: (batch_size, 8, 49, 49)
        self.dropout1 = nn.Dropout(0.2)

        self.conv2 = nn.Conv2d(8, 16, kernel_size=3)  # Input: (batch_size, 8, 49, 49), Output: (batch_size, 16, 47, 47)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)  # Output: (batch_size, 16, 23, 23)
        self.dropout2 = nn.Dropout(0.2)

        self.conv3 = nn.Conv2d(16, 32, kernel_size=3)  # Input: (batch_size, 16, 23, 23), Output: (batch_size, 32, 21, 21)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)  # Output: (batch_size, 32, 10, 10)
        self.dropout3 = nn.Dropout(0.3)

        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(6272, 400)  # Adjust input size based on the output of the last pooling layer * 11, 400)  # Adjust input size based on the output of the last pooling layer
        self.dropout4 = nn.Dropout(0.1)
        self.fc2 = nn.Linear(400, 400)
        self.dropout5 = nn.Dropout(0.2)
        self.fc3 = nn.Linear(400, 13)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = self.dropout1(x)
        # print('Output shape of layer 1', x.shape)
        
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.dropout2(x)
        # print('Output shape of layer 2', x.shape)

        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.dropout3(x)
        # print('Output shape of layer 3', x.shape)
        
        x = self.flatten(x)

        #print('Shape required to pass to Linear Layer', x.shape)

        x = F.relu(self.fc1(x))
        x = self.dropout4(x)
        x = F.relu(self.fc2(x))
        x = self.dropout5(x)
        x = self.fc3(x) # Return the raw logits
        return x