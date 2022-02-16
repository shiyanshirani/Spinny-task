
# Spinny Backend Assignment


## Documentation

- [Postman Collection](https://documenter.getpostman.com/view/11525932/UVkiRJ5z)
## API Reference

#### Obtain Authentication Token
```http
  GET /api/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | Existing username|
| `password` | `string` | password|

#### List all boxes

```http
  GET /api/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | Open to Any |

#### CREATE box

```http
  POST /api/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :------------------------------- |
| `length`      | `int` |Length of the box |
| `breadth`      | `int` | Breadth of the box |
| `height`      | `int` |  Height of the box |
| `Token`      | `string` |  Authentication to POST |


#### List user's boxes

```http
  GET /api/users_box
```

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`      | `string` |Authentication |


#### Update specific box

```http
  PUT /api/<int:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Changes`      | `string/int` |Updated data|
| `Token`      | `string` |Authentication|


#### Delete specific box

```http
  DELETE /api/<int:pk>
```

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Box's User Token`      | `string` |Authentication|


#### List filtered boxes 
```http
  GET /api/list?length__gt=6&created_by=3&area__gt=3000
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `length__gt or length__lt`      | `int` |Length of the box |
| `breadth__gt or breadth__lt`      | `int` |Breadth of the box |
| `height__gt or height__gt`      | `int` |Height of the box |
## Run Locally

Clone the project

```bash
  git clone https://github.com/shiyanshirani/Spinny-task.git
```

Go to the project directory

```bash
  cd Spinny-task
```

Install dependencies

```bash
  pipenv install
```

Make migrations

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

```bash
  python3 manage.py createsuperuser (testing purposes)
```

Run server
```bash
  python3 manage.py runserver
```
## Environment Variables

To run this project, you will need to add the following `SECRET_KEY` variable to your .env file

`API_KEY` - .env file as an attachment in mail.



## Acknowledgements
 - [Design with developer empathy](https://apiguide.readthedocs.io/en/latest/principles/empathy.html#:~:text=Design%20with%20developer%20empathy&text=Perhaps%20the%20most%20important%20criteria,will%20remain%20undiscovered%20or%20unrealised)
 - [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Tech Stack

**Server:** Django, Django Rest Framework
