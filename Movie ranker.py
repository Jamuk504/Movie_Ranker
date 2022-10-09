import PySimpleGUI as sg
import mysql.connector
from SQL_connection import mydb, mycursor


    
def window():
    mycursor.execute("SELECT * FROM movies")
    data = mycursor.fetchall()
    headings = ['ID', 'Name', 'Rating', 'Date']
    the_theme = {'BACKGROUND': '#605858',
                'TEXT': 'white',
                'INPUT': '#323131',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#2b90dc'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
    sg.theme_add_new('the_theme', the_theme)
    sg.theme('the_theme')
    font=('Consolas',16)
    layout= [ [sg.Text("Movie Ranker", font=('Consolas',35))],
              [sg.Text("Sort by:"), sg.Button("Name", key='Name', visible=False), sg.Button("Rating", key='Rating', visible=False), sg.Button("Date", key='Date', visible=False)],
              [sg.Table(values=data, headings=headings, key='Table')],
              [sg.Button("Filter", key='Filter'), sg.Exit()]]
    window = sg.Window("Movie Ranker", layout, modal=True)
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Filter':
            window['Name'].update(visible=True)
            window['Rating'].update(visible=True)
            window['Date'].update(visible=True)
        elif event == 'Name':
            mycursor.execute("SELECT * FROM movies ORDER BY Name")
            data=mycursor.fetchall()
            window['Table'].update(values=data)
        elif event == 'Rating':
            mycursor.execute("SELECT * FROM movies ORDER BY Rating")
            data=mycursor.fetchall()
            window['Table'].update(values=data)
        elif event == 'Date':
            mycursor.execute("SELECT * FROM movies ORDER BY Date")
            data=mycursor.fetchall()
            window['Table'].update(values=data)
window()
        
