requests = [90, 36, 384, 33, 306, 203, 347, 238, 35, 146, 255, 137]
page_size = 100
memory_size = 400
num_frames = memory_size // page_size


# FIFO Page Replacement Algorithm
def fifo(requests, num_frames):
    memory = []
    page_faults = 0

    for request in requests:
        page = request // page_size

        if page not in memory:
            if len(memory) < num_frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

    success_frequency = 1 - (page_faults / len(requests))
    return success_frequency


# LRU Page Replacement Algorithm
def lru(requests, num_frames):
    memory = []
    page_faults = 0
    counter = {}

    for request in requests:
        page = request // page_size

        if page not in memory:
            if len(memory) < num_frames:
                memory.append(page)
            else:
                oldest_page = min(memory, key=counter.get)
                memory.remove(oldest_page)
                memory.append(page)
            page_faults += 1

        counter[page] = request

    success_frequency = 1 - (page_faults / len(requests))
    return success_frequency


# Calculate success frequency
fifo_success_frequency = fifo(requests, num_frames)
lru_success_frequency = lru(requests, num_frames)

print(f"FIFO Success Frequency: {fifo_success_frequency}")
print(f"LRU Success Frequency: {lru_success_frequency}")
