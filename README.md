# Project: Todo App
# 📁 Collection: Accounts 


## End-point: register
### Method: POST
>```
>http://127.0.0.1:8000/api/users/
>```
### Body (**raw**)

```json
{
    "email": "test@test.com",
    "first_name": "fulano",
    "last_name":"sutano",
    "password": "123456",
    "password_confirm": "123456"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: update user
### Method: PUT
>```
>http://127.0.0.1:8000/api/users/
>```
### Body (**raw**)

```json
{
    "email": "t2est@test.com",
    "first_name": "fulano2",
    "last_name":"sutano1"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTE3NjgyLCJpYXQiOjE2ODcwNTM2ODIsImp0aSI6IjEwZmRlYTQxYWYxZjQ0ZDU5ZTkyMDk2ZDI0ZmNhYzg5IiwidXNlcl9pZCI6M30.7HloSCh3uQz0Zs5Aq7sEEnKlIfDU9aPNd6xc1HTVjRI|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get user
### Method: GET
>```
>http://127.0.0.1:8000/api/users/4
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTE4NTE4LCJpYXQiOjE2ODcwNTQ1MTgsImp0aSI6ImIyZjFhMWI0M2VkYzQ0ODZiNDc2YmVkYjlhOGFiODBkIiwidXNlcl9pZCI6M30.uiAqpnawcQvxdJ2AimiTaQB-GpsX-zcMoOpqTwCagnU|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: delete user
### Method: DELETE
>```
>http://127.0.0.1:8000/api/users/
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTE4NTE4LCJpYXQiOjE2ODcwNTQ1MTgsImp0aSI6ImIyZjFhMWI0M2VkYzQ0ODZiNDc2YmVkYjlhOGFiODBkIiwidXNlcl9pZCI6M30.uiAqpnawcQvxdJ2AimiTaQB-GpsX-zcMoOpqTwCagnU|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: signin
### Method: POST
>```
>http://127.0.0.1:8000/api/users/signin
>```
### Body (**raw**)

```json
{
    "email":"test@test.com",
    "password": "123456"
}
```

### 🔑 Authentication noauth

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Todos 


## End-point: get todos user
### Method: GET
>```
>http://127.0.0.1:8000/api/todos
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTE0NjM2LCJpYXQiOjE2ODcwNTA2MzYsImp0aSI6IjFjNjhiYzY2YzBhMjRjM2FiYTY2MWE5Y2Y2MTRkN2M3IiwidXNlcl9pZCI6Mn0.tmJtPW9lzkoALukMgHLpZJ9HNg5SiJ2HK_cmyXIGsEQ|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: update todo
### Method: PUT
>```
>http://127.0.0.1:8000/api/todos
>```
### Body (**raw**)

```json
{
    "id": 2,
    "title": "testig",
    "detail": "optional",
    "is_completed": false
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTEyOTkxLCJpYXQiOjE2ODcwNDg5OTEsImp0aSI6ImI5M2RmNmJiOTRjMDQxM2RiMTk5YTY0OTBjMTM3OWFmIiwidXNlcl9pZCI6Mn0.icWOBszpw6nMQAjJABAYOuy2Fn2CaJDH3JsUlKMxRtA|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: create todo
### Method: POST
>```
>http://127.0.0.1:8000/api/todos
>```
### Body (**raw**)

```json
{
    "title": "testig",
    "detail": "optional",
    "is_completed": false
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTEyOTkxLCJpYXQiOjE2ODcwNDg5OTEsImp0aSI6ImI5M2RmNmJiOTRjMDQxM2RiMTk5YTY0OTBjMTM3OWFmIiwidXNlcl9pZCI6Mn0.icWOBszpw6nMQAjJABAYOuy2Fn2CaJDH3JsUlKMxRtA|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: delete todo
### Method: DELETE
>```
>http://127.0.0.1:8000/api/todos
>```
### Body (**raw**)

```json
{
    "id": 1
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTE1MzkxLCJpYXQiOjE2ODcwNTEzOTEsImp0aSI6IjQ5YmZiZjQ1ZWUyNDQ1ZjFhZTYzNzIxMjM4MDZlNWYwIiwidXNlcl9pZCI6Mn0.s_lfZk4Mq6O3TWThvpdddnB3uQgS2zmONdOtmM6Ckk0|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
