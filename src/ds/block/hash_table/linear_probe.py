class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def get_hash(self, key):
        return hash(key) % self.size

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size

        for item in old_table:
            if item is not None and item is not self.deleted:
                self.insert(item[0], item[1])

    def insert(self, key, val):
        if self.load_factor() > 0.7:
            self.resize()

        hash_index = self.get_hash(key)
        if (
            self.table[hash_index] is None
            or self.table[hash_index] is self.deleted
            or self.table[hash_index][0] == key
        ):
            self.table[hash_index] = (key, val)
            return

        original_index = hash_index
        while self.table[hash_index] is not None:
            hash_index = (hash_index + 1) % self.size
            if original_index == hash_index:
                self.resize()
                return self.insert(key, val)
        self.table[hash_index] = (key, val)

    def get(self, key):
        hash_index = self.get_hash(key)
        original_index = hash_index

        while self.table[hash_index] is not None:
            if self.table[hash_index][0] == key:
                return self.table[hash_index][1]
            hash_index = (hash_index + 1) % self.size
            if original_index == hash_index:
                break

        return None

    def rehash(self, hash_index):
        hash_index = (hash_index + 1) % self.size
        while self.table[hash_index] is not None:
            if self.table[hash_index] is not self.deleted:
                key, value = self.table[hash_index]
                self.table[hash_index] = self.deleted
                self.insert(key, value)
            hash_index = (hash_index + 1) % self.size

    def delete(self, key):
        hash_index = self.get_hash(key)
        while self.table[hash_index] is not None:
            if (
                self.table[hash_index] is not self.deleted
                and self.table[hash_index][0] == key
            ):
                self.table[hash_index] = self.deleted
                self.rehash(hash_index)
                return
            hash_index = (hash_index + 1) % self.size
        return

    def load_factor(self):
        return sum(1 for item in self.table if item is not None) / self.size
