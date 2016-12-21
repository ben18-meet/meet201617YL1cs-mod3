#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Two things are missing from the line below - fill them in
my_user=UserAccount("Ben","0802","my secret is..." )

#Call the print_password method (function) - it takes one input - a guess for the password.
my_user.print_secret()
#Use the wrong password as input here
password_attemp == my_user.password("00234")

#Use the right password here
my_user.password("0802")
