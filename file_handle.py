# with open('index.txt') as file:
#     data = file.read()
#     print(data)

# f = open('index.txt', 'r')
# for i in f:
#     print(i)
#
# with open('index.txt') as file:
#     f = file.read()
#     print(f)
f = open('index.txt', mode='r', buffering=10, encoding='utf-8')
print(f.read())
print(f.mode)
print(f.line_buffering)
print(f.close)

f.close()