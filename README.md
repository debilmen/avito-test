Стек: Sanic, Postgresql, marshmallow, SQLAlchemy
Запуск: 
Качаем
Настраиваем .env(

POSTGRES_DB = <название_для_DB>
POSTGRES_USER = <имя_пользователя>
POSTGRES_PASSWORD = <пароль>
POSTGRES_HOST = <имя_хоста>
POSTGRES_PORT = <порт>
host = 0.0.0.0
) 
А потом вот так: docker-compose up
