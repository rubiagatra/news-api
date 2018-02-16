# Get, Update, and Delete News by id

## Get News by id

**URL** : `/api/news/<int:id>`

**Method** : `GET`

**Auth required** : YES 

Not Found Response

**Condition** : User can not see any News.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "news": "News not found"
} 
```
Success Response

**Condition** : User can see one News.

**Code** : `200 OK`

**Content** : 

```json
{
    "news": {
        "id": 25,
        "topic": "car",
        "status": "publish",
        "title": "New Car Released this Month"
    }
}
```

Error Response

**Condition** : If Token is Expired.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Signature has expired",
    "error": "Invalid token",
    "status_code": 401
}    

```
**Condition** : If there is not access token.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Request does not contain an access token",
    "error": "Authorization Required",
    "status_code": 401
}    

```
## Update A News 

Update a news with title,status, and topic.

**URL** : `/api/news/<int:id>`

**Method** : `PUT`

**Auth required** : YES

**Data constraints**

```json
{
    "status": "[Status of the news draft/publish]",
    "topic": "[Name or your topic can be more than one]",
    "title": "[Name of your title]"
}
```

**Data Example**

```json
{
    "status": "draft",
    "topic": "car",
    "title": "Tesla is the best car right now"
}
```
OR

```json
{
    "status": "publish",
    "topic": ["car", "auto"],
    "title": "Tesla is the best car right now"
}
```
Success Response

**Code** : `200 OK` 

**Content example**

```json
{
    "news": {
        "id": 25,
        "topic": "car",
        "status": "publish",
        "title": "Updated, Tesla New Car Released this Month"
    }
}
```

Error Response

**Condition** : If Token is Expired.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Signature has expired",
    "error": "Invalid token",
    "status_code": 401
}    

```
**Condition** : If there is not access token.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Request does not contain an access token",
    "error": "Authorization Required",
    "status_code": 401
}    

```
## Delete News by id

**URL** : `/api/news/<int:id>`

**Method** : `DELETE`

**Auth required** : YES 

Not Found Response

**Condition** : User can not see any News.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "news": "News not found"
} 
```
Success Response

**Condition** : User deleted news.

**Code** : `200 OK`

**Content** : 

```json
{
    "news": {"News was deleted"}
}
```

Error Response

**Condition** : If Token is Expired.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Signature has expired",
    "error": "Invalid token",
    "status_code": 401
}    

```
**Condition** : If there is not access token.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{
    "description": "Request does not contain an access token",
    "error": "Authorization Required",
    "status_code": 401
}    

```