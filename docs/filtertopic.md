# Filter News by Topic 

## Get all News by Topic

**URL** : `/api/news/topic/<string:topic>`

**Method** : `GET`

**Auth required** : YES 

Not Found Response

**Condition** : User can not see any News by topic.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "agama": "topic was not found"
} 
```
OR

**Condition** : User can see one or more News by topic.

**Code** : `200 OK`

**Content** : 

```json
{
    "car": [
        {
            "_id": 25,
            "status": "publish",
            "topic": "car",
            "title": "New Car Released this Month"
        }
    ]
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