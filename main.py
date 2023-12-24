# import sth


def menu():
    while True:
        print('Главное меню:'
              '1. Задание 1'
              '2. Задание 7'
              '3. Задание 8'
              '4. Выход из программы ')

        menu_point = input('Выберите пункт меню: ')

        if menu_point == '1':
            pass

        elif menu_point == '2':
            pass

        elif menu_point == '3':
            pass

        elif menu_point == '4':
            print('Выход из программы.')
            break
        else:
            print('Некорректный выбор. Пожалуйста, выберите снова.')


if __name__ == "__main__":
    menu()
