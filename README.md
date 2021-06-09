# Ghibli Tracker's API

This is the API for the first group project in Platzi Master. It is the backend for the Ghibli Tracker App, an ap that allows you to see the general details of all the films produced by Studio Ghibli including title, description, length in minutes, score in Rotten Tomatoes and more. The proyect will further develop knowledge in REST API's using Python, as well as the API testing using Postman.

The backend was built using Django 3.2.3. The reason to choose Django is that this framework works very well with realtional databases. As for now, it is using SQLite, the default database that is used when creating a new project with Django. The database that will be used in production will be MySQL. All the requirements can be found in the requirements.txt file.

To run the proyect, you can either clone the repository or download the .zip fle from github. As Django is a Python Framework, you need to have Python 3 installed. It is reccomended to start a virtual environment with the "python -m venv name" command in the Command Line Interface. after that, you can install the requirements needed using the "pip install -r requirements.txt" command, which will install the additional frameworks (django included) and libreries needed for the project.

Once you have successfully installed all requirements, you can run the project using the "python manage.py runserver" command, which will start a server in the url "127.0.0.1:8000". You can then access "127.0.0.1:8000/films" to have access to all the films in the database. This project is also abailable in Heroku https://masterghibli.herokuapp.com/

The site has the following routes:
  
https://masterghibli.herokuapp.com/admin a login page where you have access to tje data in the database and can modify, add, delete or create a user, film or rating
  
https://masterghibli.herokuapp.com/films where you can have access to the API for the films in a JSON format
  
https://masterghibli.herokuapp.com/profiles where you can have access to the users' information

https://masterghibli.herokuapp.com/ratings where you have access to all the ratings currently in the database. You can also filter the results using https://masterghibli.herokuapp.com/id:int where it will display the ratings for each user (each id is the user primary key). The assignment was requested by Erik Ochoa and bult by Luis Loaeza.
