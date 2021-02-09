# API documentation
The repository contains an API made using Python with Flask technology and local database. It is related to the Frontend repository (https://github.com/MarBas97/EventMapsFront). 
## Launching the project
Download the project and to install all dependencies run

*pip install -r requirements.txt*

in the project folder.

Then create the initial migration:

*$ python manage.py create_db*

*$ python manage.py db init*

*$ python manage.py db migrate*

Launching the application:

*$ python manage.py runserver*

Running on *http://127.0.0.1:5000/*

## Endpoints description
| Address | Method | Input | Output |
| ------- | ------ | ----- | ------ |  
| '/api/register'| 'POST' | {email: "email", password: "password"} | Flag indicating whether user registered or not |
| '/api/login' | 'POST' | {email: "email", password: "password"} | Flag indicating whether user logged in or not |
| '/api/logout' | 'GET' | cookie | Informs that any user isn't logged in |
| '/api/getareapointers?long={long}&&lat={lat}'| 'GET' | {long},{lat} | List of all of the pointers nearby given latitude and longitude |
| '/api/getuserpointers?id={id}' | 'GET' | {id} | List of all of the pointers created by logged in user |
| '/api/addPointer' | 'POST' | {description:"description",longitude:"longitude",latitude: "latitude",created_by:"created_by"} | Flag indicating whether pointer added or not |
| '/api/addLike?user_id={user_id}&&id={id}' | 'PUT' | {user_id}, {id} | Flag indicating whether like added or not | 


