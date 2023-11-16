# rabidRestful
## setting up
1. Install fastapi
```bash
pip install fastapi==0.101.1
```
2. Ensure you have a Mysql Database

3. configure the db_config.py to setup your database configurations
```
user = ''
password = ''
host = ''
port = 
database_name = ''
```


## Introduction

This API provides functionality for managing posts. It allows users to perform operations such as retrieving, creating, updating, and deleting posts.

## Base URL

The base URL for this API is `/posts`.

## Authentication

This API uses OAuth2 authentication. Users need to obtain an access token by authenticating with the system.

## Endpoints
## POSTS
### 1. Get All Posts

#### `GET /posts/`

**Description:** Retrieve a list of all posts.

**Response:**
- Status Code: 200 OK
- Response Body: List of posts in JSON format.

### 2. Create a Post

#### `POST /posts/create_post`

**Description:** Create a new post.

**Request Body:**
- Content: JSON data containing post information.

**Response:**
- Status Code: 201 Created
- Response Body: Created post details in JSON format.

### 3. Get Latest Post

#### `GET /posts/latest`

**Description:** Retrieve the latest post.

**Response:**
- Status Code: 200 OK
- Response Body: Details of the latest post in JSON format.

### 4. Get a Specific Post

#### `GET /posts/{id}`

**Description:** Retrieve details of a specific post by providing its ID.

**Path Parameters:**
- `id` (integer): ID of the post.

**Response:**
- Status Code: 200 OK
- Response Body: Details of the specified post in JSON format.

### 5. Delete a Post

#### `DELETE /posts/{id}`

**Description:** Delete a specific post by providing its ID.

**Path Parameters:**
- `id` (integer): ID of the post.

**Response:**
- Status Code: 204 No Content

### 6. Update a Post

#### `PUT /posts/{id}`

**Description:** Update a specific post by providing its ID.

**Path Parameters:**
- `id` (integer): ID of the post.

**Request Body:**
- Content: JSON data containing updated post information.

**Response:**
- Status Code: 200 OK
- Response Body: Updated details of the post in JSON format.

## Examples

### 1. Retrieve All Posts

```bash
curl -X GET http://api-base-url/posts/
```
## USERS
## Endpoints

### 1. Create User

#### `POST /users/`

**Description:** Create a new user.

**Request Body:**
- Content: JSON data containing user information.

**Response:**
- Status Code: 201 Created
- Response Body: Created user details in JSON format.
### 2. Find User by ID

#### `GET /users/{id}`

**Description:** Retrieve details of a specific user by providing its ID.

**Path Parameters:**
- `id` (integer): ID of the user.

**Response:**
- Status Code: 200 OK
- Response Body: Details of the specified user in JSON format.
## Examples

### 1. Create a New User

```bash
curl -X POST -d '{"username": "newuser", "password": "securepassword", "email": "newuser@example.com"}' http://api-base-url/users/
```
## LOGIN
## Endpoints

### 1. User Login

#### `POST /auth/login`

**Description:** Authenticate a user and generate an access token.

**Request Body:**
- Content: Form data containing user email and password.

**Response:**
- Status Code: 200 OK
- Response Body: JSON object containing an access token and token type.

### Examples

#### 1. User Login

```bash
curl -X POST -d "username=user@example.com&password=securepassword" http://api-base-url/auth/login
```
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
  "token_type": "Bearer"
}
```


