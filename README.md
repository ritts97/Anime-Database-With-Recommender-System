# Anime-Database-With-Recommender-System

This project was done as a class project for the course 'Database Management System'. This is a command line app of an anime database which uses SQLite and Python. It contains anime details and a personal anime recommendation system which recommends anime using pearson correlation coefficient and user-to-user collaborative filtering. Users can sign up and view anime details like the summary, genres, creators, age limit and the number of episodes, rate and unrate animes and update their personal details. The recommender system recommends anime based their ratings. The admin(s) can view user details and add animes to the database. It also uses Google's SMTP server to send emails to the users to reset their password in case they forget their current password.

REQUIREMENTS :-
Python 3

HOW TO RUN THE PROJECT :-
1. Clone the repository.
2. Make sure the 'out.csv' and 'animedatabase.db' files are in the same directory as the 'animedbapp.py' file.
3. Open the animedbapp.py file and make the necessary changes which are mentioned in the comments of the file. You need to add your gmail address and password wherever specified to connect to Google's SMTP services to send mails through the app.
4. Run the python file. If using terminal, run the command "python animedbapp.py".
