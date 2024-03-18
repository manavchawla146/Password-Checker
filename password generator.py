
i = 1
while i == 1:  # start while loop

    symbols = set(
        r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")  # special characters set

    x = input("Enter Password : ")  # password input

    uper = lower = num = spechar = 0

    for c in x:
        txt_uper = c.isupper()
        txt_lower = c.islower()
        txt_num = c.isnumeric()
        txt_spechar = c in symbols

        if (txt_uper is True):
            uper = 1
        if (txt_lower is True):
            lower = 1
        if (txt_num is True):
            num = 1
        if (txt_spechar is True):
            spechar = 1

    if uper == 1 and lower == 1 and num == 1 and spechar == 1 and len(x) >= 8:
        print("Good ! Strong Password")
        j = 1
        while j == 1:  # password re-enter while loop
            y = input("Re-enter password : ")  # password re-enter
            if (x == y):
                # password is generated with all conditions
                print(">>> Done!\n>>> Password is generated.")
                i = 0
                j = 0
            else:
                print("!!! Password not match.")

    # The generated passwords meet the following requirements:
    if uper == 0:
        print("> Passwords must include at least one uppercase letter.")
    if lower == 0:
        print("> Passwords must include at least one lowercase letter.")
    if num == 0:
        print("> Passwords must include at least one numerical digit.")
    if spechar == 0:
        print("> Passwords must include at least one special character.")
    if (len(x) < 8):
        print("> Passwords must have a minimum length of 8 characters.")
