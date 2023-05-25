'''
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given numberFor example,
if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
'''

s = 0
num = int(input("Enter number: "))

for eachNum in range(1, num+1):
    s *= eachNum
#print("\n")
print(s)
