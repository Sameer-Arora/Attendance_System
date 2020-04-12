# Attendance System

Please clone and push into the development branch only

To clone :- git clone https://github.com/Sameer-Arora/Attendance_System.git

To move to developement branch :- git checkout development

Set your origin as this repository (If repository not cloned):- git remote add origin https://github.com/Sameer-Arora/Attendance_System.git

To push :- git push origin development

## Decoupled The Environment Variables

Just rename the .env.example file to .env and change the database and other environment settings accordingly. 

## Django Basics 

TO INTEGRATE Djnago with Database intially update the database settings as given in .env.example file.Then run following :- 
```
$ python manage.py makemigrations <app_name>
$ python manage.py migrate
```

TO test the backend server
```
python manage.py runserver
```

TO run the backend shell for experimenting with models 
```
python manage.py shell
```

Complete List of Other basic Stuff :- 

https://github.com/Sameer-Arora/django-cheat-sheet
