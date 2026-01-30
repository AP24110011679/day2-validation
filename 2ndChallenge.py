student_id = input("Enter student id: ")
email = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter referral: ")

valid = True


if len(student_id) != 7:
    valid = False
if valid and student_id[:4] != "CSE-":
    valid = False
if valid and not student_id[4:].isdigit():
    valid = False


if valid:
    if "@" not in email or "." not in email:
        valid = False
    elif email[0] == "@" or email[-1] == "@":
        valid = False
    elif not email.endswith(".edu"):
        valid = False


if valid:
    if len(password) < 8:
        valid = False
    elif not password[0].isupper():
        valid = False
    elif password.isalpha():
        valid = False


if valid:
    if len(referral) != 6:
        valid = False
    elif referral[:3] != "REF":
        valid = False
    elif not referral[3:5].isdigit():
        valid = False
    elif referral[5] != "@":
        valid = False

if valid:
    print("Approved")
else:
    print("Rejected")