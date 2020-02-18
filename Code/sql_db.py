import sqlite3

conn = sqlite3.connect('DB\\fantasy-cricket.db')
c = conn.cursor()

def create_tabel():
    c.execute('''CREATE TABLE IF NOT EXISTS fantasy(player text,
                                                    scored integer,
                                                    faced integer,
                                                    fours integer,
                                                    sixes integer,
                                                    bowled integer,
                                                    maiden integer,
                                                    given integer,
                                                    wkts integer,
                                                    catches integer,
                                                    stumping integer,
                                                    ro integer,
                                                    value integer,
                                                    matches integer,
                                                    runs integer,
                                                    hundreds integer,
                                                    fifty integer,
                                                    ctg text)''')

def dynamic_entry():
    c.execute("INSERT INTO fantasy VALUES('Kohli',102	,98,	8,	2,	0,	0,	0,	0,	0,	0,	1,	120,	  189,	8257,	28,	43, 'BAT')") 

def fetch_data():
    c.execute("SELECT * FROM fantasy")
    out = c.fetchall()
    for row in out:
        print(row[0])
    # print(c.fetchall())
# create_tabel()
# dynamic_entry()
fetch_data()



