MyMusic Maestro
===============

Instructions for Testing 
------------------------

1. python3 manage.py compilescss, to compile any SASS files you may have. This is optional and carries no marks; you do not need to use SASS unless desired.
2. python3 manage.py compilemessages, to generate localisation strings.
3. python3 manage.py makemigrations, in case required migrations were not supplied.
4. python3 manage.py migrate, to perform the migrations to the local database.
5. python3 manage.py seed, to insert your sample data into the database.
6. python3 manage.py test, to run your tests.
7. python3 manage.py runserver, to run your web application.

Write here any extra instructions or notes for marking.

Put any extra requirements in requirements.txt.

Structure
---------

Project structure is as follows:
1. /MyMusicMaestro -- configuration directory for project
2. /templates -- project-wide shared templates
3. /static -- project-wide shared static resources
4. /locale -- project-wide string localisation
5. /media -- user-uploaded file directory
6. /app_pages -- pages sub-app for public pages, e.g., landing page, help page, about page
7. /app_album_viewer -- viewer/editor sub-app for album management functionality

The sub-apps have the following nested structure:
1. /app_NAME/locale/ -- translations specific to the sub-app
2. /app_NAME/migrations/ -- migrations specific to the sub-app, if applicable
3. /app_NAME/templates/ -- view templates specific to the sub-app
4. /app_NAME/[apps,urls,models,views,tests,admin].py -- Django setup and code for each sub-app


Credits
-------

Album icons from Openclipart.
