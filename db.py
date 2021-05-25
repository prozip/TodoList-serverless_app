import sqlite3
import time


class myDB:
    def __init__(self) -> None:
        pass

    @staticmethod
    def initDB():
        myDB.connect = sqlite3.connect('item.db', check_same_thread=False)
        myDB.cur = myDB.connect.cursor()
        myDB.cur.execute('''CREATE TABLE IF NOT EXISTS items
        (id integer PRIMARY KEY AUTOINCREMENT, task text,taskDescriptionText text, taskDescriptionInnerHTML text,textDelta text, time text, myclass text, prio text)''')

    @staticmethod
    def addItem(task, taskDescriptionText, taskDescriptionInnerHTML, textDelta, time, myclass):
        query = "INSERT INTO items VALUES (null,'" + task + "','" + taskDescriptionText + "','" + \
            taskDescriptionInnerHTML + "','" + textDelta + \
                "','" + time + "','" + myclass + "','" + 'dropdown-toggle primary' + "')"
        print('Added')
        myDB.cur.execute(query)
        return myDB.cur.lastrowid

    @staticmethod
    def updateItemClass(id, myclass):
        query = "UPDATE items SET myclass='" + myclass + "' WHERE id='" + id + "'"
        myDB.cur.execute(query)
        print(query)

    @staticmethod
    def editItem(id, task, taskDescriptionText, taskDescriptionInnerHTML, textDelta, time):
        query = "UPDATE items SET task='" + task + "', taskDescriptionText='" + \
            taskDescriptionText + "', taskDescriptionInnerHTML='" + \
                taskDescriptionInnerHTML + "', textDelta='" + \
            textDelta + "', time='" + time +"' WHERE id='" + id + "'"
        print(query)
        myDB.cur.execute(query)

    @staticmethod
    def updateItemPrio(id, prio):
        query = "UPDATE items SET prio='" + prio + "' WHERE id='" + id + "'"
        myDB.cur.execute(query)
        print(query)

    @staticmethod
    def removeItem(id):
        query = "DELETE FROM items WHERE id='" + id + "'"
        myDB.cur.execute(query)
        print(query)

    @staticmethod
    def initFetch(window):
        for row in myDB.cur.execute('SELECT * FROM items'):
            cmd = "addTask('" + str(row[0]) + "','" + row[1] + "','" + row[2] + \
                "','" + row[3] + "','" + row[4] + \
                "','" + row[5]+"','" + row[6]+"','" + row[7]+"')"
            window.evaluate_js(cmd)
        window.evaluate_js("clean()")

    @staticmethod
    def show():
        for row in myDB.cur.execute('SELECT * FROM items'):
            print(row)

    @staticmethod
    def commit():
        myDB.connect.commit()
