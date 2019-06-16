import psycopg2    # импортировали модуль psycopg2

from relational_database.config import DATABASE    # из файла config импортировали словарь с конфигурацией БД

conn = psycopg2.connect(**DATABASE)   # устанавливаем соединение передаем раскрытый словарь с конфигурацией БД

with conn.cursor() as cursor:     # создаем менедждер контекста с курсором. Гарантированное закрытие соединения.

    cursor.execute('''SELECT * 
                      FROM Customers
                      WHERE CustomerID IN (3, 91, 92);     
                      ''')              # метод execute для выполнения запросов
    print(cursor.fetchall())           # fetchall вызывает результат запрос из курсоа, print-вывод результата на экран
                                    # результать -  список кортежей
