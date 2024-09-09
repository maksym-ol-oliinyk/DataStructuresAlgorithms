from collections import deque

class Stack:
    def __init__(self):
        self.collection = deque()
    
    def push(self, value):
        self.collection.append(value)

    def pop(self):
        return self.collection.pop()
    
    def peek(self):
        return self.collection[-1]
    
    def print(self):
        print(self.collection)
    
    def size(self):
        return len(self.collection)
    
    def isEmpty(self):
        return self.size() == 0
    
#Write a function in python that can reverse a string using 
#stack data structure. Use Stack class from the tutorial.

def reverse_string(str):
    stack = Stack()
    reversed = ""

    for ch in str:
        stack.push(ch)

    while not stack.isEmpty():
        reversed += stack.pop()
    
    return reversed

print(reverse_string("We will conquere COVID-19")) 

#Write a function in python 
#that checks if paranthesis in the 
#string are balanced or not. Possible parantheses are 
# "{}',"()" or "[]". Use Stack class from the tutorial.

def is_balanced(str):
    symbols = Stack()

    for ch in str:
        if ch == "{" or ch == "(" or ch == "[":
            symbols.push(ch)
        if (ch == "}" or ch == ")" or ch == "]") and symbols.isEmpty():
            return False
        if ch == "}" and symbols.peek() == "{":
            symbols.pop()
        if ch == ")" and symbols.peek() == "(":
            symbols.pop()
        if ch == "]" and symbols.peek() == "[":
            symbols.pop()
    
    return symbols.isEmpty()


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))   
print(is_balanced("((a+b))"))     
print(is_balanced("))"))          
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

