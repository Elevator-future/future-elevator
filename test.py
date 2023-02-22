print(
    *[num ** 2 for num in list(map(int, input('My numbers >>>').split())) if num % 2 == 0 and num % 10 != 4 and num != 2]
)