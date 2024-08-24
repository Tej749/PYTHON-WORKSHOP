# a = 56
# b = 67
# sum = a + b
# def sum():
#     sum = a + b
#     # print(sum)

# print(sum)
# Syntax : It is the set of rule that define how python code will be written and interpreted is called syntax.
# print("Hello World !")      #it is the default message of python programming (inline comment, single line comment)
print ("Hello Dear!!")

x = '56'    # string
y = 50
print(type(x))
x = int(x)  # now convert fron string to integer

print(type(x))
sum = x + y

print(sum)

# It is an attribute associate with piece of data tell the computer how it will be interpreted its values.
x = 45
name = 'ram'        # string
gpa = 3.7           # float /decimal
isFemale = True     # boolean value ; True or False
data_a = [34, 23, 12, 15, 'ram']    # list: It is the collection of data which is ordere, separated by comma, enclosed in big/square brcaket. It's a mutable type data.
data_b = (23, 78, 'shyam', 23)  # tuple; it's some how similar to list, but it is immutable data.
data_c = {23, 12, 14, "Gita", 'sita', "Gita", 'sita'}   # set: it the collection of unique value,,,number of same value element counted as single value.
data_e = {'id':101, 'name':'hari', 'school': 'NCMT'}    # dictionary : mapping the data in key -  value pairs: eacj Keys is associate with their own value.
print(data_e.get('school'))
# print(type(name))
# print(type(x))
# print(type(gpa))
print(data_a)
print(data_b)
print(data_c)

# Python comment: It's used to define complex code, which make easy to understand.

for i in range(10):
    print(i, end=" ") # end = "" ; it's used to print data horizontally ; single line comment, inline comment

# BCA 2077
stu_1 = "Shiwani"
stu_2 = "Najuma"
stu_3 = "Prasha"
stu_4 = "Sumit"
stu_5 = "Rajiv"
print(f'''
    {stu_1} is the top student.
    {stu_2} is the district topper
    {stu_3} is a good developer's.
    {stu_4} is very good in Networking.
    {stu_5} is very genius in NM.
''')
list = [1,2,3, [34, 56, 'tej'], 67]
print(list[3][2])
import datetime
d = datetime.date(2024, 7, 17)
print(d)