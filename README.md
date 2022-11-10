# Решение тестового задания для gocloudcamp. 
Прошрамма написана на Python c использование стороних библиотек: fastapi, pydantic и sqlalchemy.
Для взаимодействия с api лучше использовать графический интерфейс `http://127.0.0.1:8000/docs`.

### Пример использования

#### Создание конфига

`curl -d "@data.json" -H "Content-Type: application/json" -X POST http://localhost:8000`

```json
{
    "service": "managed-k8s",
    "data": "random text"
}
```

#### Получение конфига

`curl http://127.0.0.1:8000/?id=1`

```json
{"service":"managed-k8s","id":1,"data":"random text"}
```