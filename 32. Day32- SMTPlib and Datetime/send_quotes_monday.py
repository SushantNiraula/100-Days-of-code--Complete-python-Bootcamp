import datetime as dt
import smtplib
import random
my_email="gopalsharma98011@gmail.com"
now=dt.datetime.now()  # Current date and time
if now.weekday()==4: # Monday
    print("Today is Monday")
    # Send email with quotes
    with open("quotes.txt") as quotes_file:
        all_quotes=quotes_file.readlines()
        quote=random.choice(all_quotes)
    quote=str(quote.strip())
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sushantniraula01@gmail.com",
            msg=f"Subject:Monday Motivation quote\n\n{quote}".encode("utf-8")
    
        )

    