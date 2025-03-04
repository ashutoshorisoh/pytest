#any pytest file should start with test_ or end with _test (ex: test_first.py or first_test.py)
#every code should be wrapped in a function
#function in pytest also called as methods and it should start with "test"
#method name should have sense
#to run  all test cases at once, run "py.test" in cmd
#for detailed info run "py.test -v"
#for console logs run "py.test -v -s"
#to run all function related to credit card, lets say we named it commonly "CreditCard" then run "py.test -k CreditCard -v -s"
#to run specific file "py.test filename"
def test_firstprogram():
    print("hello")


#output log: C:\Users\ASHUTOSH\AppData\Local\Programs\Python\Python313\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2024.3.3/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path C:\Users\ASHUTOSH\Desktop\PyTest\pytestDemo\test_firstprogram.py
#Testing started at 09:02 ...
#Launching pytest with arguments C:\Users\ASHUTOSH\Desktop\PyTest\pytestDemo\test_firstprogram.py --no-header --no-summary -q in C:\Users\ASHUTOSH\Desktop\PyTest\pytestDemo

#============================= test session starts =============================
#collecting ... collected 1 item

#test_firstprogram.py::test_firstprogram PASSED                           [100%]hello


#============================== 1 passed in 0.01s ==============================

#Process finished with exit code 0