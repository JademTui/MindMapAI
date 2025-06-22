
import torch
import torch.nn as nn
import torch.nn.functional as F

class MindMapNeuralNet(nn.Module):
    def __init__(self, input_size=128, hidden_size=256, output_size=10, dropout_rate=0.3):
        super(MindMapNeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.dropout = nn.Dropout(dropout_rate)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
