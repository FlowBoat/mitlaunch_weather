# -*- coding: utf-8 -*-
# Coded by Alex Liao
# Some code samples taken from open-source PyTorch tutorial code
# The objective is mainly to test matplotlib's rendering system and eventually
# for me to make my own samples and maybe train my own neural network. Who knows

import torch
import torchvision
import torchvision.transforms as transforms

import numpy as np
import matplotlib.pyplot as plt

import random

def fill(dimensions, generator = random.random):
    if len(dimensions) == 0:
        raise RuntimeError("Dimensions argument must contain at least one axis")
    elif len(dimensions) == 1:
        return [generator() for _ in range(dimensions[0])]
    else:
        return [fill(dimensions[1:], generator) for _ in range(dimensions[0])]

bit = 0

def generate():
    global bit
    bit += 0.4
    bit %= 1
    return float(bit)

a = np.array(fill((1, 3, 32, 32), generate))
b = torch.from_numpy(a)
c = torchvision.utils.make_grid(b)
d = c.numpy()
e = np.transpose(d, (1, 2, 0))
plt.imshow(e)
plt.show()
