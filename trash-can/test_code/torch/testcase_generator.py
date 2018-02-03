import numpy, pickle

################################################################################
# LABELS                                                                       #
# The following data type labels are present                                   #
# 0 - Nothing                                                                  #
# TODO                                                                         #
################################################################################

for i in range(1, 6):
    with open("data/cifar-10-batches-py/data_batch_%d" % i, "rb") as f:
        data = pickle.load(f, encoding = "bytes")
    with open("data/cifar-10-batches-py/data_batch_%d" % i, "wb") as f:
        data[b"data"] = numpy.zeros((10000, 3072), dtype = numpy.uint8)
        f.write(pickle.dumps(data))
