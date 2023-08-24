from Utilitys import comands, func

def find_command(command_name):
    if command_name[:20] == "поставь громкость на" and command_name != "поставь громкость на максимум" and command_name != "поставь громкость на минимум":
        i = 1
        while True:
            if command_name[-i] == " ":
                break
            else:
                i += 1

        command_option = int(command_name[-i + 1:])
        func.choise_func("volume_set", command_option)

    elif command_name[:14] == "найди на ютуби" or command_name[:16] == "найди на youtube":
        print("Ищу")
        command_option = command_name[15:]
        print(command_option)
        func.choise_func("find_on_youtube", command_option)

    elif command_name[:7] == "youtube":
        print("Ищу")
        command_option = command_name[8:]
        print(command_option)
        func.choise_func("find_on_youtube", command_option)

    elif command_name[:4] == "ютуб":
        print("Ищу")
        command_option = command_name[5:]
        print(command_option)
        func.choise_func("find_on_youtube", command_option)

    elif command_name[:17] == "найди в интернете":
        print("Ищу")
        command_option = command_name[18:]
        print(command_option)
        func.choise_func("find_in_browser", command_option)

    elif command_name[:5] == "найди" and command_name[:14] != "найди на ютуби" and command_name[:17] != "найди в интернете" and command_name[:18] != "найди на википедии":
        print("Ищу")
        command_option = command_name[6:]
        print(command_option)
        func.choise_func("find_in_browser", command_option)

    elif command_name[:18] == "найди на википедии":
        print("Ищу")
        command_option = command_name[19:]
        print(command_option)
        func.choise_func("find_on_wiki", command_option)

    elif command_name[:9] == "википедия":
        print("Ищу")
        command_option = command_name[10:]
        print(command_option)
        func.choise_func("find_on_wiki", command_option)

    else:
        for key in comands.commands.keys():
            if command_name in key:
                print("key:", key)
                print("name of func:", comands.commands[key])
                func.choise_func(comands.commands[key], "")
            else:
                pass