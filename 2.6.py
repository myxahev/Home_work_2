
list, list_name, list_cost, list_count, list_unit = [], [], [], [], []
n = 1

while True:
    count_items = input('Введите "добавить" для добавлении товара или "стоп" для завершения: ')
    if count_items == 'добавить':
        user_base = {'название': input('Введите название: '), 'цена': input('Введите цену: '),
                     'количество': input('Введите количество: '), 'ед': input('Введите единицу измерения: ')}
        list_name.append(user_base.get('название'))
        list_cost.append(user_base.get('цена'))
        list_count.append(user_base.get('количество'))
        list_unit.append(user_base.get('ед'))
        analytics = {'название': list_name, 'цена': list_cost, 'количество': list_count,
                     'ед': list_unit}
        my_list.append((n, user_base))
        n += 1
        print(' ')
        continue
    elif count_items == 'стоп':
        break
    else:
        print('Неизвестное значение, введите заново')
        continue


print(my_list)
print(analytics)