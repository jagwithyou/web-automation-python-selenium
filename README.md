# automation_testing_with_python

This is a framework that will make your life easier in the field of automation testing. The goal of this framework is to making automation testing as easier as python that any one can learn and start using easily. your support will be highly appriciated in this process of making this as the easiest and effective framework in the field of automation testing. Please join us by contributing your inputs and giving this repo a star.  

https://user-images.githubusercontent.com/50165036/154853172-5a883d20-1fc3-4fbc-a4f8-7411dab2954c.mp4

#### Below are few useful features of this framework
- Modular Design.
- Report generation.
- Mailer to send the report.
- Events Log.
#### Prerequisite
- High learning sprit towards automation
- Basic knowledge in python

## Quick Start
- ##### Clone Framework
    <pre>
    git clone https://github.com/jagwithyou/automation-testing-python-selenium.git</pre>
- ##### Copy the web_ui_testing folder to your project location and open command prompt from there.
    
- ##### Create and activate virtual environment
    <pre>
    python -m venv ENVIRONMENT_NAME
    ENVIRONMENT_NAME\scripts\activate</pre>
- ##### Install required Python Packages
    <pre>
    pip install -r requirements.txt</pre>
- ##### Run the test
    <pre>
    pytest</pre>
- ##### Work on project
    Congratulations! framework is ready you can add new testcases now.

## Folder Structure
- web_ui_testing
    - Locators 
    - src
        - Drivers 
        - logs
        - Reports
        - Utility
    - Tests
    - Config.py
    - Conftest.py
 - api-testing
    - releasing soon

## Web UI Testing:
### Folder Description
**Driver**
- As selenium supports different drivers for different browsers, this folder contains the web drivers that we are going to use on our project.
    Ex:- For chrome browser:- chomedriver.exe

**Locators**
- Locator is the unique identifier for any element using which we can find the element. 
- Locators can be formed: 
    1) By X-path, 
    2) By CSS 
    3) By ID 
    4) By attribute

- Let's take a example of a submit button whose xpath is //button[@type='submit 
- The locator for the submit button will be:
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
 

**Logs**
- Contains the test execution logs

**Reports**
- Contains the test case execution report file after test case execution.

**Tests**
- Contains test cases 
- All the functionality and UI test cases should be created inside this folder
- For parallel test case execution all the test case prefix should be uniform.
- To test the user login create a test case as "test_user_login.py".


**Utility**
- this is the utility folder where you should keep your utilities. You can get a large collection of utilities from the [Utilities_repo](../../utilities)
 
**Config.py**
- A config.py (configuration) file contains all the settings that you can change as per your requirements.


**Conftest.py**
- conftest is the test configuration file for pytest using which we can change the way pytest is working. From adding the setup and teardown to every test case to import external plugins or modules we can configure these easily.


### How to work with this framework
Suppose you want to test the google search bar (which you have seen in the demo; you can relate the flow with the existing code to understand better).

#### **Step-1**
As we want to test google, the project url will be google.com. you have to assign this to the BASE_URL variable.
<pre>
BASE_URL = "https://www.google.com/"
</pre>

#### **Step-2**
Now we have to create a locator file for maintaining all the locators of a page. For a better use create individual locator files for each of the pages of your project. In our case we have created the locator file named google_homepage_locator and declared the locator inside this.
<pre>
from selenium.webdriver.common.by import By

SEARCH_BAR = (By.NAME, "q")
</pre>

#### **Step-3 - Perform the Action**
Now we are ready to write the test script. For that create a file inside tests folder and name it as test_FILENAME.py. As you can rightly guess each test script file should start with ***test_

Inside the script the code looks like below.
<pre>
from tests import BaseClass
from locator.google_homepage_locator import *
from selenium.webdriver.common.keys import Keys

class TestGooglePage(BaseClass):
    def test_1_search(self):
        ''' This is a test case to test the Google Search Page page. '''
        #Instantiating the logger
        self.log().info("Google Search Page Test Started")
        #accessing the search field and sending text to that
        self.get_element(SEARCH_BAR).send_keys('Automation Testing Python Selenium')
        self.get_element(SEARCH_BAR).send_keys(Keys.RETURN)
        #logging the test success
        self.log().info("Test Success")
        assert True

</pre>


As you can see first we have declared a class that is inherited from the BaseClass and inside it we are writing the test cases. you can assume this class as the ***TestSuite*** and each of the methods as the testcases inside the test-suite. you can write number of testcases inside this class. All the test cases should start as ***test_*** and they are executed alphabetically. so if you want any order of execution then please mention as ***test_1_***. You can give any number (1,2,3) and they will be executed with this order.

The next line is for log if you don't want log you can skip it. After that the operation starts. give your attention to the below three lines.

<pre>
#accessing the search field and sending text to that
self.get_element(SEARCH_BAR).send_keys('Automation Testing Python Selenium')
self.get_element(SEARCH_BAR).send_keys(Keys.RETURN)        
</pre>

1. self.get_element() - it is a method that takes the locator and return the element object to perform operation.
2. send_keys() - This sends some value to the object. Here it is sending the Text to the search bar of google. These are pytest derived methods and you can get the list from the pytest documentation. 
3. Keys.RETURN - It works like we are clicking the Enter Key after writing our query.

#### Step-4 - Running the script
We can run the complete testing by using the below command
<pre>
pytest
</pre>
If you want to run in a different browser then you can add one more argument here like below.
<pre>
pytest --browser_name firefox
</pre>

Awesome we have done this. Similarly you can follow step 2,3,4 to write automation for each of the field.
