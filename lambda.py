# Lambda Function

def result(a, b):
    sum = a + b * a
    print(sum)
result(56, 23)

result_1 = lambda x, y: x + y * x
print(result_1(56, 23))
