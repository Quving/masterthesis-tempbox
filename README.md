# Masterthesis-Tempbox

## Description
In the scope of my masterthesis which examine urban-heat-islands of Hamburg, Germany, I collect temperature data using different source (see Sources). The data, where each object is a measurement has the following data-structure:
```
{
    measurement_id:	string
    lat:	number
    lng:	number
    source:	string
    timezone:	string
    timestamp:	integer
    temperature:	number
    country:	string
    city:	string
    street:	string
    altitude:	integer
}
```

In order to perform queries on the large dataset, I use [Django REST Framework](https://www.django-rest-framework.org/) which is "a powerful and flexible toolkit for building Web APIs". To simplify the usage, a swagger documentation is also offered. My official endpoint can be found here: **https://tempbox.quving.com**


## Architecture
This Project (Tempbox) is only a box, where the data is stored. It is not adding or modifying data by itself.
- For this purpose, I created a sub-projects (e.g. [Netatmo-Crawler](https://github.com/Quving/masterthesis-netatmo-crawler)) which crawls every 15 mins using the Netamo-Api and fills the tempbox with data.

## Data Sources
- Netatmo
    - Docs: https://dev.netatmo.com/apidocumentation/weather



## Usage
### Authorization
The API is secured. Any read or write operation require authentication.

### How to get access?
First, ask the developer who maintains the API for access. The developer will create a user (username, password) which is required the for the furthersteps.


### API-Auth using JWT

#### Obtain the access_token and refresh_token
```bash
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  <api-host>/api/token/
```
Sample response

```json
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

#### Perform a authenticated request
```bash
curl \
  -X GET \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  <api-host>/measurements/
```

Sample Response:
```json
{
  "count": 16091,
  "next": "https://tempbox.quving.com/measurements/?limit=100&offset=100",
  "previous": null,
  "results": [
    {
      "id": 1,
      "measurement_id": "70:ee:50:03:da:4c",
      "lat": 53.523671999723,
      "lng": 10.1670769999999,
      "source": "netatmo",
      "timezone": "Europe/Berlin",
      "timestamp": 1640057384,
      "temperature": -2.8,
      "country": "DE",
      "city": "Oststeinbek",
      "street": "Dorfstraße",
      "altitude": 23
    },
    {
      "id": 2,
      "measurement_id": "70:ee:50:58:6c:b6",
      "lat": 53.5024223327637,
      "lng": 10.1748380661011,
      "source": "netatmo"
      ...

    }
   ]
  }
}
```

