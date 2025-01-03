import re

def search(a):
    email_pattern = "^\w+([\.-]?\w+)*@\w+([|.-]?\w+)*(\?\w{2,3})+$"
    result=re.search(email_pattern,a)
    if result:
        print("True")
    else:
        print("False")


search("hankara\gmail?com")
