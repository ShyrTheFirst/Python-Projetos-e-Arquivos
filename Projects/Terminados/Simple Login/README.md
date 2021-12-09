# Simplest-loginsys-ever
Just a simple Login system created with openpyxl


You can create your username and password and then login using it. You can't use an already taken username, but you can use the same password and the system still identify wich account it belongs to.

You'll find, in each .py:
config.py --- 4 var used in the other codes. It was easy for me to use like this to change them in local but having global effect.
edit_sheet.py --- this is the code used for creating new users and passwords. We use 2 var from config.py here!
verify_login.py --- this is the code for verifying if the user and password you are using to login are correct! Here we use another 2 var from config.py
main.py --- call all the codes :) 
users.xlsx --- Our "database" with username and password. Yeah, you can edit it, so it's not safe to use for real... And it's just local, so you can't create an user somewhere and use anywhere else if you don't bring your spreadsheet along with you... but it's only for testing!!!


If you're trying to understand openpyxl, trying to understand login systems or you are just curious... I hope this code help :) 
