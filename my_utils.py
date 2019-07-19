from flask import flash
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$")
AT_LEAST_ONE_NUM_REGEX = re.compile(r"^.*[0-9]+.*")
AT_LEAST_ONE_CAP_REGEX = re.compile(r"^.*[A-Z]+.*")

def is_age_over(num, dob):
    if(type(dob) == type('')):
        if dob != '':
            dob = datetime.strptime(dob, '%Y-%m-%d')
        else:
            return False
    elif type(dob) == type(datetime.now()):
        dob = dob
    else:
        return False
    year = dob.year + num
    nth_bday = datetime.strptime(f"{year}-{dob.month}-{dob.day}", "%Y-%m-%d")
    today = datetime.today()
    return (today - nth_bday).days >= 0

def copy_immutable_dict(immutable_dict, **kwargs):
    result_dict = dict()
    for item in immutable_dict.keys():
        result_dict[item] = immutable_dict[item]
    for param, value in kwargs.items():
        result_dict[param] = value
    return result_dict

def get_age(dob):
    age = -1
    while(is_age_over(age+1, dob)):
        age += 1
    return age

def is_valid_password(request_form, categories=['password', 'confirm']):
    is_valid = True
    if len(request_form[categories[0]]) < 8:
        flash("Password must be at least eight characters", categories[0])
        is_valid = False
    if not(AT_LEAST_ONE_NUM_REGEX.match(request_form[categories[0]]) and AT_LEAST_ONE_CAP_REGEX.match(request_form[categories[0]])):
        flash("Password must contain at least one capital letter and one digit", categories[0])
        is_valid = False
    if (request_form[categories[1]] == "") or (request_form[categories[0]] != request_form[categories[1]]):
        flash("Passwords do not match", categories[1])
        is_valid = False
    return is_valid


