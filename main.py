##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib
import  os

# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")

dt_month = dt.datetime.now().month
dt_day = dt.datetime.now().day
dt_date = f"{dt_month}/{dt_day}"

for i in range(0, len(df_dict)):
    df_data = f"{df_dict[i]['month']}/{df_dict[i]['day']}"
    if dt_date == df_data:
        to_send = True

rand_num = random.randint(1, 3)

with open("/letter_templates/letter_1.txt") as file:
    print(file)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
