print("You want to login?")
login_answer = input("Y/Register/N:")
if login_answer == "Y":
  import verify_login
if login_answer == "Register":
  import edit_sheet
  print("Now login")
  import verify_login
if login_answer == "N":
    print("OK, Bye!")



