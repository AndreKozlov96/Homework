file = r'Telephone.txt'


def read_txt():
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def add_txt():
    with open(file, 'a', encoding='utf-8') as f:
        abonent = input('Введите данные абонента: ')
        f.write('\n' + abonent)


def serch_txt():
    abonent = input('Введите фамилию, имя или отчество абонента: ')
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if abonent in line:
                print(line.strip())


def change_txt():
    abonent = input('Введите фамилию, имя или отчество искомого абонента: ')
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if abonent in lines[i]:
                print(lines[i].strip('\n'))
                ch = input('Вы хотите изменить/удалить данные именно этого абанента? 1 - "Да"/2 - "Нет": ')
                if ch == '1':
                    del lines[i]
                    break
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    ch = input('Уточните, Вы хотите изменить или удалить данные этого абанента? 1 - "Изменить"/2 - "Удалить": ')
    if ch == '1':
        add_txt()
    else:
        print('Данные удалены')


while True:
    print('\nВыберите режим работы:\n1 - распечатка данных\n2 - добавление абонентов\n'
          '3 - поиск абонентов\n4 - изменение/удаление данных абонентов\n5 - выход из справочника')
    ans = int(input())
    if ans == 1:
        read_txt()
    elif ans == 2:
        add_txt()
    elif ans == 3:
        serch_txt()
    elif ans == 4:
        change_txt()
    else:
        break
