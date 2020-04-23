# bpidus_user
User service with Django


# API Endpoints

## Sign up

- `POST /api/users`

**Data example** 

All fields must be sent except **'gender'**

```json
{
    "password" : "xxxxxxxx",
    "name": "[unicode 64 chars max]",
    "nickName": "[unicode 64 chars max]",
    "email": "sample@example.com",
    "phoneNumber":"000-0000-0000",
    "gender" : "male" // (optional)
}
```


## Sign in

- `POST /api/auth/signin`

**Data example** All fields must be sent.

```json
{
    "password" : "xxxxxxxx",
    "email": "sample@example.com"
}
```

## Sign out

- `GET /api/auth/signout`



## Get User info

- `POST /api/users/{userId}`


## Search user

- `GET /api/users/search`


