import pandas as pd
import smtplib
import datetime as dt

# Load the CSV file
df = pd.read_csv("birthdays.csv", encoding='latin1')

# Get today's date in dd-MMM format (e.g., 07-Jun)
today = dt.datetime.now().strftime("%d-%b")

# Your Gmail credentials
your_email = "ponugotiakshit@gmail.com"
your_password = "Your App password"  # App Password

# Loop through each person in the CSV
for index, row in df.iterrows():
    if row['Birthday'].strip() == today:
        name = row['Name']
        email = row['Email']
        
        subject = "🎉 Happy Birthday!"
        body = f"""Hi {name},

Wishing you a wonderful birthday filled with happiness, success, and love. 🎂🎈🎁

Best wishes,
Akshit
"""
        message = f"Subject: {subject}\n\n{body}"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=your_email, password=your_password)
            connection.sendmail(
                from_addr=your_email,
                to_addrs=email,
                msg=message.encode("utf-8")
            )

print("✅ Birthday wishes sent (if anyone had a birthday today).")
