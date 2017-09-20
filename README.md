Steps to run the application:

1. Create virtual environment using command
   virtualenv venv

2. Activate the virtual environment using command
   source venv/bin/activate

3. Install the requirements in virtual environment using command
   pip install -r requirements.txt

4. Migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Load dummy data using command
   python manage.py loaddetails

6. Start the server using command
   python manage.py runserver


Users:

username - test_user1, password - password11
username - test_user2, password - password22
username - test_user2, password - password33

tanant - Tenant1 api-key - 3c1a5d88ac914da6a92e860789453779
tenant - Tenant2 api-key - 23cb00a63d7945eba0ff5b846de1b728


apis:

1. Get access token

   url - /api-token-auth/
   method - POST
   params - username, password - Pass these parameters in body eg. {"username" : "test_user1", "password" : "password11"}


2. Get questions

   url - api/questions
   method - GET
   headers - token, api-key - pass these parameters in header section
   params - q (optional)