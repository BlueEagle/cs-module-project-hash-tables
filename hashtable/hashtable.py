class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.fill = 0
        self.table = [None] * capacity
        '''
            Each entry will be the head of a separate linked list.
        '''


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # print(f"Fill: {self.fill/self.capacity} of Capacity: {self.capacity}")
        return self.fill/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_prime = 1099511628211
        # FNV_size = 2**64
        offset_basis = 14695981039346656037

        hash = offset_basis
        for char in key:
            hash = (hash * FNV_prime)# % FNV_size
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # print(self.fnv1(key))
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.table[self.hash_index(key)]: 
            if self.table[self.hash_index(key)].key == key:
                newHead = HashTableEntry(key, value)
                newHead.next = self.table[self.hash_index(key)].next
                self.table[self.hash_index(key)] = newHead
            else:
                newHead = HashTableEntry(key, value)
                newHead.next = self.table[self.hash_index(key)]
                self.table[self.hash_index(key)] = newHead
                self.fill += 1
        else:
            self.table[self.hash_index(key)] = HashTableEntry(key, value)
            self.fill += 1
        # print(f"Key added: {self.table[self.hash_index(key)]} at {self.hash_index(key)}")
        
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashedItem = self.table[self.hash_index(key)]
        if hashedItem.key == key:
            self.table[self.hash_index(key)] = self.table[self.hash_index(key)].next
            self.fill -= 1

        while hashedItem.next:
            prev = hashedItem
            hashedItem = hashedItem.next
            if hashedItem.key == key:
                self.fill -= 1
                if hashedItem.next:
                    prev.next = hashedItem.next
                else:
                    prev.next = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hashedItem = self.table[self.hash_index(key)]

        if hashedItem:
            if hashedItem.key == key: return hashedItem.value
            while hashedItem.next:
                hashedItem = hashedItem.next
                if hashedItem.key == key: return hashedItem.value
        return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        newTable = [None] * new_capacity
        self.capacity = new_capacity

        for item in self.table:
            curr = item

            while curr:
                key, value = curr.key, curr.value
                if newTable[self.hash_index(key)]: 
                    newHead = HashTableEntry(key, value)
                    newHead.next = newTable[self.hash_index(key)]
                    newTable[self.hash_index(key)] = newHead
                else:
                    newTable[self.hash_index(key)] = HashTableEntry(key, value)
                curr = curr.next
        
        self.table = newTable
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
