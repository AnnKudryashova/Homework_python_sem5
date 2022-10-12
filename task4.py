#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

def RLE(txt):
    count  =  1
    result = " "
    for i in range (len(txt) - 1):
        if txt [i] == txt[i+1]:
            count  += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        result = result + str(count) + txt[-1]
    return result

x = input("Введите текст для сжатия данных: ")
print(f"Текст после сжатия данных: {RLE(x)}")


# def RLE_2(txt):
#     number = ''
#     result = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             result = result + txt[i] * int(number)
#             number = ''
#     return result

# x = input("Введите текст для восстановления данных: ")
# print(f"Текст после восстановления данных: {RLE_2(x)}")