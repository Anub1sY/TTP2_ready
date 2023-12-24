import Task1
import Task7
import Task9


def menu():
    while True:
        print('Главное меню:'
              '1. Задание 1'
              '2. Задание 7'
              '3. Задание 8'
              '4. Выход из программы ')

        menu_point = input('Выберите пункт меню: ')

        if menu_point == '1':
            Task1.start_task1()

        elif menu_point == '2':
            Task7.start_task7()

        elif menu_point == '3':
            Task9.start_task9()

        elif menu_point == '4':
            print('Выход из программы.')
            break
        else:
            print('Некорректный выбор. Пожалуйста, выберите снова.')


if __name__ == "__main__":
    menu()
