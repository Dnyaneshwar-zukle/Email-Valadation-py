# a-z  dnyaneshwar@gmail.com
# 0-9
# 1 time . _ should be oresent only 
# 1 time @ should be oresent only 
# . position should be on 2nd last or 3rd last
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Email : ")

if re.search(email_condition,user_email):
    print(" Right email ")
else:
    print(" Wrong email ")    