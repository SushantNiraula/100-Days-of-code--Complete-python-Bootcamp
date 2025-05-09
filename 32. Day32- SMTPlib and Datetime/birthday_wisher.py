import datetime as dt
import random
import smtplib
##################### Extra Hard Starting Project ######################
my_email="gopalsharma98011@gmail.com"

# 1. Update the birthdays.csv
# done
# 2. Check if today matches a birthday in the birthdays.csv
with open('birthdays.csv') as file:
    lines = file.readlines()
    
for line in lines[1:]:
    line=line.strip().split(',')
    name=line[0].strip()
    birthday_email=line[1].strip()
    year=int(line[2].strip())
    month=int(line[3].strip())
    day=int(line[4].strip())
    birthday= dt.datetime(year, month, day)
    today=dt.datetime.now()
    if birthday.month==today.month and birthday.day==today.day:
        print(f"Today is {name}'s birthday. Sending email to {birthday_email}...")
        with open(f'./letter_templates/letter_{random.randint(1,3)}.txt') as letter:
            letter_content=letter.read()
            letter_content=letter_content.replace('[NAME]', name)
            letter_content=letter_content.replace('Angela', "Sushant")
            print(letter_content)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_email,
                    msg=f"Subject:Happy Birthday {name}! \n\n {letter_content}"
                )
        

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
