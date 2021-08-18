# Peter Gatsby
# Problem: https://leetcode.com/explore/interview/card/google/67/sql-2/3044/

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

def numUniqueEmails(emails):
    new_emails = set()
    for email in emails:
        username = email.split('@')[0].replace(".", "")
        if '+' in username:
            username = username[:username.index('+')]
        domain = email.split('@')[1]

        new_emails.add(username+'@'+domain)

    print(new_emails)
    return len(new_emails)

print(numUniqueEmails(emails))