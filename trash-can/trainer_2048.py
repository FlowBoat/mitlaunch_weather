import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import pickle

from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 1, 1)
        self.fc1 = nn.Linear(4, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

net = Net()
params = list(net.parameters())

criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr = 0.01)

with open("data", "rb") as f:
    data = pickle.load(f)
    for input, des in data:
        out = net(input)
        target = Variable(torch.Tensor([[des]]))
        out.backward(target)
        criterion = nn.MSELoss()
        loss = criterion(out, target)
        net.zero_grad()
        loss.backward()
        optimizer.zero_grad()
        optimizer.step()

print("Random tests?")

print(round(float(net(Variable(torch.Tensor([[[[0, 2, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]])))[0][0][0])))
