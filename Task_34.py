def rifma(poem):
    str = poem.lower().split()
    f = lambda x: sum(1 for i in x if i in "аеёиоуыэюя")
    counter = f(str[0])
    if all([f(i) == counter for i in str]):
        return "Парам пам-пам"
    return "Пам парам"

result = rifma(input(""))
print(result)
