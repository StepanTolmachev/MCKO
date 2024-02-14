fin = open('songs.csv','r', encoding='utf-8')
tittle=fin.readline()
songs=[x.strip().split(',') for x in fin]
fin.close()
while True:
    n = input('Введите имя артиста:')
    if n.upper()=='СТОП':
        break
    for x in songs:
        if n==x[2]:
            fio=x[1].split()
            print(f'название песни {x[2]} имя артиста: {fio[1][0]}.{fio[0]} ')
            break
        else:
            print('Ничего не найдено')