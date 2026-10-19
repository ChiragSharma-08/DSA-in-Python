signups = [
    "ravi@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com", #signed up 2nd time
    "sneha@gmail.com",
    "priya@gmail.com",
    "karan@gmail.com",
    "ravi@gmail.com" #signed up 3rd time
]

def remmove_dup(emails):
    seen = set()
    unique = []

    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)
    return unique

clean = remmove_dup(signups)
print(clean)