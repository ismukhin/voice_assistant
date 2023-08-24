import pvporcupine
from pvrecorder import PvRecorder
from playsound import playsound

def wake_word():
    porcupine = pvporcupine.create(
        access_key='8s2zeJzg+EdjZhb5biPmxZcicyo1RJz9p8MiJvr+t2nCR1uYpaZUMg==',
        keyword_paths=[r"C:\Users\kiril\PycharmProjects\Emily\Referens\Rachel_en_windows_v2_2_0.ppn"]
    )

    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    print("Using device: %s" % recoder.selected_device)
    recoder.start()
    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            playsound(r"C:\Users\kiril\PycharmProjects\Emily\Referens\yes_sir.wav")
            print("Yes, sir!")
            break

    porcupine.delete()
