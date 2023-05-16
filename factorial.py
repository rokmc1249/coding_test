def factorial(i):
    if i == 1:
        print(i)
        return 1
    else:
        result = i * factorial(i - 1)
        print(result)
        return result

result = factorial(6)
print(result)

