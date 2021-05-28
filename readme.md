# TodoList

#### The cross-platform todo app is written in Python3 and use sqlite3 as database. Available for Windows, Linux and MacOS

### ScreenShot:

| Windows                                                      |
| ------------------------------------------------------------ |
| ![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/win_test.png) |

| Linux                                                        | Mac OS                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/linux_test.png) | ![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/macosx_test.png) |



### Features:

- Python as BackEnd, Html/CSS/JS as FrontEnd

- Small build size: 7.8 MB

- Available on any system (even without modern webview runtime - Ex: Win7 support)

  

### Download:

- Windows version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/windows/todo.exe) (If no webview found, then mshtml is used)

- Windows chromium embed version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/windows/todo_chromium.exe) (Not recommended)

- Linux version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/linux/todo) (WebKit rendering)

- MacOS version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/macosx/todo) (WebKit rendering)

  

### Run from source code:

1. Setup Git, Python3 (<=3.8), webview2 runtime (if use), cefpython3 module (if use)

2. Clone source: `git clone https://github.com/prozip/TodoList-serverless_app/`

3. Install requiments: `pip install -r requirements.txt`

4. Run with: `python src/start.py`

   

### How to build ?

 Check out PyInstaller





### Work flow:

![app_flow](https://github.com/prozip/TodoList-serverless_app/blob/master/image/app_flow.png)



