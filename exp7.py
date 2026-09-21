import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails

if __name__ == "__main__":
    text = input("Enter text: ")

    result = find_emails(text)

    print("Email addresses found:")
    for email in result:
        print(email)