# import pvporcupine
# from pvrecorder import PvRecorder
# from playsound import playsound
#
#
# porcupine = pvporcupine.create(
#     access_key='8s2zeJzg+EdjZhb5biPmxZcicyo1RJz9p8MiJvr+t2nCR1uYpaZUMg==',
#     keyword_paths=["Referens/Rachel_en_windows_v2_2_0.ppn"]
# )
#
# recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
# print("Using device: %s" % recoder.selected_device)
# recoder.start()
# while True:
#     keyword_index = porcupine.process(recoder.read())
#
#     if keyword_index >= 0:
#         playsound("Referens/yes_sir.wav")
#         print("Yes, sir!")
#
# porcupine.delete()

import torch
import sounddevice as sd
import time
from omegaconf import OmegaConf

# models = OmegaConf.load('models.yml')
#
# available_languages = list(models.tts_models.keys())
# print(f'Available languages {available_languages}')
#
# for lang in available_languages:
#     _models = list(models.tts_models.get(lang).keys())
#     print(f'Available models for {lang}: {_models}')

language = 'ru'
model_id = 'v4_ru'
sample_rate = 48000
speaker = 'baya' #aidar, baya, kseniya, xenia, eugene, random 'v4_ru', 'v3_1_ru', 'ru_v3', 'aidar_v2', 'aidar_8khz', 'aidar_16khz', 'baya_v2', 'baya_8khz', 'baya_16khz', 'irina_v2', 'irina_8khz', 'irina_16khz', 'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz', 'natasha_v2', 'natasha_8khz', 'natasha_16khz', 'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz'
put_accent = True
put_yo = True
device = torch.device('cpu')
example_text = """
              <speak>
              <p>
                 Да, сэр</prosody>.
                 Я слушаю</prosody>.
                 Ищу в интернете!</prosody>
                 Ищу на ютубе!</prosody>
                 Ищу на википедии!</prosody>
                 Устанавливаю громкость на максимум!</prosody>
                 Устанавливаю громкость на минимум!</prosody>
                 Выключаю звук!</prosody>
                 Досвидания!</prosody>
                 Обращайтесь!</prosody>
                 <prosody pitch="x-high">
                  
              </p>
              </speak>
              """

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)

audio = model.apply_tts(text=example_text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

print(example_text)

sd.play(audio, sample_rate)
time.sleep(len(audio) / sample_rate)
sd.stop()