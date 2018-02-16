# Auth 

Used to collect a Token for a registered User.

**URL** : `/auth`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[username]",
    "password": "[password in plain text]"
}
```

**Data Demo**

```json
{
    "username": "demo",
    "password": "demo"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTg3Njg1NDcsImlhdCI6MTUxODc2ODI0NywibmJmIjoxNTE4NzY4MjQ3LCJpZGVudGl0eSI6MX0.bSNjfHhs5DwuFOJQVb22hIvrg6vrYuEHPejqCys2jjc"

}
```

## Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Invalid credentials",
    "error": "Bad Request",
    "status_code": 401
}

```