"""
CP1404 Practical 05 Email
This program stores user emails and their names
"""


def main():
    email_dic = {}  # create an empty dictionary for storing emails and names
    email_dic = store_email(email_dic)
    print_email(email_dic)


def print_email(email_dic):
    for name in email_dic:
        print("{} ({})".format(name, email_dic[name]))


def store_email(email_dic):
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (y/n)".format(name.title())).lower()
        if confirmation == "n" or confirmation == "no":
            name = input("Name: ").title()
        email_dic[name] = email
        email = input("Email: ")
    return email_dic


def get_name(email):
    parts = email.split("@")
    names = parts[0]
    names = names.split(".")
    separator = ' '
    name = separator.join(names)
    return name


main()
