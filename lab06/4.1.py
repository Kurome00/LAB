a = [1,2,3,4,5,6,7]
print (a)
max_a = None
for num in a:
    if num % 2 == 0:
        if max_a is None or num > max_a:
            max_a = num
if max_a is not None:
    print("Наибольший четный элемент:", max_a)
else:
    print("В списке нет четных чисел")
