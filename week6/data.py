import sqlite3 
conn = sqlite3.connect (r'D:\Taksayapa_python\week6\data.db')
c = conn.cursor()

c.execute('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(30) NOT NULL,
    age varchar(30) NOT NULL)''')

c.execute('''INSERT INTO users (id,fname,lName,email,sex,age) VALUES (NULL,"Phattarapan" ,"Yoykartok", "Phattarapan.y@kkumail.com","femen","20")''')
c.execute('''INSERT INTO users (id,fname,lName,email,sex,age) VALUES (NULL,"Piamsuk" ,"Wathiroiram", "Piamsuk.Wathiroiram@kkumail.com",femen","19")''')
c.execute('''INSERT INTO users (id,fname,lName,email,sex,age) VALUES (NULL,"Taksayapa" ,"Tangwong", "tuksayapa.t@kkumail.com","femen","18")''')
conn.commit()
conn.close()