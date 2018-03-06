from keras.models import Sequential
from keras.layers import *
from keras import *

from data_converter import convert

import sys, json

TRAIN = 0
TEST = 1

ARGS = sys.argv[1:]

def main():
    model = build_model()
    for data_point in get_data():
        argument = convert(data_point)
        if data_point.mode == TRAIN:
            run_training_iteration(model, data_point)
        else:
            run_test_iteration(model, data_point)

def build_model():
    model = Sequential()
    # TODO: Add layers
    return model

def get_data():
    if "--data" in ARGS:
        filename = ARGS[ARGS.index("--data") + 1]
    else:
        filename = "data.json"
    with open(filename, "r") as f:
        return json.loads(f.read())
