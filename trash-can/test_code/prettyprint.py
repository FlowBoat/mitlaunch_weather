def gather(data, delta):
    left = min(data)
    length = int((max(data) - left) / delta)
    counts = [0] * length
    for point in data:
        counts[min(length - 1, int((point - left) / delta))] += 1
    return counts

def plot(data, delta):
    counts = gather(data, delta)
    maxcount = max(counts)
    zipped = [list(("*" * count).ljust(maxcount)) for count in counts]
    return "\n".join(list(map("".join, zip(*zipped)))[::-1])
