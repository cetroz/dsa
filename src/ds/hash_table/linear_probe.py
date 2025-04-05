class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def get_hash(self, key):
        return hash(key) % self.size

    def resize(self):
        old_table = self.table
        self.size += 1
        self.table = [None] * self.size

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    def insert(self, key, val):
        hash_index = self.get_hash(key)
        if self.table[hash_index] and self.table[hash_index][0] == key:
            self.table[hash_index] = (key, val)
            return
        elif not self.table[hash_index]:
            self.table[hash_index] = (key, val)
            return
        else:
            original_index = hash_index
            while self.table[hash_index] is not None:
                hash_index = (hash_index + 1) % self.size
                if original_index == hash_index:
                    self.resize()
                    return self.insert(key, val)
            self.table[hash_index] = (key, val)

    def get(self, key):
        hash_index = self.get_hash(key)
        if self.table[hash_index] is None:
            return
        if self.table[hash_index][0] == key:
            return self.table[hash_index][1]
        else:
            original_index = hash_index
            while self.table[hash_index] is not None:
                hash_index = (hash_index + 1) % self.size
                if self.table[hash_index] is None:
                    return None
                if self.table[hash_index][0] == key:
                    return self.table[hash_index][1]
                if original_index == hash_index:
                    return
