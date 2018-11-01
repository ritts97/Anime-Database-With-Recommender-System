import sqlite3

conn = sqlite3.connect('/Users/ritwikaghosh/Projects/DBMSProject/animedatabase.db')

conn.execute('''CREATE TABLE anime_details(animeid INT PRIMARY KEY, animename TEXT NOT NULL, noofeps INT, agelimit INT CHECK(agelimit >= 0), summary TEXT);''')
conn.execute('''CREATE TABLE user(userid INT PRIMARY KEY, username TEXT NOT NULL location TEXT);''')
conn.execute('''CREATE TABLE user_ratings(userid INT NOT NULL, animeid INT NOT NULL, rating NUMERIC CHECK(rating >= 0 AND rating <= 5), PRIMARY KEY(userid, animeid), CONSTRAINT fk1 FOREIGN KEY(userid) REFERENCES user(userid), CONSTRAINT fk2 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')
conn.execute('''CREATE TABLE admin(adminid INT PRIMARY KEY, adminemail TEXT NOT NULL,  adminpassword TEXT NOT NULL);''')
conn.execute('''CREATE TABLE login_info(userid INT NOT NULL, emailid TEXT PRIMARY KEY, password TEXT NOT NULL, CONSTRAINT fk3 FOREIGN KEY(userid) REFERENCES user(userid));''')
conn.execute('''CREATE TABLE genre(genrename TEXT, animeid INT, PRIMARY KEY(genrename, animeid), CONSTRAINT fk4 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')
conn.execute('''CREATE TABLE creators(creatorid INT NOT NULL, creatorname TEXT NOT NULL, animeid INT, PRIMARY KEY(creatorid, animeid), CONSTRAINT fk5 FOREIGN KEY(animeid) REFERENCES anime_details(animeid));''')

conn.commit()
conn.close()
