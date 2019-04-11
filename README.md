# API для получения справочников
Описание API для получения справочников.

У API 5 методов

1. divisions - Подразделения
2. projects - Проекты
3. education - Мероприятия
4. positions - Должности
5. specializations - Специализации


API предназначен для интеграции ATS Хантфлоу с внутренними ресурсами компании СКБ Контур в части работы с персоналом.

В сервисе используется Basic авторизация, логин и пароль будет получен по почте.

При Basic авторизации логин и пароль передаются в заголовке Authorization

`Authorization: Basic base64(логин:пароль)`
