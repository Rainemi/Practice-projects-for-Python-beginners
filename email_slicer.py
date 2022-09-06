

# to slice an email
# collect email from user
# split the email with @ 
# the first part is the username 
# the second part is the domain name

def main():
    print("Welcome To The Email Slicer ")
    print("")

    email_input = input(" Input your email address : ")

    (username , domain) = email_input.split("@")
    (domain , extensions) = domain.split('.')

    print("Username: " , username)
    print("Domain: " , domain)
    print("Extensions: " , extensions)
    
print(main())
