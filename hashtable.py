# Initialize the hash table with the package size
class HashTable:
    def __init__(self, size=40):
        self.table_size = size
        self.table = [None] * self.table_size

    #Hash function based on package ID.
    # Using modulus to get an index
    def _hash(self, package_id):
        return package_id % self.table_size

    # Inserts a package into hashtable
    def insert(self, package):
        index = self._hash(package.package_id) # Determine starting index
        while self.table[index] is not None:
            index = (index + 1) % self.table_size # Moves to the next index

        # Inserts package into the available spot
        self.table[index] = package

    # Searches for package by its ID
    def search(self, package_id):
        index = self._hash(package_id)

        # Search for package
        while self.table[index] is not None:
            if self.table[index].package_id == package_id:
                return self.table[index]  # If found returns the package details
            index = (index + 1) % self.table_size # Continues to search

        return None  # Returns None if package is not found

    # Removes a package from hashtable
    def remove(self, package_id):
        index = self._hash(package_id)

        # Search for the package
        while self.table[index] is not None:
            if self.table[index].package_id == package_id:
                self.table[index] = None  # Removes package by setting the spot to None
                return True # Returns True if successful
            index = (index + 1) % self.table_size # Keeps searching if necessary

        return False  # Return False if package not found







