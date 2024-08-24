# lst1 = [i ** 2 for i in range(10)]
# # print(lst1)
#
# lst2 = [i for i in range(1, 21) if i % 2 ==0]
# print(lst2)
# print("Without uing list Comprehension...")
# l = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         if i % 3 == 0:
#             l.append(i)
# print(l)
#
# print("Using list comprehension....")
# new_lst = [i for i in range(1, 21) if i % 2 ==0 if i % 3 == 0]
# print(new_lst)
# result_1 = []
# marks = [45, 23, 56, 34, 23, 89, 31, 32]
# for i in marks:
#     if i >= 32:
#         result_1.append(i)
# print(result_1)
#
# result_2 = [num if num >= 32 else "Fail" for num in marks]
# print(result_2)
#
# lst2 = [[i * j for j in range(1, 5)] for i in range(1,3)]
# print(lst2)
# set1 = {i for i in range(10) if i % 2 == 0 if i % 3 == 0}
# set2 = {i * j for j in range(2,4) for i in range(5, 8)}
# print(set1)
# print(set2)
# n_dict = {i:i**2 for i in range(1, 10) if i % 2 == 0}
# print(n_dict)

# num = [34, 2, 23, 19, 98, 43]
# odd_even_filter = {i:('Pass' if i % 2 == 0 else "Fail") for i in num}
# print(odd_even_filter)

# Comprehension List
new_list = [i for i in range(1, 20) if i % 3 == 0 if i % 2 ==0]
print(new_list)

for x in range(1, 20):
    if x % 3 == 0:
        if x % 2 == 0:
            print(x, end=" ")