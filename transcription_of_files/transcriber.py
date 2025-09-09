import speech_recognition as sr
from logger_dir.logger import Logger

logger = Logger.get_logger()

class Transcriber:
    def __init__(self, path_to_file):
        self.audio = sr.AudioData.from_file(path_to_file)
        self.r = sr.Recognizer()

    def transcription_of_file(self):
        try:
            text = self.r.recognize_sphinx(self.audio)
            logger.info('The file transcribed successfully')
            return text
        except sr.UnknownValueError as error:
            logger.error(f"error: {error} - Sphinx could not understand audio")
        except sr.RequestError as error:
            logger.error(f"error: {error} - Could not request results from Sphinx service")

        try:
            text = self.r.recognize_google(self.audio)
            logger.info('The file transcribed successfully')
            return text
        except sr.UnknownValueError as error:
            logger.error(f"error: {error} - Google Speech Recognition could not understand audio")
        except sr.RequestError as error:
            logger.error(f"error: {error} - Could not request results from Google Speech Recognition service")


