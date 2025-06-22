
import torch
from mindmap_neural_net import MindMapNeuralNet
from mindmap_dataloader import load_sample_data

def train_model(epochs=10):
    data_loader = load_sample_data()
    model = MindMapNeuralNet()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.CrossEntropyLoss()

    for epoch in range(epochs):
        for inputs, labels in data_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

    torch.save(model.state_dict(), "trained_model.pt")
    print("Training complete. Model saved as trained_model.pt")

if __name__ == "__main__":
    train_model()
