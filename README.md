# Sky DNE – Python API Technical Exercise

Micro service app to fetch crypto currency market.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`user_name`

`password`


## Installation

Install Packages with pip

```bash
  pip install -r requirements.txt
```
    
## Deployment

To run this project run

```bash
  uvicorn app.main:app
```


## API Reference

#### Get market summaries

```http
  GET /api/exchange/bittrex
```

#### Get market symbol summary

```http
  GET /api/exchange/bittrex/${symbol}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `symbol`      | `string` | **Required**. symbol of market to fetch |



## Running Tests

To run tests, run the following command

```bash
  pytest
```

## Api Health check

```http
  GET /health
```

## API documentation

```http
  GET /redoc
```

