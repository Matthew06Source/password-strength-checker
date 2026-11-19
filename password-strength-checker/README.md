This is a simple command-line Python password checker with a blocklist of common passwords.

On Mac, open Terminal and type "python3 checker.py" 

This password checker pretty much follows NIST SP 800-63B-4 password requirements.

The reason this follows because it has a 15-character minimum for single-factor passwords, while also having a blocklist for simple passwords.
While it follows it also differs from it, NIST does not require mixed characters, so this tool does not score them.

Improvements can be made like larger blocklist, checking for the username or service name, and detecting repeated or sequential characters.

This project taught me passwords strength depends more on length than on character rules since NIST found pushed people toward predictable patterns like "Password1!" Which is easy to guess.
I also learned to use a set for fast lookups, load data from a file, and handle a missing file without crashing.