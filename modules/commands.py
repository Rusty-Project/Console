class Commands:
    def mainc(txt, loaded, admin):
        # admin only
        if admin:
            c = ''
        else:
            if txt[0] == 'cdebug':
                print("lol")
