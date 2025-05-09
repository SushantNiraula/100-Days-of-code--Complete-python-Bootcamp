import smtplib

my_email="gopalsharma98011@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="sushantniraula01@gmail.com",
    msg="Subject:Hello Sushant this is a test email\n\nThis is the body of the email")
connection.close()