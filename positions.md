## Должности
`GET /positions`

### Формат ответа
```
{
    "name": "Название вакансии по штатке",
    "code": "position_shtat",
    "items": [
        {
            "name": "name1",
            "foreign": "1"
        },
        {
            "name": "name2",
            "foreign": "2"
        },
        {
            "name": "name3",
            "foreign": "3"
        }
}
```
Имя | Тип | Описание
 --- | --- | ---
 name |  string | Название должности
 foreign |  string | Ключ в источниках Контура
