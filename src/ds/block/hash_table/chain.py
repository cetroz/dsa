class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get_hash(self, k):
        return hash(k) % self.size

    def insert(self, key, val):
        hash = self.get_hash(key)
        found = False

        for index, item in enumerate(self.table[hash]):
            if len(item) == 2 and item[0] == key:
                self.table[hash][index] = (key, val)
                found = True
                break

        if not found:
            self.table[hash].append((key, val))

    def delete(self, key):
        hash = self.get_hash(key)

        for index, item in enumerate(self.table[hash]):
            if len(item) == 2 and item[0] == key:
                del self.table[hash][index]
                break

    def get(self, key):
        hash = self.get_hash(key)
        for pair in self.table[hash]:
            if pair[0] == key:
                return pair[1]
