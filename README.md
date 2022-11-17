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
#### /sms_sender/.env
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
Управление клиентами<br>
*при создании Клиента создаются инстансы Оператор и Тег*
```
/client
```
Управление рассылками<br>
*при создании проверяется дата начала и происходит мгновенный или отложенный запуск*
```
/dispatch
```
Управление сообщениями
```
/message
```
Управление операторами
```
/oper
```
Управление тегами
```
/tags
```
