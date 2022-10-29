
def menu_action():
    print('1. Чтение данных: ')
    print('2. Запись данных: ')
    return input('Выберети действие: ')


def data_read():
    print('1. Справосник txt')
    print('2. Справочник csv')
    return input('Выберете тип справочника для чтения ')


def data_write():
    print('1. Справосник txt')
    print('2. Справочник csv')
    return input('Выберете тип справочника для записи ')


def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    tel = input('Введите телефон: ')
    info.append(tel)
    description = input('Введите описание: ')
    info.append(description)
    return info


                
    