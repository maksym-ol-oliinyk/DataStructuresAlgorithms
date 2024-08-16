expenses = [2200, 2350, 2600, 2130, 2190] #January, February, March, April, May

# 1. In Feb, how many dollars you spent extra compare to January?
spentExtraInFeb = expenses[1] - expenses[0]
print("1.1: ", spentExtraInFeb)

# 2. Find out your total expense in first quarter (first three months) of the year.
totalExpenseQuarter = 0
for i in range(3):
    totalExpenseQuarter += expenses[i]
print("1.2: ", totalExpenseQuarter)

# 3. Find out if you spent exactly 2000 dollars in any month
twoThousandSpent = 2000 in expenses
print("1.3: ", twoThousandSpent)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("1.4: ", expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses[3] -= 200
print("1.5: ", expenses)

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
listLength = len(heros)
print("2.1: ", listLength)

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print("2.2: ", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, "black panther")
print("2.3: ", heros)

# 4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1:3]=['doctor strange']
print("2.4: ", heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("2.5: ", heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
maxNumber = int(input("Enter max number: "))
oddNumbers = []
for num in range(1, maxNumber):
    if num % 2 == 1:
        oddNumbers.append(num)
print(oddNumbers)

