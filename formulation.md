# Задание: Callback API для управления резервированием товаров

## Формулировка
Разработать асинхронное API, используя Python, SQLAlchemy и один из фреймворков на выбор: 
AioHTTP или FastAPI. API должно принимать запросы от внешних сервисов (callback), 
обрабатывать их и обеспечивать корректное управление резервированием товаров на складе. 
Предоставить Docker Compose файл для развертывания сервиса вместе с 
базой данных PostgreSQL и выполнить анализ тестового покрытия проекта.

## Технические требования
1. Язык программирования: Python 3.8+.
2. Фреймворк: AioHTTP или FastAPI.
3. ORM: SQLAlchemy для работы с базой данных.
4. База данных: PostgreSQL.
5. Асинхронность: Код должен быть полностью асинхронным, все запросы к
базе данных и операции ввода/вывода должны выполняться асинхронно.
6. API:
   1. Метод для приема запросов на резервирование товаров.
   2. Метод для получения статуса резервирования.
7. Docker Compose: Создать docker-compose.yml файл для запуска сервиса и базы данных PostgreSQL.
8. Тестирование: Покрыть реализацию тестами с использованием фреймворка PyTest.
9. Логирование: Реализовать логирование всех запросов, действий и ошибок.
10. Анализ покрытия тестами: Сгенерировать отчет по покрытию кода тестами и включить его в проект.

## Описание
Внешний сервис отправляет запрос на резервирование определенного количества товаров на складе в формате JSON:
    
    POST /api/v1/reserve
    Content-Type: application/json
    {
    "reservation_id": Positiv number as string,
    "product_id": Positiv number as string,
    "quantity": Positiv int,
    "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
    }

### Алгоритм резервирования:
1. Проверить наличие достаточного количества товара на складе.
2. Если товара достаточно, уменьшить количество доступных единиц и
создать запись о резервировании. В противном случае корректно обработать ошибку
3. Вернуть статус операции.

Ответ в случае успеха:

    {
    "status": "success",
    "message": "Reservation completed successfully.",
    "reservation_id": Positiv number as string
    }

Ответ в случае ошибки: 

    {
    "status": "error",
    "message": "Not enough stock available.",
    "reservation_id": Positiv number as string
    }


### Примерная структура проекта
* app/ — директория с исходным кодом.
    * main.py — главный файл приложения.
    * models.py — описание моделей базы данных.
    * routes.py — описание маршрутов API.
    * db.py — конфигурация и подключение к базе данных.
* tests/ — директория с тестами.
* docker-compose.yml — файл конфигурации Docker Compose для запуска сервиса и базы данных PostgreSQL.
* requirements.txt — зависимости проекта


### Требования к тестам
* Тесты должны покрывать все основные методы API.
* Тестирование сценариев с успешным резервированием.
* Тестирование сценариев с ошибками (например, недостаточное количество товара).
* Дополнительные тесты, которые вы посчитаете необходимыми.
* Должны быть написаны на PyTest.

### Анализ покрытия тестами
* Использовать pytest-cov или аналогичный инструмент для анализа покрытия кода тестами.
* Сгенерировать отчет о покрытии в одном из следующих форматов: HTML, XML, или текстовом.

### Docker Compose
Файл docker-compose.yml должен:
* Запускать сервис API.
* Развертывать PostgreSQL базу данных.
* Запускать тесты.
* Генерировать отчет о тестовом покрытии и сохранять его на локальном устройстве

### Требования к сдаче задания
* Проект должен быть размещен в публичном репозитории на GitHub.
* В репозитории должен быть файл README.md с описанием:
  * Установки и запуска проекта с помощью Docker Compose.
  * Инструкции по запуску тестов и генерации отчета о покрытии.
* Все тесты должны успешно выполняться