## Специализации
`GET /specializations`

### Формат ответа
```
{
    "code": "specialization",
    "name": "Специализация",
    "items": [
        {
          "foreign": "1",
          "name": "name1",
          "items": [
              {
                "foreign": "2",
                "name": "name2",
                "items": [
                    {
                      "foreign": "3",
                      "name": "name3",
                      "items": [
                          {
                            "foreign": "4",
                            "name": "name4"
                          },
                          {
                            "foreign": "5",
                            "name": "name5"
                          }
                       ]
                    }
                 ]
              }
           ]
        }
    ]
}
               
```
Имя | Тип | Описание
 --- | --- | ---
 name |  string | Название специализации
 foreign | string | Ключ в источниках Контура
 items | string | Дочерние специализации

