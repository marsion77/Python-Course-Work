# 1.In a paragraph replace a “is” with “was” . then count no of “a” in a paragraph
name = "Lion was coming lorem10sjnefjaih3ufh322aaaodwasaawasniwdwasaa"
print(name.replace("was","is"))
print(name.count("a"))


# 2.get a input from user check its a Email Id.
Email = input("Enter a Valid EMail Address")
if Email.endswith(".com"):
    print(True)


# 3.get a input from user also check  its valid password.
Password = input("Enter a Valid Passowrd")
strong = ["@","#","$","%","&","*"]
for i in Password:
    if i in strong:
        print("Strong Password")
        break
    else:
        print("Enter a Strong Password")


# 4.login task - get input from user name & password its align with your previous data.throw a login successful message.otherwise its a Invalid input.
name = "Maarison"
password = "India@2025"

user_name = input("Enter You Name")
user_password = input("Enter a Password")

if name == user_name:
    if password == user_password:
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid User Name")
    

