from backend import main
import webview
from backend.db import myDB

class Api:
    def __init__(self):
        myDB.initDB()

    def addItem(self, task, taskDescriptionText, taskDescriptionInnerHTML,textDelta, time, myclass):
        return myDB.addItem(task, taskDescriptionText, taskDescriptionInnerHTML,textDelta, time, myclass)

    def editItem(self, id, task, taskDescriptionText, taskDescriptionInnerHTML,textDelta, time):
        myDB.editItem(id, task, taskDescriptionText, taskDescriptionInnerHTML,textDelta, time)
    
    def updateItemClass(self, id, className):
        myDB.updateItemClass(id, className)

    def updateItemPrio(self, id, prio):
        myDB.updateItemPrio(id, prio)

    def removeItem(self, id):
        myDB.removeItem(id)
    
    def test(self):
        print('run')

def backend(window):
    main.run(window)

def on_closing():
    myDB.commit()
    print('closed')

if __name__=='__main__':


    api = Api()
    window = webview.create_window('Todo List', './frontend/index.html', js_api=api, min_size=(1050,650), height=650, width=1050)
    window.closing += on_closing

    # webview2 version
    webview.start(backend, window)

    # chromium verison
    # webview.start(backend, window, gui='cef')
