# Решение тестового задания для gocloudcamp. 
Прошрамма написана на Python c использование стороних библиотек: fastapi, pydantic и sqlalchemy.
Для взаимодействия с api лучше использовать графический интерфейс `http://127.0.0.1:8000/docs`.

### Пример использования

#### Создание конфига

```
curl -X 'POST' \
  'http://127.0.0.1:8000/id' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "service": "managed-k8s",
  "data": "value1"
}'
```

```json
{"data":"value1","service":"managed-k8s","id":1}
```

#### Получение конфига

`curl 'http://127.0.0.1:8000/id?id=1'`

```json
{"data":"value1","service":"managed-k8s","id":1}
```

### Использование сервиса

#### Изменить используемый сервисом config

```
curl -X 'PUT' \
  'http://127.0.0.1:8000/service/1' \
  -H 'accept: application/json'
```

```json
["Config update!",{"data":"value1","service":"managed-k8s","id":1}]
```

