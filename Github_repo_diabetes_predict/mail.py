import smtplib
import os

def send_mail(cust_email,message,name,phone):

    rec_email="your_email_address"
    password="your_email_password"
    # message="hi"
    body="Mail From: "+name+"\n\nmessage: "+message + "\n\nPhone: "+phone+"\n\nemail: "+cust_email
    Subject="Mail From Diabetes Prediction"
    msg=f'Subject: {Subject}\n\n{body}'
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(rec_email,password)
    # print("login success")
    server.sendmail("your_email_address",rec_email,msg)#here your_email_address is used as sender email
    # print("email sent to",rec_email)
    server.quit()
    return True


























# # from flask import Blueprint, render_template, request
# # from flask_mail import Mail,Message
# # from flask_login import login_required, current_user

# # mail = Blueprint("mail", __name__)

# # # # mail = Mail(mail)
# # # def send_mails(name,email,phone,message,mail_username):
# # #     msg=Message(subject=f"Mail from{name}",body=f"Name: {name}\nE-mail: {email}\nPhone: {phone}\n\n{message}",sender=mail_username,recipients=['pofocas475@latovic.com'])
# # #     mail.send(msg)

# # @mail.route("/contact/",methods=['GET','POST'])
# # @login_required
# # def contact():
# #     if request.method=="POST":
# #         name = request.form.get('name')
# #         email = request.form.get('email')
# #         phone = request.form.get('phone')
# #         message = request.form.get('message')
# #         username="testingmail01@opentrash.com"
# #         # send_mails(name,email,phone,message,username)
# #         msg=Message(subject=f"Mail from{name}",body=f"Name: {name}\nE-mail: {email}\nPhone: {phone}\n\n{message}",sender=username,recipients=['pofocas475@latovic.com'])
# #         mail.send(msg)
# #         return  render_template('contact.html',success=True)
# #     return render_template('contact.html')