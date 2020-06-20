
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.items = []
        self.capacity = capacity
        self.lenght = 0
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        for item in self.items:

            if key == item[0]:
                return item[1]
        
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.lenght >= self.capacity: 
            self.items.pop(0)
        self.items.append((key, value))
        self.lenght += 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
