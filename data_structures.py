import time
# recursion

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n in [0, 1]: # if n is 0 or 1
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

# fibonacci numbers/sequence - cumulative frequency
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


# Big O Notation
'''
Big O notation is used to measure how running time or space requirements for your program grow as input size grows

O(n)
for a linear program that in which time taken is proportional to number/size or array or iteration,
time = a*n + b

rule 1: keep the fastest growing term, i.e, time = a * n
rule 2: drop constants i.e time = n
hence, time = O(n)
the Big O time complexity of the program is n

example:
'''
def get_squared_numbers(numbers):
    start = time.time()
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    end = time.time()
    print('time = ',end - start)
    return squared_numbers

numbers = [2, 5, 8, 9, 4, 7, 2, 5, 9, 2, 6, 11, 77, 2, 66, 36, 80]
print(get_squared_numbers(numbers)) 
print()

'''
O(1)
example:
'''
def find_first_pe(prices, eps, index):
    start = time.time()
    pe = prices[index]/eps[index]
    end = time.time()
    print('time = ',end - start)
    return pe
prices = [5, 7, 2, 8, 6, 9, 10, 3, 6, 6, 7, 20, 13]
eps = [2, 3, 4, 5, 8, 9, 4, 7, 2, 5, 9, 2, 6]
index = 3
print(find_first_pe(prices, eps, index))

'''
time = a * n2 + b
O(n2)
example 1:
'''
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], ' is a duplicate')
            break

print()
# example 2
# an2 + bn + c
# first, n2 iterations
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

# second,  n iterations
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)
'''
instead  of n iterations in above, we can use binary search
iteration 1 = n/2
iteration 2 = n/2^2
iteration 3 = n/2^3
...
number of iterations k = n/2^k
worst case scenario is 1 i.e there will be at least 1 iteration
1 = n/2^k
n = 2^k
take the log base 2 of both sides

k = log n, n = number of elements
'''

# anagram example
# example 1 : checking off O(n^2)
def anagram_solution1(s1,s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1
    return still_ok

print(anagram_solution1('abcd','dcba'))


# solution 2 : sort and compare O(n^2) or O(n log n)
def anagram_solution2(s1,s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

print(anagram_solution2('abcde','edcba'))


# solution 3 : brute force

# solution 4: count and compare
def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok

print(anagram_solution4('apple','pleap'))

# how to measure codes using Big O
'''
1. Any assignment statements and if statements that are executed once regardless of the size of the problem     O(1)
2. A simple for loop from 0 to n with no internal loops        O(n)
3. A nested loop of the same type takes quadratic time complexity    O(n^2)
4. A loop, in which the controlling parameter is divided by two at each step     O(log n)
5. When dealing with multiple statements, just add them up
'''
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]  #-----------------------------> O(1)
    for index in range(1, len(sampleArray)):    #-----------------> O(n)
        if sampleArray[index] > biggestNumber:  #-------> O(1)
            biggestNumber = sampleArray[index]  #-------> O(1)
    print(biggestNumber)#-----------------------------------------> O(1)
# Time complexity = O(1) + O(n) + O(1) = O(n)

# using recursion
def findMaxNumRec(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1))


# stacks in python
from collections import deque
stack = deque()
print(dir(stack))   # available methods
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
stack.append('f')
#print(stack)
print()

# create a stack object
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def list(self):
        return self.container

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.push('e')
s.push('f')
print(s.list())

print()

# reverse string
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
