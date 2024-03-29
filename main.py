##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib

EMAIL = "jayber1@yahoo.com"
PASSWORD = "yvfngtkvredjkygx"

# - pass work "yvfngtkvredjkygx"
# - pass marina "fzxgmakhpdnwtjqk"
# 2. Check if today matches a birthday in the birthdays.csv
# ----------------------------- csv handling ------------------------- #
df = pandas.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")

# --------------------------datetime handling ------------------------ #
dt_month = dt.datetime.now().month
dt_day = dt.datetime.now().day
dt_date = f"{dt_month}/{dt_day}" # current date

# -------------------------- program --------------------------------- #

rand_num = random.randint(1, 3)

for i in range(0, len(df_dict)):
    df_data = f"{df_dict[i]['month']}/{df_dict[i]['day']}"
    if dt_date == df_data:
        with open(f"letter_templates/letter_{rand_num}.txt") as file:
            to_send_file = file.read()
            to_send_updated = to_send_file.replace("[NAME]", f"{df_dict[i]['name']}")

            print(to_send_updated)
            print(df_dict[i]["email"])
        
        connection = smtplib.SMTP("smtp.mail.yahoo.com",465)
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=EMAIL, from_addr=df_dict[i]["email"], msg=f"subject: happy happy yay yay \n\n {to_send_updated}")
        connection.close()
        print("sending seccessful")
       

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
