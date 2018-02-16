# News

## Get all Published News
Get all Published News from API.

**URL** : `/api/news`

**Method** : `GET`

**Auth required** : NO


Success Response

**Condition** : User can not see any News.

**Code** : `200 OK`

**Content** :
```json
{
    "published_news": []
} 
```
OR

**Condition** : User can see one or more News.

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
## Post A New News 

Post new news with title,status, and topic.

**URL** : `/api/news`

**Method** : `POST`

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

**Code** : `201 CREATED`

**Content example**

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

**Condition** : If the body missing one or more of entity.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "message": {
        "status": "status = 'draft' or 'publish'",
        "topic": "Please Insert Your Topic",
        "title": "Please enter your title"
    }
}    
```
