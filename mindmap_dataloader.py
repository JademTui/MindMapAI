
import torch
from torch.utils.data import DataLoader, TensorDataset

def load_sample_data():
    inputs = torch.randn(100, 128)
    labels = torch.randint(0, 10, (100,))
    dataset = TensorDataset(inputs, labels)
    return DataLoader(dataset, batch_size=8, shuffle=True)
