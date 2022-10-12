#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input("Введите текст: ")
print(f"Исходный текст: {text}")
text_2 = "абв"
list = [i for i in text.split() if text_2 not in i]
print(f'Результат: {" ".join(list)}')