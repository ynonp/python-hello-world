from gtts import gTTS

google_voice = gTTS(text="Hello world", lang='en')
google_voice.save('sound.mp3')

