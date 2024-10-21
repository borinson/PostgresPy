import psycopg2

sender = input("Введите ID отправителя: ")
receiver = input("Введите ID получателя: ")
msg = input("Сообщение: ")

try:
    connection = psycopg2.connect(
        dbname = 'test_db',
        user = 'postgres',
        password = '123',
        host = 'localhost',
        port = '5432'
    )
    cursor = connection.cursor()
    print("Соединение с БД успешно установлено")

    # Удаление
    # data = (receiver, )
    # cursor.execute("DELETE FROM messages WHERE user_receiver_id = %s", data)
    # connection.commit()
    # Изменение
    # data = (sender, receiver, msg)
    # cursor.execute("UPDATE messages SET user_sender_id = %s, user_receiver_id = %s, text = %s WHERE id = 1", data)
    # connection.commit()
    # Чтение
    cursor.execute("SELECT id, user_sender_id, user_receiver_id, text, edited FROM messages")
    rows = cursor.fetchall()
    for row in rows:
        print("id", "user_sender_id", "user_receiver_id", "text", "edited")
        print(row[0], row[1], row[2], row[3], row[4])
    # Вставка
    # data = (sender, receiver, msg)
    # cursor.execute(f"INSERT INTO messages (user_sender_id, user_receiver_id, text) VALUES (%s, %s, %s)", data)
    # connection.commit()

except Exception as e:
    print(f"Ошибка: {e}")