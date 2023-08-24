import subprocess
import webbrowser
import sys

from Utilitys.sound import Sound

def choise_func(command_name, command_option):
    if command_name == "get_info_about_assistant":
        print(f"""==========================
name: Rachel
version: 0.1
==========================""")

    elif command_name == "volume_max":
        Sound.volume_max()

    elif command_name == "volume_min":
        Sound.volume_min()

    elif command_name == "volume_up":
        Sound.volume_up()

    elif command_name == "volume_down":
        Sound.volume_down()

    elif command_name == "volume_mute":
        Sound.mute()

    elif command_name == "volume_set":
        Sound.volume_set(command_option)

    elif command_name == "find_on_youtube":
        try:
            webbrowser.open(f"https://www.youtube.com/results?search_query={command_option}", new=2)
        except:
            webbrowser.open(f"https://www.youtube.com/results?search_query={command_option}", new=1)

    elif command_name == "find_in_browser":
        if command_option in ["youtube", "ютуб"]:
            try:
                webbrowser.open("https://www.youtube.com", new=2)
            except:
                webbrowser.open("https://www.youtube.com", new=1)

        elif command_option in ["wikipedia", "вики", "википедия"]:
            try:
                webbrowser.open("https://ru.wikipedia.org/wiki/Заглавная_страница", new=2)
            except:
                webbrowser.open("https://ru.wikipedia.org/wiki/Заглавная_страница", new=1)

        else:
            try:
                webbrowser.open(f"https://yandex.ru/search/?text={command_option}&lr=47&clid=2358536&src=suggest_B", new=2)
            except:
                webbrowser.open(f"https://yandex.ru/search/?text={command_option}&lr=47&clid=2358536&src=suggest_B", new=1)

    elif command_name == "find_on_wiki":
        try:
            webbrowser.open(f"https://ru.wikipedia.org/wiki/{command_option}", new=2)
        except:
            webbrowser.open(f"https://ru.wikipedia.org/wiki/{command_option}", new=1)

    elif command_name == "open_youtube":
        try:
            webbrowser.open("https://www.youtube.com", new=2)
        except:
            webbrowser.open("https://www.youtube.com", new=1)

    elif command_name == "open_wiki":
        try:
            webbrowser.open("https://ru.wikipedia.org/wiki/Заглавная_страница", new=2)
        except:
            webbrowser.open(r"https://ru.wikipedia.org/wiki/Заглавная_страница", new=1)

    elif command_name == "open_browser":
        subprocess.Popen(r"C:\Users\kiril\AppData\Local\Programs\Opera GX\launcher.exe")

    elif command_name == "exit":
        sys.exit(0)