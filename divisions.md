## Подразделения
`GET /divisions`

### Формат ответа
```
{
    "items": [
        {
            "name": "name1",
            "foreign": "1",
            "items": [
                {
                    "name": "name2",
                    "foreign": "2",
                    "items": [
                        {
                            "name": "name3",
                            "foreign": "3",
                            "items": []
                        },
                        {
                            "name": "name4",
                            "foreign": "4",
                            "items": []
                        }                        
                    ]
                },
                {
                    "name": "name5",
                    "foreign": "5",
                    "items": []
                }         
          }
     ]         
}
               
```
Имя | Тип | Описание
 --- | --- | ---
 name |  string | Название подразделения
 foreign | string | Ключ в источниках Контура
 items | string | Дочерние подразделения
