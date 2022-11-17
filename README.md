## Установка
####  Создать окружение

#### Склонировать репозиторий с GitHub
```shell
git clone https://github.com/EASidorov/StripeInteraction.git
```

#### Установить зависимости:
```shell
pip install -r requirements.txt
```

#### Создать env
```shell
touch /api/.env 
touch /StripeInteraction/.env
```

#### /api/.env
```shell
STRIPE_KEY='ваш ключ от Stripe API'
```
#### /StripeInteraction.env
```shell
SECRET_KEY='ваш джанго секретный ключ'
```
#### Мигрировать базы данных:
```shell
python manage.py makemigrations
python manage.py migrate
```
#### Запустить:
```shell
python manage.py runserver
```


## Структура
Создание и удаление моделей через панель админа<br>
Доступные модели: *Товар, Заказ, Налог\*, Скидка\**
```
/admin
```
Список всех Товаров
```
/
```
Детальная страница на созданные Товары
```
/item/$id
```
Реализация обращения к StripeAPI
```
/buy/$id
```
