# About

Directory about sample Flask functions.

# Sample Usage

## Basic Usage

### Preparetion

`pip install flask`

### Usage

```
➜  python -m flask --app index run
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## Docker

### Preparetion

`docker build -t py_flask .`

- py_flask ... Example image ID

### Usage

```
➜  docker run -p 5000:5000 py_flask
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
...
```

## Docker Compose

### Preparetion

`docker compose build`

### Usage

`docker compose up`
