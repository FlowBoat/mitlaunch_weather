import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.autograd import Variable

import random

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
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

def learn(inp, target):
    out = net(var)
    out.backward(target)
    criterion = nn.MSELoss()
    loss = criterion(out, target)
    net.zero_grad()
    loss.backward()
    optimizer.zero_grad()
    optimizer.step()

for _ in range(1000):
    num = random.random() * 100
    var = Variable(torch.Tensor([[[[num, num], [num, num]]]]))
    target = Variable(torch.Tensor([num]))
    learn(var, target)
    print(float(out))

print(net(Variable(torch.Tensor([[[[50, 50], [50, 50]]]]))))
