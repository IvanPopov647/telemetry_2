with open("Text_2.txt", 'w') as file_obj:
    file = ['1 stroka\n', '2 stroka2\n', '3 stroka\n', '4 stroka\n', '5 stroka\n']
    file_obj.writelines(file)

with open("Text_2.txt") as file_obj:
    stroki = 0
    simvoli = 0
    for line in file_obj:
        stroki += line.count("\n")
        simvoli = len(line)-1
        print(f"{simvoli} символов в строке")

    print(f"Всего строк: {stroki}")