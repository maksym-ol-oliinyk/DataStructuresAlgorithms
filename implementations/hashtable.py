class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        
        return hash % self.MAX 

    def __setitem__(self, key, value):
        hash = self.getHash(key)
        
        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                self.arr[hash][idx] = (key, value)
                return
            
        self.arr[hash].append((key, value))
    
    def __getitem__(self, key):
        hash = self.getHash(key)

        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                return self.arr[hash][idx][1]
    
    def __delitem__(self, key):
        hash = self.getHash(key)

        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                del self.arr[hash][idx]
    

def main():
    hashTable = HashTable()
    hashTable["aa"] = "vultures"
    hashTable["ab"] = "master of puppets"
    hashTable["ba"] = "stairway to heaven"

    print(hashTable["aa"])
    print(hashTable["ab"])
    print(hashTable["ba"])

    del hashTable["aa"]
    del hashTable["ba"]

    print("/")
    print(hashTable["aa"])
    print(hashTable["ab"])
    print(hashTable["ba"])

    

if __name__ == "__main__":
    main()