class SQLiteDatabase:
    def connect(self):
        print("Соединение с БД sqlite")

    def get_users(self):
        print("Получение пользователей из базы данных через запрос")


class MongoDatabase:
    def connect(self):
        print("Соединение с БД MongoDatabase")

    def get_users(self):
        print("Получение пользователей из базы данных через NO SQL")


class Server:
    def get_users(self, db):
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print("Читаем конфигурацию")
    return MongoDatabase()


if __name__ == "__main__":
    server = Server()
    server.get_users(get_db_from_config())
