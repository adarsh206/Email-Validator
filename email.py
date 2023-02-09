# This is also email validator but we are using regex approach in this by using regex module

#a-z  njkdj@gmail.com
#0-9
#. _ time 1
#@ time 1
#. on 3,4 position from back

import re
email_condition="^[a-z]+[.\_]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input( " Enter Your Email : ")

if re.search(email_condition, user_email):
    print(" Right Email ")
else:
    print(" Wrong Email ")    