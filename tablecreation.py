#This file creates the tables of the database. Contains 7 tables.

import sqlite3

#Connecting to the database
conn = sqlite3.connect('animedatabase.db')

#Table 'anime_details' contains the details of the anime like anime ID, anime name, number of episodes, age limit and summary.
conn.execute('''CREATE TABLE anime_details(animeid INT PRIMARY KEY, animename TEXT NOT NULL, noofeps INT, agelimit INT CHECK(agelimit >= 0), summary TEXT);''')

#Table 'user' contains the details of the user like user ID, user name and location of the user.
conn.execute('''CREATE TABLE user(userid INT PRIMARY KEY, username TEXT NOT NULL location TEXT);''')

#Table 'user_ratings' contains the user ID, anime ID and the user's rating for the given anime.
conn.execute('''CREATE TABLE user_ratings(userid INT NOT NULL, animeid INT NOT NULL, rating NUMERIC CHECK(rating >= 0 AND rating <= 5), PRIMARY KEY(userid, animeid), CONSTRAINT fk1 FOREIGN KEY(userid) REFERENCES user(userid), CONSTRAINT fk2 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')

#Table 'admin' contains the admin details like admin ID, email address and password.
conn.execute('''CREATE TABLE admin(adminid INT PRIMARY KEY, adminemail TEXT NOT NULL,  adminpassword TEXT NOT NULL);''')

#Table 'login_info' contains the login information of the users like user ID, email address and password.
conn.execute('''CREATE TABLE login_info(userid INT NOT NULL, emailid TEXT PRIMARY KEY, password TEXT NOT NULL, CONSTRAINT fk3 FOREIGN KEY(userid) REFERENCES user(userid));''')

#Table 'genre' contains the genres of each anime. An anime can have multiple genres. It contains genre name and anime ID.
conn.execute('''CREATE TABLE genre(genrename TEXT, animeid INT, PRIMARY KEY(genrename, animeid), CONSTRAINT fk4 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')

#Table 'creators' contains the creators of the animes. An anime can have multiple creators and a creator can create multiple animes. It contains creator ID, creator name and anime ID.
conn.execute('''CREATE TABLE creators(creatorid INT NOT NULL, creatorname TEXT NOT NULL, animeid INT, PRIMARY KEY(creatorid, animeid), CONSTRAINT fk5 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')

conn.commit()
conn.close()
