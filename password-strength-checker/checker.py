import getpass
from pathlib import Path

MIN_LENGTH = 15  
MAX_SCORE = 4


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
    """Return (score, rating, tips) for a password."""
    if password.lower() in COMMON_PASSWORDS:
        return 0, "Blocked", ["This is on the common-password list. Choose a different one."]

    length = len(password)
    tips = []

    if length < 8:
        score, rating = 1, "Weak"
        tips.append("Too short. Use at least 15 characters.")
    elif length < MIN_LENGTH:
        score, rating = 2, "Below NIST minimum"
        tips.append("Use at least 15 characters if this is your only login factor.")
    elif length < 20:
        score, rating = 3, "Meets NIST minimum"
        tips.append("Longer is better. A passphrase of several random words works well.")
    else:
        score, rating = 4, "Strong"

    return score, rating, tips


if __name__ == "__main__":
    pw = getpass.getpass("Enter a password to check: ")
    score, rating, tips = check_password(pw)
    print(f"Score: {score}/{MAX_SCORE} ({rating})")
    for tip in tips:
        print(f"- {tip}")
