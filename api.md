### Описание API

##### Routes API:

###### Работа со списком: `/api/routes/?limit=3` 
Методы: `GET`, `POST`

Пагинация через limit/offset

**GET отдаёт**:

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 4,
    "next": "http://127.0.0.1:8000/api/routes/?limit=3&offset=3",
    "previous": null,
    "results": [{...}, {...}, {...}]
}
```

**Пример result**:
```
{
    "id": 11,
    "name": "Заезд по миру",
    "route_type": 2,
    "short_desc": "Lorem ipsum ...",
    "long_desc": "Lorem ipsum ...",
    "location": 22,
    "duration": 4,
    "length": 23.0,
    "complexity": 2,
    "featured_photo": "http://127.0.0.1:8000/static/img/pexels-pixabay-460621_PIoOurT.jpg",
}
```

###### Работа с элементом: `/api/routes/<N>/`
Методы: GET, PUT, PATCH, DELETE

**GET отдаёт** (пример для `/api/routes/1/`):
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "name": "Путешествие в историю",
    "route_type": 2,
    "short_desc": "Lorem ipsum ...",
    "long_desc": "Lorem ipsum ...",
    "location": 22,
    "duration": 3,
    "length": 40.0,
    "complexity": 3,
    "featured_photo": "https://damp-reef-45123.herokuapp.com/static/img/pexels-kaique-rocha-775201_h8QHdL7.jpg",
    "trips": [1, 2],
    "photos": [
        {
            "id": 33,
            "url": "http://127.0.0.1:8000/static/route_photos/pexels-mali-maeder-109391_j6WNCS6.jpg"
        },
        {
            "id": 34,
            "url": "http://127.0.0.1:8000/static/route_photos/pexels-david-bartus-2415927_uyoNffR.jpg"
        },
        {
            "id": 36,
            "url": "http://127.0.0.1:8000/static/route_photos/opera_2021-03-26_13-47-43_1LDo9qj.jpg"
        }
    ]
}
```

##### Trips API

###### Работа со списком: `/api/trips/?limit=3`
Методы: `GET`, `POST`

Пагинация через limit/offset

**GET отдаёт**:
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 4,
    "next": "https://damp-reef-45123.herokuapp.com/api/trips/?limit=3&offset=3",
    "previous": null,
    "results": [{...}, {...}, {...}]
}
```

**Пример result**:
```
{
    "id": 1,
    "route": 1,
    "price": "11000.00",
    "starts_at": "2021-05-01T10:00:00+03:00",
    "ends_at": "2021-05-03T10:00:00+03:00",
    "instructor": 1,
    "kids": 0,
    "adults": 0,
    "max_group_size": 20,
    "options": [
        1,
        3
    ]
}
```

###### GET с фильтрами
Параметры фильтров:

Поля модели Trip

- `min_price` - минимальная цена
- `max_price` - максимальная цена
- `starts_after` - отправление после (даты). Формат - "YYYY-MM-DD"
- `ends_before` - возвращение до (даты) 

_(также есть `starts_before` и `ends_after`, но, подозреваю, они менее используемы)_
- `instructor` - инструктор (id)
- `route` - маршрут (id)

Поля модели Trip.Route (фильтрация походов по маршруту)

- `region` - регион маршрута
- `district` - округ маршрута
- `route_type` - тип маршрута (int enum от 1 до 6): Пеший, Велосипедный, Водный, Автомобильный, Лыжный, Горный
- `complexity` - сложность маршрута (int enum от 1 до 5): Простой, Обычный, Продвинутый, Сложный, Экстремальный, Горный
- `min_duration` - минимальная продолжительность
- `max_duration` - максимальная продолжительность

Пример: `/api/trips/?max_price=10000&starts_after=2021-04-01&ends_before=2021-07-01&instructor=2`
(Цена до 10000, проходит в интервале от 1 апреля до 1 июля, проводит гид с id=2)

_возвращает аналогично - список в описанном формате_

###### Работа с элементом: `/api/trips/<N>/`
Методы: GET, PUT, PATCH, DELETE

**GET отдаёт** (пример для `/api/trips/1/`):
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "route": 1,
    "price": "11000.00",
    "starts_at": "2021-05-01T10:00:00+03:00",
    "ends_at": "2021-05-03T10:00:00+03:00",
    "instructor": 1,
    "kids": 0,
    "adults": 0,
    "max_group_size": 20,
    "options": [
        1,
        3
    ]
}
```

##### TripComments API

###### Работа со списком: `/api/comments/`
Методы: `GET`, `POST`

Пагинация через limit/offset

**GET отдаёт**:
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [{...}, {...}, {...}]
}
```

**Пример result**:
```
{
    "id": 2,
    "author": 1,
    "content": "Вышло весьма неплохо, хорошая работа!",
    "added_at": "2021-03-04T16:41:17.120000+03:00",
    "trip": 3,
    "score": 4
},
```

###### Работа с элементом: `/api/comments/<N>/`
Методы: GET, PUT, PATCH, DELETE

**GET отдаёт** (пример для `/api/comments/3/`):
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "author": 1,
    "content": "asdasd",
    "added_at": "2021-03-23T16:25:34.957830+03:00",
    "trip": 3,
    "score": 3,
    "photos": [
        {
            "id": 3,
            "url": "http://127.0.0.1:8000/static/comment_media/pexels-pixabay-460621.jpg"
        },
        {
            "id": 4,
            "url": "http://127.0.0.1:8000/static/comment_media/pexels-andr%C3%A9-cook-131723.jpg"
        },
        {
            "id": 5,
            "url": "http://127.0.0.1:8000/static/comment_media/pexels-pixabay-266436_rJojJ3k.jpg"
        }
    ]
}
```

##### Orders API

###### Работа со списком: `/api/orders/`
Методы: `GET`, `POST`

Пагинация через limit/offset

На данный момент выдаёт только релевантные юзеру OrderItem's (для юзера - его брони, для инструктора - брони к его походам) 

**GET отдаёт**:
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [{...}, {...}]
}
```

**Пример result**:
```
{
    "id": 1,
    "traveler": 1,
    "trip": 3,
    "adults_amount": 1,
    "kids_amount": 2,
    "options_used": [
        1
    ],
    "contact_phone": "+7(000)000-0000",
    "contact_email": "geekpython@mail.ru",
    "notes": "побыстрее бы!"
}
```

(GET одиночной брони на данный момент аналогичен)