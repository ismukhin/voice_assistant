from Utilitys import choise_command, wake_word, listen_recognized

# Main part with information of assistant
# ==================================================
# name = "Rachel"
# version = "0.1"
# ==================================================


# Greetings
# ==================================================
wake_word.wake_word()
# ==================================================

# Take command
# ==================================================
while True:
    call = listen_recognized.mic_recognition_ru()
    if call is not None:
        choise_command.find_command(call)