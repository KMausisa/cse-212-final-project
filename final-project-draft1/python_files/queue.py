class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        value = self.items.pop(0)
        return value

    def size(self):
        return len(self.items)

#################
# Start Problem #
#################
shoppers = {
    "shopper 1": 4,
    "shopper 2": 7,
    "shopper 3": 8,
    "shopper 4": 14
}

# Create a queue
q = Queue()
# Add up to ten shoppers in the queue
if len(shoppers) <= 10:
    for shopper, items in shoppers.items():
        if items <= 12:
            q.enqueue(shopper)

for i in range(0, q.size()):
    print(q.dequeue())

# The queue will only take the first three shoppers

###############
# End Problem #
###############