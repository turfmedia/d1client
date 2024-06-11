# D1Client

Simple D1 client class in Python.

## Installation

```sh
pip install d1client
```

## Usage

```python
  from d1client import D1Client

  client = D1Client(api_token='your_api_token', account_id='your_account_id', database_id='your_database_id')
  result = client.query_database('SELECT * FROM your_table')
  print(result)
```
