import psycopg2    # импортировали модуль psycopg2

from relational_database.config import DATABASE    # из файла config импортировали словарь с конфигурацией БД

conn = psycopg2.connect(**DATABASE)   # устанавливаем соединение передаем раскрытый словарь с конфигурацией БД

with conn.cursor() as cursor:     # создаем менедждер контекста с курсором. Гарантированное закрытие соединения.

    cursor.execute("SELECT * FROM Customers")  # метод execute для выполнения запросов
    for result in cursor.fetchall():          # fetchall вызывает результат запрос из курсора в виде списка кортежей
        print(result)                        # итеруемся по списку кортежей и каждй кортеж выводим в виде отд. строки.
