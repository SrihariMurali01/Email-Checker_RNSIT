# Email Status Checker

This Python script is designed to check the status of emails in a CSV file and send a reminder email if necessary.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- `smtplib`: This library is used for sending emails.
- `pandas`: A powerful data manipulation and analysis library.
- `datetime`: To work with dates and times.
- `imap_tools`: A library for working with IMAP mail servers.

You can install these dependencies using `pip`:

```bash
pip install smtplib pandas datetime imap_tools
```
Usage
Replace EMAIL and PASSWORD in the script with your email credentials.
Set the file_path variable to the path of your CSV file.
Run the script.
The script will check the email status and, if needed, send reminder emails to recipients.

Example
```python
# Example usage
file_path = 'list.csv'  # Replace with the path to your CSV file
check_email_status(file_path)
```

Contributors
- Srihari M
- Suraj RS
