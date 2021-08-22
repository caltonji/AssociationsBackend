# AssociationsBackend

### Running Locally

1. `git clone https://github.com/caltonji/AssociationsBackend.git`
2. `cd AssociationsBackend`
3. `conda create --name associations_env --file requirements.txt`
4. `conda activate associations_env`
5. `export FLASK_APP=application`
6. `flask run`

### Deploying

1. `az login`
2. `az account set --subscription "Visual Studio Enterprise Subscription"`
3. `az webapp up --sku B3 --name "AssociationsBackendB1"`

Deployed publicly at https://associationsbackendb1.azurewebsites.net (Last deployed 7/25/21. No active maintenance.)

# API Documentation

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