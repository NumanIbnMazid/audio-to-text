from rest_framework import viewsets
from .serializer import AudioSerializer
import speech_recognition as sr
from rest_framework.response import Response


class AudioToTextViewset(viewsets.ViewSet):
    serializer_class = AudioSerializer
    
    def audio_to_text(self, request):
        AUDIO_FILE = request.data.get("audio_file")
        
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            result = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + result)
            return Response(result)
        except sr.UnknownValueError:
            return Response("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            return Response("Could not request results from Google Speech Recognition service; {0}".format(e))
        return Response("Failed!!!")
