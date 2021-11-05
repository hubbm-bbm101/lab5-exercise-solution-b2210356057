email = input('Please enter your email = ')
def function(mail):
    for i in email:
        if i == '@':
            i in email == False
        elif i == '.':
            i in email == False
    if '@' in email and '.' in email:
        return True
    else:
        return False
print(function(email))