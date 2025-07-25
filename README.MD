# MEL-Random

**MEL-Random** — это веб-приложение на Flask с OAuth2-аутентификацией через Discord, позволяющее пользователям из белого списка запускать "спиннер" для случайного выбора футбольной команды или клуба из заданного списка. Каждая команда может выпасть только один раз, пока все варианты не закончатся.

---

## Что это?

- Веб-приложение с авторизацией через Discord OAuth2.
- Пользователи из заранее заданного белого списка могут использовать функционал.
- Есть "спиннер", который рандомно выбирает уникальный предмет (команду) из списка.
- Когда все команды выпали, история сбрасывается.
- Информацию о пользователе (аватар и имя) можно видеть в верхнем правом углу.
- Современный и адаптивный дизайн с анимациями, хорошо выглядит как на ПК, так и на мобильных устройствах.

---

## Основные технологии

- Python 3.11+
- Flask — веб-фреймворк
- Requests — для работы с OAuth2 Discord API
- Gunicorn — production-сервер для запуска приложения
- HTML, CSS — адаптивный дизайн с анимациями

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MEL-Random/MEL-Random-SRC.git
   cd MEL-Random
