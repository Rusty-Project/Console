def adminlog():
    global isLog, isPass
    log = input("Admin Username > ")
    password = input("Admin Password > ")

    apass = ["1234567890"]  # You can add some custom passwords
    alog = ["admin"]  # You can add some custom usernames

    for i in apass:
        if password == i:
            isPass = True
        else:
            isPass = False

    for i in alog:
        if log == i:
            isLog = True
        else:
            isLog = False

    if isLog and isPass:
        return True
