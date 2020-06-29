class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_index = 0
        self.items = []

    def append(self, item):
        if len(self.items) < self.capacity:

            self.items.append(item)

        else:
            
            self.items.pop(self.oldest_index)
            self.items.insert(self.oldest_index, item)

            if self.oldest_index == self.capacity - 1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1

    def get(self):
        
        return self.items