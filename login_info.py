import sqlite3

conn = sqlite3.connect('/Users/ritwikaghosh/Projects/DBMSProject/animedatabase.db')

conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (107, 'ritwikaghosh48@gmail.com', 'Mritts97');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (100, 'yasharthp@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (101, 'vishesh@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (102, 'rishabha@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (103, 'suman@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (104, 'nikhil@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (105, 'abhishekg@gmail.com', 'password');")
conn.execute("INSERT INTO login_info(userid, emailid, password) VALUES (106, 'jagdesh@gmail.com', 'password');")

print("Done!");

conn.commit()
conn.close()
