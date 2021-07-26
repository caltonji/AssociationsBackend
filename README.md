# AssociationsBackend

## Setup

1. `git clone https://github.com/caltonji/AssociationsBackend.git`
2. `cd AssociationsBackend`
3. `conda create --name associations_env --file requirements.txt`
4. `export FLASK_APP=application`
5. `flask run`

## API Documentation

## Get Random Words

**URL** : `/random`

**Method** : `GET`

**URL Params**

**Required** : `count`

### Example Request

`GET /random?count=2`

```json
[
    "ball",
    "shareholders"
]
```

## Get Associated Word

**URL** : `/associations`

**Method** : `GET`

**URL Params**

`words` needs to be a comma seperated list.  The result will be a single word associated with all input words.  (only tested on input of 2 comma seperated words)

**Required** : `words`

### Example Request

`GET /associations?words=ball,shareholders`

```json
"contracts"
```