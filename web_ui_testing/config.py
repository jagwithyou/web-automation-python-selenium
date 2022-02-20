import os
BASE_DIRECTORY = os.getcwd()
BASE_URL = "https://www.google.com/"

#DRIVER
DRIVER_PATH = os.path.join(BASE_DIRECTORY, 'src', 'drivers') #use os.path.join to create a path
WEB_DRIVER_WAIT = 60
HEADLESS = False
ACTION_DELAY = 2
DOWNLOAD_WAIT_TIME = 60
DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY,'src', 'media','download')

#Reporting
REPORT_TITLE = "Orange HRM Testing"
REPORT_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'reports')
INDIVIDUAL_REPORT = False
LOG_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'logs')

