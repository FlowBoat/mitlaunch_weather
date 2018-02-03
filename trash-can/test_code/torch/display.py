import pickle

data = pickle.load(open("./data/cifar-10-batches-py/data_batch_1", "rb"), encoding = "bytes")[b"data"]
print(data)
