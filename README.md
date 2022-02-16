
# Spinny Backend Assignment

A brief description of what this project does and who it's for


## API Reference

#### List all boxes

```http
  GET /api/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Open to Any |

#### CREATE box

```http
  POST /api/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `length`      | `int` | **Required**. Length of the box |
| `breadth`      | `int` | **Required**. Breadth of the box |
| `height`      | `int` | **Required**. Height of the box |
| `Token Authenthication`      | `string` | **Header**. Authentication to create |


#### List user's boxes

```http
  GET /api/users_box
```

| Authorization | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token Authenthication`      | `string` | **Required**. Id of item to fetch |


#### Get User's boxes

```http
  GET /api/users_box
```

| Authorization | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token Authenthication`      | `string` | **Required**. Id of item to fetch |


#### Get User's boxes

```http
  GET /api/<int:pk>
```

| Authorization | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token Authenthication`      | `string` | **Require**. Id of item to fetch |


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

## Documentation

- [Postman Collection](https://documenter.getpostman.com/view/11525932/UVkiRJ5z)
- d
