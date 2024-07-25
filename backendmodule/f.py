import re

def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9.-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{8,}\b'
    return re.match(regex, email)

# def is_valid_password(password):
#     if len(password) < 8:
#         return False
#     if not re.search(r"[A-Z]", password):
#         return False
#     if not re.search(r"[a-z]", password):
#         return False
#     if not re.search(r"[0-9]", password):
#         return False
#     # if not re.search(r"[!@#\$%\^&\*]", password):
#     #     return False
#     return True

def is_valid_username(username):
    regex = r'^[A-Za-zА-Яа-я0-9]{1,25}$'
    return re.match(regex, username)

def is_valid_name(name):
    regex = r'^[а-яА-Яa-zA-Z]{1,20}$'
    return re.match(regex, name)

def is_valid_birthday(bday):
    regex = r'^[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,4}$'
    return re.match(regex, bday)

def is_valid_sex(sex):
    regex = r'^[mfo]{1}$'
    return re.match(regex, sex)

def is_valid_phone(phone):
    regex = r"^[+7|8]{2}[0-9]{10}$"
    return re.match(regex,phone)