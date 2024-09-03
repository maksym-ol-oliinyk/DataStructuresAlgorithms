import csv
import re

#nyc_weather.csv contains new york city weather for first few days in 
#the month of January.

def csv_to_hashtable(file_path):
    hashtable = {}
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for row in csv_reader:
            key = row[0]
            value = row[1]
            hashtable[key] = value
    
    return hashtable

hashtable = {}
file_path = 'resources/nyc_weather.csv'
hashtable = csv_to_hashtable(file_path)

#What was the average temperature in first week of Jan
#What was the maximum temperature in first 10 days of Jan
#What was the temperature on Jan 9?
#What was the temperature on Jan 4?

firstWeekTemperatures = 0
maxTemperature = 0

for i in range(1,11):
    dayTemperature = int(hashtable["Jan " + str(i)])

    if i < 8:
        firstWeekTemperatures += dayTemperature
    if dayTemperature > maxTemperature:
        maxTemperature = dayTemperature
    
averageTemperature = firstWeekTemperatures / 7
print("{:.1f}".format(averageTemperature))
print("{:.1f}".format(maxTemperature))
print("{:.1f}".format(int(hashtable["Jan 9"])))
print("{:.1f}".format(int(hashtable["Jan 4"])))

#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
#You have to read this file in python and print every word and its count 
#as show below. Think about the best data structure that you can use 
#to solve this problem and figure out why you selected that specific 
#data structure.

fileContents = ""
with open('resources/poem.txt', 'r') as file:
    # Read the file contents and store it as a string
    fileContents = file.read()

cleanedContents = re.sub(r'[^A-Za-z0-9\s]', '', fileContents)
cleanedContents = cleanedContents.split(" ")
wordsCount = {}
for word in cleanedContents:
    if word in wordsCount:
        wordsCount[word] += 1
    else:
        wordsCount[word] = 1 

print(wordsCount)

#Implement hash table where collisions are handled using linear probing. 
#We learnt about linear probing in the video tutorial. 
#Take the hash table implementation that uses chaining and modify 
#methods to use linear probing. Keep MAX size of arr in hashtable as 10.

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        
        return hash % self.MAX

    def insert(self, key, value):
        hash = self.hash(key)

        if self.arr[hash] == None:
            self.arr[hash] = (key, value)
        else:
            idx = (hash + 1) % self.MAX
            for i in range(self.MAX):
                if self.arr[idx] == None:
                    self.arr[idx] = (key, value)
                    break
                idx = (idx + 1) % self.MAX
    
    def get(self, key):
        hash = self.hash(key)

        if self.arr[hash] == None:
            return None
        elif self.arr[hash][0] == key:
            return self.arr[hash][1]
        else:
            idx = (hash + 1) % self.MAX
            for i in range(self.MAX):
                if not self.arr[idx] == None and self.arr[idx][0] == key:
                    return self.arr[idx][1]
                idx = (idx + 1) % self.MAX
            
            return None
    
    def delete(self, key):
        hash = self.hash(key)

        if not self.arr[hash] == None and self.arr[hash][0] == key:
            self.arr[hash] = None
        else:
            idx = (hash + 1) % self.MAX
            for i in range(self.MAX):
                if not self.arr[hash] == None and self.arr[idx][0] == key:
                    self.arr[idx] = None
                    break
                idx = (idx + 1) % self.MAX

hashtable = HashTable()
hashtable.insert("hello", "hi")
hashtable.insert("hello2", "hi2")
hashtable.insert("helol", "hi3")
hashtable.insert("hello4", "hi4")
hashtable.insert("hello8", "hi8")
hashtable.insert("hello9", "hi9")
hashtable.insert("HELLO11111", "hi10")

print(hashtable.get("hello"))
print(hashtable.get("helol"))
print(hashtable.get("HELLO11111"))

hashtable.delete("HELLO11111")
print(hashtable.get("HELLO11111"))

            



