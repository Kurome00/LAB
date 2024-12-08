text = [2,3,4,1,5,6,7,8,6,5,4,3,5,6,8,6,4,5,6,7,8,9,7,6,5,4,3,6,7,8,9,12,14,16]
print (text)
text_itog = [num for num in text if num % 2 == 0 and num < 10]
if text_itog:
    text_itog.sort()
    print("Массив:", text_itog)
else:
    print("Четных чисел меньше 10 нет")
