import os
from time import sleep
from robocorp.tasks import task
from robocorp import browser

@task
def open_browser():
    local_app_data = os.environ.get('LOCALAPPDATA')
    browser.configure(
        persistent_context_directory=f"{local_app_data}\\Google\\Chrome\\User Data Assistant",
        headless=False
    )
    page = browser.page()
    page.goto("https://cloud.robocorp.com/")
    sleep(300)

