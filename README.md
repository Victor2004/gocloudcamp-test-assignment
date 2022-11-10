# Решение тестового задания для gocloudcamp. 
Прошрамма написана на Python c использование стороних библиотек: fastapi, pydantic и sqlalchemy.
Для взаимодействия с api лучше использовать графический интерфейс `http://127.0.0.1:8000/docs`.

### Пример использования

#### Создание конфига

```bash
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

```bash
curl 'http://127.0.0.1:8000/id?id=1'
```

```json
{"data":"value1","service":"managed-k8s","id":1}
```

#### Изменение конфига

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/id/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "service": "newtext",
  "data": "NEWdata"
}'
```

```json
{"data":"value1","service":"string","id":1}
```

#### Удаление конфига

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/id/1' \
  -H 'accept: application/json'
```

```json
"Config id=1 delete."
```


### Использование сервиса

##### По умолчанию сервис не использует ни какой конфиг, после запуска/перезапука программы требуется назначить конфиг который будет использовать сервис.

#### Изменить/назначить используемый сервисом конфиг

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/service/1' \
  -H 'accept: application/json'
```

```json
["Config update!",{"data":"value1","service":"managed-k8s","id":1}]
```

#### Получить содержимое всех конфигов

```bash
curl 'http://127.0.0.1:8000/service'
```

```json
[
  {
    "data": "value1",
    "service": "string",
    "id": 1
  },
  {
    "data": "value99",
    "service": "managed-k8s",
    "id": 2
  },
  {
    "data": "2011",
    "service": "managed-t9x0",
    "id": 3
  }
]
```