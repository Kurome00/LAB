text = input("введите строку")
count_colons = text.count(':')
text_itog = text.replace(':','%')
print("Измененная строка: ")
print (text_itog)
print("Колличество замен равно:")
print (count_colons)
