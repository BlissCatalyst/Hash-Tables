

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + ord(x))
    result = hash & 0xFFFFFFFF
    return result % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] is None:
        new_node = LinkedPair(key, value)
        hash_table.storage[index] = new_node
    else:
        current_node = hash_table.storage[index]
        while current_node.next is not None:
            if current_node.key == key:
                current_node.value = value
                return
            current_node = current_node.next
        current_node.next = LinkedPair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
# *** DOES NOT REMOVE NODES - Just changes the keys and values to "None" and keeps the value of .next
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] is None:
        print('There is no value to delete at that key!')
    else:
        current_node = hash_table.storage[index]
        while current_node is not None:
            if current_node.key == key:
                current_node.key = None
                current_node.value = None
                print("Removed successfully")
                return
            current_node = current_node.next
        if current_node is None:
            print('There is no value to delete at that key!')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] is None:
        print("There is no value at that key!")
    else:
        current_node = hash_table.storage[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        if current_node is None:
            print("There is no value at that key!")


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_table = HashTable(len(hash_table.storage) * 2)
    for x in hash_table.storage:
        if x is None:
            continue
        else:
            current_node = x
            while current_node is not None:
                hash_table_insert(new_table, current_node.key,
                                  current_node.value)
                current_node = current_node.next
    return new_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
