# API для получения справочников
API предназначен для интеграции ATS Хантфлоу с внутренними ресурсами компании СКБ Контур в части работы с персоналом.

У API есть 5 методов без каких либо дополнительных параметров, все запросы передаются метотдом `GET`.

1. `/divisions` - Подразделения
2. `/projects` - Проекты
3. `/education` - Образовательыне мероприятия
4. `/positions` - Должности
5. `/specializations` - Специализации


Авторизация
Для авторизации в сервисе используется Basic авторизация.
При Basic авторизации логин и пароль передаются в заголовке Authorization в `base64`, логин и пароль будут получены по почте.

`Authorization: Basic base64(логин:пароль)`

При неудачной авторизации будет возвращен ответ 401

```
{
  unaccess authorization
}
```

Форматы ответа


## Подразделения `/divisions`

