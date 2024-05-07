#Платформа торговой сети электроники
Описание:
API приложение с админ-панелью.

#Функционал:
Модели объекта торговой сети содержащей завод, розничную сеть, индивидуального предпринимателя имеют следующие поля:
контакт, продукт, поставщик, задолженность и дата создания.
В админ-панели доступен вывод созданных объектов.
На странице объекта сети добавлена ссылка на "Поставщика", фильтр по названию города и "admin action" для очистки задолженности перед поставщиком
Используя Django REST framework (DRF), создан набор представлений для CRUD операций с моделью поставщика, с фильтрацией по стране
Настроены права доступа к API, позволяющие доступ только активным сотрудникам.

#Стэк Технологии:
Python
Django
Django REST framework
psycopg2-binary
JWT
DRF-YASG


#Запуск проекта

Клонировать файлы проекта с GitHub репозитория:
Создать виртуальное окружение:
python -m venv venv
Активировать виртуальное окружение:
venv/Scripts/activate (Windows)
source venv/bin/activate (Linux, MacOS)
Установить зависимости:
pip install -r requirements.txt
Создать файл .env c переменными окружения, заполнить по аналогии с .env.sample.
Создайте базу данных, выполните python manage.py migrate.
Создайте администратора, выполните python manage.py csu.
Запустите сервер разработки, выполните python manage.py runserver. (Сервис запустится по адресу http://localhost:8000)
