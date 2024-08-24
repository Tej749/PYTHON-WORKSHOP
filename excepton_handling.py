# Pythoon Comprehension
'''
1. List Comprehension
2. Set Comprehension
3. Dictionary Comprehension

'''
# List Comprehension
# without List comprehension

l = []

for i in range(1, 20):
    if i % 2 == 0:
        if i % 3 == 0:
            l.append(i)

print(l)


# With List Comprehension

new_list = [x for x in range(1, 20) if x % 2 == 0 if x % 3 == 0]
print(new_list)

# Dictionary Comprehension

dict = {n:n*2 for n in range(10)}
print