

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    djb2_hash = 5381

    for char in string:
        djb2_hash = ((djb2_hash * 33) ^ char) % hex(max)

    return djb2_hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_pair = Pair(hash(key, hash_table.capacity), value)

    if new_pair.value == hash_table.storage[new_pair.key]:
        print("You are overwriting a value with a different key")
    hash_table.storage[new_pair.key] = new_pair.value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    removing = hash(key, hash_table.capacity)

    if hash_table[removing] is None:
        print("There is no value to remove.")
    hash_table[removing] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    for i in hash_table.storage:
        if i == key:
            return i
        else:
            return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
