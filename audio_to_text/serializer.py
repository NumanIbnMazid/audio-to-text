from rest_framework import serializers


class AudioSerializer(serializers.Serializer):
    audio_file = serializers.FileField(max_length=None, allow_empty_file=False)
