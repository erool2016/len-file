''''Задача 4 , расположение файлов по возрастанию'''
def calculate_file(list_file):
    ''''Ф запрашивает наименования файлов, и составляет список списков из названия и длинны'''

    dict_file = {}
    len_string_file = []

    for name in list_file:
        dict_file[name] = []

        with open(name, 'r', encoding='UTF-8') as f:
            list_file1 = []
            ltn_str = []
            for line in f:
                list_file1.append(line)

            ltn_str.append(name)
            ltn_str.append(len(list_file1))
        len_string_file.append(ltn_str)
        dict_file[name] += [ltn_str]
        dict_file[name] += [list_file1]

    comparison(len_string_file,dict_file)


    # return len_string_file,dict_file
def custom_key(n):
    ''''возвращает ключ для сортировки'''
    return n[1]
def comparison(len_string_file,dict_file):
    ''''расположение по возрастаню формирование результирующего файла'''
    print(f'Имена файлов в порядку чтения : {len_string_file}')
    len_string_file.sort(key=custom_key)
    print(f'Имена файлов по возрастанию: {len_string_file}')
    # формирование резултирующего файла

    with open('result_file.txt','w',encoding='UTF-8') as file:
        for name_file in len_string_file:
            text = dict_file[name_file[0]]
            file.write(f'{name_file[0]}\n{name_file[1]}\n{text[1]}\n')






list_file = []
while True:# запрос файлов для сравнения

    name_file = input('ведите название файла,- q - для выхода, all - все файлы')
    if name_file == 'q':
        break
    if name_file == 'all':
       list_file += ['1.txt','2.txt','3.txt','4.txt']
       break
    list_file.append(name_file)


calculate_file(list_file)