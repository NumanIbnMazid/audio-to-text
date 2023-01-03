# Setup Guide

## setup virtual environment and activate

- <https://gist.github.com/umr55766/02084fd38b0426775411ab8353376c69>

## Install required dependencies

$ `pip install -r requirements.txt`

## Run Django Server

$ `python manage.py runserver`

## Access audio to text API url and get result

[Currently supported file formats are: PCM WAV, AIFF/AIFF-C, or Native FLAC]

Access URL <http://127.0.0.1:8000/api/audio-to-text/>, select the audio file with appropriate format and submit.

Done
