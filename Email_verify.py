import math
import random
import smtplib
import string
def OTP_generator():
    string='0123456789abcdefghijklmnopqrstuvwxyz'
    OTP=''
    for i in range(6):
        OTP+=string[math.floor(random.random()*len(string))]
    return OTP
def password_generator(size):
    password_G=''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for n in range(size)])
    return password_G

user_name_list=['mohit02']
password_u_l=['singh']
print('login or signup')
take_input=input()
if take_input=='login':
    print('enter user name and password')
    user_name=input()
    for i in user_name_list:
        if user_name==i:
            print('user name is correct')
            print('now enter password')
            password_u=input()
            for j in password_u_l:
                if password_u==j:
                    print('password is correct, now you can generate password')
                    print('enter size of password you need')
                    size=int(input())
                    ans=password_generator(size)
                    print(ans)
                    break
                else:
                    print('again start from starting')
                    exit()
        else:
            print('user name is incorrect restart again')
            quit()
elif take_input=='signup':
    print('enter user name')
    user_name=input()
    user_name_list.append(user_name)
    print(user_name_list)
    print('enter password')
    password_u=input()
    password_u_l.append(password_u)
    print(password_u_l)
    print('enter your email')
    email=input()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('mohit1124.be21@chitkarauniversity.edu.in','hjxbwxwqpziudxbs')
    otp=OTP_generator()
    server.sendmail('mohit1124.be21@chitkarauniversity.edu.in',email,otp)
    server.quit()
    print('enter the otp for verification')
    receive_otp=input()
    if receive_otp==otp:
        print('your otp is correct')
        print('enter size of password you need')
        size=int(input())
        print('here is password')
        ans=password_generator(size)
        print(ans)
        quit()
    else:
        print('start from starting')
        quit()
