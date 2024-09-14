import threading
import time
import random
from collections import deque

class Queue:
    def __init__(self):
        self.collection = deque()
    
    def enqueue(self, val):
        self.collection.appendleft(val)

    def dequeue(self):
        return self.collection.pop()
    
    def front(self):
        return self.collection[-1]
    
    def size(self):
        return len(self.collection)

    def isEmpty(self):
        return self.size() == 0

#Design a food ordering system where your python program will run two threads
orders = ['pizza','samosa','pasta','biryani','burger']
activeOrders = Queue()

def makeOrder(ordersNumber):
    print(f"---- customers are here to place {ordersNumber} orders ----")
    for i in range(ordersNumber):
        newOrder = random.choice(orders)
        activeOrders.enqueue(newOrder)
        print(f"{newOrder} is placed")
        time.sleep(0.5)

def prepareOrder():
    time.sleep(1)
    print("---- we start cooking ----")
    while True:
        if not activeOrders.isEmpty():
            dish = activeOrders.dequeue()
            print(f"{dish} is ready")
        time.sleep(2)

ordersNumber = 54
customerThread = threading.Thread(target=makeOrder, args=(ordersNumber,))
restaurantThread = threading.Thread(target=prepareOrder)

#To start the threads:
#customerThread.start()
#restaurantThread.start()

#Write a program to print binary numbers from 1 to 10 using Queue

queue = Queue()
queue.enqueue("1")

for i in range(10):
    front = queue.front()
    print(front)
    queue.enqueue(front + "0")
    queue.enqueue(front + "1")

    queue.dequeue()









