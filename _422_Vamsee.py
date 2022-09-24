#1. Implement palindrome using iterator(for loop) and generator mechanism.
print("--------------Checking palindrome using for loop----------------------")
str1= input("Enter a word:")
flag=True
for i in range(len(str1)):
    if str1[i]!=str1[-1-i]:
        flag = False
        break
if flag== True:
    print("It is a palindrome ")
else:
    print("It is not a palindrome")
def palindrome(word):
    for i in range(len(word)):
        if word[i]!=word[-1-i]:
            yield False
        else:
            yield True
print("--------------Checking palindrome using Generator----------------------")
obj=palindrome(str1)
if False in obj:
    print("It is not a palindrome")
else:
    print("It is a palindrome")
#2 Sum of 2 digits into output
		#n1 = 1234 # int(input("Enter number1 :" ))
		#n2 = 9999 # int(input("Enter number2 :" ))
		#Output: 9+1 2+9 3+9 4+9
		         ##46

print("------Sum of digits of 2 numbers-------")


n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n1 = list(str(n1))
n2 = list(str(n2))

print("Other Method")

def sum_of_two_numbers(a, b):
    return int(a) + int(b)

sum_of_ind=list(map(sum_of_two_numbers,n1,n2))
print("sum of elements of same indices:",sum_of_ind)
print("Total sum:",sum(sum_of_ind))

#3
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
    # findout elements duplicate count output in  dict format
dict_={}
for i in some_list:
    if some_list.count(i)>1:
        dict_[i]=some_list.count(i)
print(dict_)
#4
st = "ab@#cd!ef"
#Reverse string considering only alphabets. Symobls should not be reversed
# Output: fe@#dc!ba
print("-----------Reverse string except special characters-----------")
def reverseString(text):
    index = -1

    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text
string = reverseString(list(st))
print ("Output string: ", "".join(string))
#5.
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for i in t1:
    if isinstance(i, int):
        for j in t2:
            if j not in lis2 and isinstance(j, int):
                lis2.append(j)
                lis1.append((i + j))
                break
    else:
        for j in t2:
            if j not in lis2 and isinstance(j, str):
                lis2.append(j)
                lis1.append((i + j))
                break
print(lis1)

#6 Write a Python program to remove leading zeros from an IP address.
#inp = "216.08.094.196"
## o/p =  216.8.94.196
print("-------------Python program to remove leading zeros from an IP address--------------")
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)
#7
print("--------Elements in Nested list into single list----------------------------")
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]

def rec(l):
    li = []
    for i in l:
        if isinstance(i, int):
            li.append(i)
        elif isinstance(i, list):
            x=rec(i)
            li.extend(x)
    return li
print(rec(l))
#Load sample content in text file.
   #Read data and find
    #1. No of lines in file
	#3. No of chars in each line
	#4. No of vowels and consonants
	#5. No of special chars linewise and total
#1. No of lines in file
print("-----1.No of lines in a file--------")
with open(r"C:/Users/Windows/PycharmProjects/pythonProject3/test.txt","r") as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
#3. No of chars in each line
with open(r"C:/Users/Windows/PycharmProjects/pythonProject3/test.txt","r") as fp:
    data=fp.readlines()
    print('Total Number of characters of lines:', len(data[0]))

a=[54,'54',76,77,76.9,12,45.87,'django']
# final_list = list(filter(lambda x: (type(x) == int or type(x)==float), a))
# print(final_list)

l1=[]
for i in a:
    if type(i)==int:
        l1.append(i)
print(l1)

dict = {
    "1": 1,
    "2": 2,
    "3": {
        "4": 4,
        "5": 5,
        "6": {
            "7": 7,
            "8": 8
        },
        "9": {
            "10": 10
        }
    }
}
defualt_dict = {"1": "one", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "six", "7": "seven", "8": "eight", "9": "Nine", "10": "Ten"}
