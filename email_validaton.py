import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = input("Enter email: ")
if re.search(regex, email):
    print("Valid email")
    
else:
    print("Invalid email")
    
# another method
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("address is valid")
else:
    print("not valid")
    
    
x = email.strip().lower()
if ("@" not in email) or (email[-4:] not in ".com.org.edu.gov.net"):
    print('another invalidity')
elif not "@" in email:
    print("invalid")
elif not email[-4:] in ".com.org.edu.gov.net":
    print('another invalid')
else:
    print('correct')
