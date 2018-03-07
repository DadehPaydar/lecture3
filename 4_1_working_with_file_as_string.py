"""
reading a file
"""
file = open('emails', 'r')
file_contents = file.read()
list_of_emails = file_contents.split('\n')
"""
show emails that contains outlook
"""
for email in list_of_emails:
    if 'outlook' in email:
        print(email)
