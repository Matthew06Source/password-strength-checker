import getpass
from pathlib import Path


def load_common_passwords(filename="common.txt"):
    path = Path(__file__).parent / filename
    try:
        with open(path, "r") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using a small built-in list.")
        return {"password", "123456", "qwerty"}


COMMON_PASSWORDS = load_common_passwords()


def check_password(password):
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is a very common password."]

    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use 12 or more characters.")
    else:
        tips.append("Too short. Use at least 12 characters.")

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Mix uppercase and lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add a number.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        tips.append("Add a symbol.")

    return score, tips


def rate(score):
    if score <= 1:
        return "Weak"
    if score <= 3:
        return "Medium"
    return "Strong"


if __name__ == "__main__":
    pw = getpass.getpass("Enter a password to check: ")
    score, tips = check_password(pw)
    print(f"Score: {score}/5 ({rate(score)})")
    for tip in tips:
        print(f"- {tip}")