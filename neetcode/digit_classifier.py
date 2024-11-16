"""
https://neetcode.io/problems/handwritten-digit-classifier
"""

import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)

        # Define the architecture here
        self.linear_layer_0 = nn.Linear(28*28, 512)
        self.relu_layer = nn.ReLU()
        self.dropout_layer = nn.Dropout(0.2)
        self.linear_layer_1 = nn.Linear(512, 10)
        self.sigmoid_layer = nn.Sigmoid()
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        output = self.linear_layer_0(images)
        output = self.relu_layer(output)
        output = self.dropout_layer(output)
        output = self.linear_layer_1(output)
        output = self.sigmoid_layer(output)

        # Return the model's prediction to 4 decimal places
        return torch.round(output, decimals=4)
