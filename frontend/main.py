from nicegui.ui import page, run
from pages import sign_up
from pages import sign_up_candidate
from pages import sign_up_company
from pages import home
from nicegui import app

app.add_static_files(url_path = '/css', local_directory = './css')

@page(path = '/')
def main():
    pass

run(dark = True)