import MySQLdb
from datetime import datetime

dataBase = MySQLdb.connect('127.0.0.1', 'root', 'root', 'mark')
cursor = dataBase.cursor()


def validate_date():
    print('Введите дату рождения сотрудника форматом ГОД-МЕСЯЦ-ДЕНЬ: ')
    date = input()
    try:
        b = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Неверный формат даты...")
        validate_date()
    return date


def Insert():
    cursor = dataBase.cursor()
    name = input('Введите ФИО сотрудника:\n')
    date = validate_date()
    experience = input('Введите опыт работы сотрудника:\n')
    sql = "INSERT INTO mark_staff (name, date, experience) VALUES (%s, %s, %s)"
    val = (name, date, experience)
    cursor.execute(sql, val)
    dataBase.commit()
    with dataBase.cursor() as cursor:
        sql = f"SELECT name, date, experience FROM `mark_staff` WHERE name = '{name}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(
            'Добавлен сотрудник с именем ' + result[0] + ', датой рождения ' + result[1] + ' и опытом работы ' + result[
                2] + '.\n')


def Select():
    cursor = dataBase.cursor()
    cursor.execute("SELECT name FROM mark_staff")
    for row in cursor.fetchall():
        print('ФИО: ' + row[0])
    worker = input("Введите ФИО сотрудника из списка: ")
    with dataBase.cursor() as cursor:
        sql = f"SELECT date, experience FROM `mark_staff` WHERE name = '{worker}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print('Дата рождения: ' + result[0] + ', опыт работы ' + result[1] + '.\n')


def Update():
    cursor = dataBase.cursor()
    cursor.execute("SELECT name FROM mark_staff")
    for row in cursor.fetchall():
        print('ФИО: ' + row[0])
    username = input('Введите фио сотрудника из списка, информацию о котором хотите обновить:\n')
    with dataBase.cursor() as cursor:
        sql = "SELECT date, experience FROM `mark_staff` WHERE `name`=%s"
        cursor.execute(sql, [username])
        result = cursor.fetchone()
        print('ИНФОРМАЦИЯ О СОТРУДНИКЕ\nДата рождения: ' + result[0] + ', опыт работы ' + result[1] + '.')
    STOPPER = 1
    while STOPPER != 0:
        information_to_update = input("""Введите цифру 1, если хотите обновить фио сотрдуника;
Введите цифру 2, если хотите обновить дату рождения сотрудника
Введите цифру 3, если хотите обновить опыт работы сотрудника
Введите цифру 4, чтобы обновить все данные сотрудника;\n""")
        if information_to_update == '1':
            Name(username)
            STOPPER = 0
        elif information_to_update == '2':
            Date(username)
            STOPPER = 0
        elif information_to_update == '3':
            Experience(username)
            STOPPER = 0
        elif information_to_update == '4':
            All(username)
            STOPPER = 0
        else:
            print('Неправильно введены данные для обновления..')


def Date(username):
    cursor = dataBase.cursor()
    new_date = validate_date()
    sql = "UPDATE mark_staff SET date=%s WHERE name=%s"
    values = (new_date, username)
    cursor.execute(sql, values)
    dataBase.commit()
    with dataBase.cursor() as cursor:
        sql = "SELECT name, date, experience FROM `mark_staff` WHERE `name`=%s"
        cursor.execute(sql, [username])
        result = cursor.fetchone()
        print('ОБНОВЛЕННАЯ ИНФОРМАЦИЯ О СОТРУДНИКЕ\n ФИО: ' + result[0] + ', дата рождения: ' + result[
            1] + ', опыт работы: ' + result[2] + '.')


def All(username):
    cursor = dataBase.cursor()
    new_name = input('Введите новое ФИО сотрудника:\n')
    sql = "UPDATE mark_staff SET name=%s WHERE name=%s"
    values = (new_name, username)
    cursor.execute(sql, values)
    dataBase.commit()

    cursor = dataBase.cursor()
    new_date = validate_date()
    sql = "UPDATE mark_staff SET date=%s WHERE name=%s"
    values = (new_date, [new_name])
    cursor.execute(sql, values)
    dataBase.commit()
    cursor = dataBase.cursor()
    new_date = input('Введите новый опыт работы сотрудника:\n')
    sql = "UPDATE mark_staff SET experience=%s WHERE name=%s"
    values = (new_date, [new_name])
    cursor.execute(sql, values)
    dataBase.commit()
    with dataBase.cursor() as cursor:
        sql = "SELECT name, date, experience FROM `mark_staff` WHERE `name`=%s"
        cursor.execute(sql, [new_name])
        result = cursor.fetchone()
        print('ОБНОВЛЕННАЯ ИНФОРМАЦИЯ О СОТРУДНИКЕ\n ФИО: ' + result[0] + ', дата рождения: ' + result[
            1] + ', опыт работы: ' + result[2] + '.')


def Experience(username):
    cursor = dataBase.cursor()
    new_experience = input('Введите новый опыт работы сотрудника:\n')
    sql = "UPDATE mark_staff SET experience=%s WHERE name=%s"
    values = (new_experience, username)
    cursor.execute(sql, values)
    dataBase.commit()
    with dataBase.cursor() as cursor:
        sql = "SELECT name, date, experience FROM `mark_staff` WHERE `name`=%s"
        cursor.execute(sql, [username])
        result = cursor.fetchone()
        print('ОБНОВЛЕННАЯ ИНФОРМАЦИЯ О СОТРУДНИКЕ\n ФИО: ' + result[0] + ', дата рождения: ' + result[
            1] + ', опыт работы: ' + result[2] + '.')


def Name(username):
    cursor = dataBase.cursor()
    new_name = input('Введите новое фио сотрудника:\n')
    sql = "UPDATE mark_staff SET name=%s WHERE name=%s"
    values = (new_name, username)
    cursor.execute(sql, values)
    dataBase.commit()
    with dataBase.cursor() as cursor:
        sql = "SELECT name, date, experience FROM `mark_staff` WHERE `name`=%s"
        cursor.execute(sql, [new_name])
        result = cursor.fetchone()
        print('ОБНОВЛЕННАЯ ИНФОРМАЦИЯ О СОТРУДНИКЕ\n ФИО: ' + result[0] + ', дата рождения: ' + result[
            1] + ', опыт работы: ' + result[2] + '.')


def Delete():
    cursor = dataBase.cursor()
    cursor.execute("SELECT name FROM mark_staff")
    for row in cursor.fetchall():
        print('ФИО: ' + row[0])
    worker = input("Введите ФИО из списка, которое хотите удалить: ")
    with dataBase.cursor() as cursor:
        sql = f"DELETE FROM `mark_staff` WHERE name = '{worker}'"
        cursor.execute(sql)
        dataBase.commit()
    print("Пользователь " + worker + " удалён...")


def Main():
    while True:
        s = input(
            "Введите команду для взаимодейтсвия с базой данных или введите '/help' для просмотра доступных команд: ")
        if s == '/help':
            print('http://localhost:8000/insert')
            print('http://localhost:8000/select')
            print('http://localhost:8000/update')
            print('http://localhost:8000/delete')
            print('/shutdown - остановка программы.')
        elif s == 'http://localhost:8000/insert':
            Insert()
        elif s == 'http://localhost:8000/select':
            Select()
        elif s == 'http://localhost:8000/update':
            Update()
        elif s == 'http://localhost:8000/delete':
            Delete()
        elif s == '/shutdown':
            break


Main()

# Закрываем соединение
dataBase.close()