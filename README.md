# bpidus_user
User service with Django

# How to run

1. `docker-compose up`

or

1. `docker build -t <image_name> .`

2. `docker exec -t -i <container_id> bash`

3. Run `python manage.py migrate`

3. `docker run -p 8000:8000 <image_name>`

# API Endpoints

## Sign up

- `POST /api/signup`

**Data example** 

All fields must be sent except **'gender'**

```json
curl --location --request POST 'http://127.0.0.1:8000/api/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
 "email":"sample@gmail.com",
 "password":"xxxxxxxx",
 "profile": {
        "name": "John",
        "nickname": "doe",
        "phone_number": "010-0000-0000",
        "email": "sample@gmail.com",
        "gender": "M" // (optional
 }
}'
```

**Response example** 

```json
{
    "message": "User registered  successfully"
}
```

## Sign in

- `POST /api/signin`

```json
curl --location --request POST 'http://127.0.0.1:8000/api/signin' \
--header 'Content-Type: application/json' \
--data-raw '{
 "email":"sample@gmail.com",
 "password":"xxxxxxxx"
}'

```

**Data example** All fields must be sent.

```json
{
    "message": "User logged in  successfully",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYTQwMGRhNjMtMzIyOC00ZTkxLWFiMDMtMjA0ZjJjMDgxM2UzIiwidXNlcm5hbWUiOiJyYW1AZ21haWwuY29tIiwiZXhwIjoxNTkwNjY4NzQzLCJlbWFpbCI6InJhbUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU4ODA3Njc0M30.Ys9A-fijKgd4jON5nG8yMc6QUhCTh3PieUb2_hYMWhw"
}
```

## Refresh token

- `POST /api/token/refresh`

Should have JWT token

```json
curl --location --request POST 'localhost:8000/api/token/refresh' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYTQwMGRhNjMtMzIyOC00ZTkxLWFiMDMtMjA0ZjJjMDgxM2UzIiwidXNlcm5hbWUiOiJyYW1AZ21haWwuY29tIiwiZXhwIjoxNTkwNjU3MzM2LCJlbWFpbCI6InJhbUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU4ODA2NTMzNn0.8khki13m-jLXaWXqqbHVW2sEZPF1GsqislkEH4DiQcI' \
```


**Response example** 

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYTQwMGRhNjMtMzIyOC00ZTkxLWFiMDMtMjA0ZjJjMDgxM2UzIiwidXNlcm5hbWUiOiJyYW1AZ21haWwuY29tIiwiZXhwIjoxNTkwNjY4NTE2LCJlbWFpbCI6InJhbUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU4ODA2NTMzNn0.Jw4g3ggxVSCf2AyOxqB7XfhyRdI6hTWloXJZo8WRr6w"
}
```


## Get User info

- `GET /api/profiles/{profileId}`

**Response example** 

```json
{
    "name": "John",
    "nickname": "Doe",
    "phone_number": "010-0000-0000",
    "email": "sample@gmail.com",
    "gender": "M"
}
```



## Search user

- `GET /api/profiles/search`

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Sample",
            "nickname": "example",
            "phone_number": "010-0000-0000",
            "email": "ram@gmail.com",
            "gender": "M"
        },
        {
            "name": "Sample",
            "nickname": "Doe",
            "phone_number": "010-0000-0000",
            "email": "example3m@gmail.com",
            "gender": "M"
        }
    ]
}
```

## DB creation

CREATE TABLE "login" ("password" varchar(128) NOT NULL, "last_login" datetime NULL, "id" char(32) NOT NULL PRIMARY KEY, "email" varchar(100) NOT NULL UNIQUE, "is_active" bool NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL)

CREATE TABLE "profile" ("id" char(32) NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "nickname" varchar(50) NOT NULL, "email" varchar(100) NOT NULL UNIQUE, "phone_number" varchar(10) NOT NULL UNIQUE, "gender" varchar(1) NOT NULL, "user_id" char(32) NOT NULL UNIQUE REFERENCES "login" ("id") DEFERRABLE INITIALLY DEFERRED)