# Filter News by Status 

## Get all News by Status 

**URL** : `/api/news/status/<string:status>`

**Method** : `GET`

**Auth required** : YES 

Not Found Response

**Condition** : User can not see any News by status.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "draft": "news with draft status was not found"
} 
```
OR

**Condition** : User can see one or more News by topic.

**Code** : `200 OK`

**Content** : 

```json
{
    "publish": [
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