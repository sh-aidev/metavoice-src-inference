import os
import uuid
from whisperspeech.pipeline import Pipeline

from src.utils.logger import logger

class WhisperSpeech:
    def __init__(self, model_name = "collabora/whisperspeech:s2a-q4-tiny-en+pl.model", output_dir = "tts-data/speech"):
        logger.info(f"WhisperSpeech model: {model_name}")
        self.pipeline = Pipeline(s2a_ref=model_name)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir

    def speak(self, text: str):
        audio_id = str(uuid.uuid4())
        audio_path = os.path.join(self.output_dir, f"{audio_id}.wav")
        logger.info(f"Audio path: {audio_path} for text: {text}")
        self.pipeline.generate_to_file(audio_path, text)
        return audio_path