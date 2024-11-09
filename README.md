# Проект "YACUT"
Проект для укорачивания длинных ссылок.
Позволяет создать короткую ссылку на ресурс, задав уникальную часть короткой ссылки самостоятельно или сгенерирвать её автоматически.
## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:corbuncul/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл ".env" и прописать константы:
```
FLASK_APP={Ваше название приложения}
FLASK_DEBUG={Режим отладки (True/False)}
DATABASE_URI={Ваше подключение к базе данных (например: sqlite:///db.sqlite3)}
SECRET_KEY={Ваш секртный ключ (любая случайная строка)}
```
Применить миграции:
```
flask db upgrade
```
Запустить проект:
```
flask run
```
Проект будет доступен по адресу http://127.0.0.1:5000/