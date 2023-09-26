
import smtplib
import pandas as pd
from datetime import datetime
from imap_tools import MailBox, AND

# Server is the address of the IMAP server
EMAIL = "test_0608@hotmail.com"
PASSWORD = "Test@0608"
mailbox = MailBox("outlook.office365.com").login(EMAIL, PASSWORD)

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

def write_csv_file(df, file_path):
    df.to_csv(file_path, index=False)

def check_email_status(file_path):
    df = read_csv_file(file_path)
    for index, row in df.iterrows():
        email = row['Email']  # Assuming 'Email' is the column name for email addresses
        messages = mailbox.fetch()
        for msg in messages:
            if row['Status'] != 'Sent':
                if msg.from_ == email:
                    # Email found, mark as sent
                    df.at[index, 'Status'] = 'Sent'
                else:
                    df.at[index,'Status'] = 'Not Sent'
                    due_date = datetime.strptime(row['Due Date'], '%Y-%m-%d')
                    if datetime.today() > due_date:
                        # Due date has exceeded, send not sent mail
                        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
                            connection.starttls()  # Encrypt connection
                            connection.login(user=EMAIL, password=PASSWORD)  # Logging into the given email account
                            connection.sendmail(from_addr=EMAIL,
                                                to_addrs=row["Email"],
                                                msg=f"Subject:SEND THE GODDAMN ASSIGNMENT!\n\nSEND madbidappa plis!")

    write_csv_file(df, file_path)

# Example usage
file_path = 'list.csv'  # Replace with the path to your CSV file
check_email_status(file_path)
