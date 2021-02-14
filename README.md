Стек
=============
Sanic, Postgresql, marshmallow, SQLAlchemy

Запуск
=============
Качаем
***
Создаем и настраиваем `.env`

```
POSTGRES_DB = название_DB
POSTGRES_USER = имя_пользователя
POSTGRES_PASSWORD = пароль
POSTGRES_HOST = имя_хоста
POSTGRES_PORT = порт
host = 0.0.0.0
```
***
<p>docker-compose up</p>

Роуты
=============
  /ad "POST"
  ---------------
```
request: 
{  
        "name": str,https://github.com/debilmen/avito-test/issues
        "description": str,
        "photo": list,
        "price": int 
        }
response:
    {
        "id": int,
        "status_code": 201
        }
```   
/ad "GET"
-----------
 ```
request: 
{  
        "id": int,
        "Fields": bool, #optional
        }
response:
    {
        "name": str,
        "price": int,
        "photo": str,
         "all_photo": list #optional,
         "description": str
        }
 ```   
/ad/<page_n:int> "GET" <br/>
----------
Тут,указывается номер страницы начиная с 1. На каждой странице 10 объявлений. Есть сортировка по цене и дате создания. Если asscend'ы не указаны в request'e то сначала самые новые.
 ```
 request: 
{        
        "ascend_price": bool, #optional
        "ascend_date": bool, #optional
        }
response:
    [{
        "name": str,
        "price": int,
        "photo": str,
      },
       {
        "name": str,
        "price": int,
        "photo": str,
        "all_photo": list #optional,
        "description": str
        },
        ........
      ]
 ```   
