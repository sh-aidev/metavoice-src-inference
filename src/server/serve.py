import gradio as gr

from src.core.whisperSpeech import WhisperSpeech
from src.utils.config import Config
from src.utils.logger import logger

class Server:
    def __init__(self) -> None:
        root_config_dir = "configs"

        logger.debug(f"Root config dir: {root_config_dir}")

        self.config = Config(root_config_dir)

        self.whisper_speech_pipeline = WhisperSpeech(
            model_name=self.config.tts.tts_model.whispertts.model_name,
            output_dir=self.config.tts.paths.output_dir
        )

    def gradio_serve(self) -> None:
        text = gr.Textbox(lines=3, label="Text")
        # tts_model = gr.Dropdown(
        #     choices=["whisper-speech", "tortoise-tts", "metavoice-tts"],
        #     label="TTS Model",
        #     default="whisper-speech"
        # )
        
        demo = gr.Interface(fn = self.whisper_speech_pipeline.speak,
            inputs = [text],
            outputs = gr.Audio(label="Audio"), 
            title = '',
            description = 'A simple application for text to speech using whisper speech model.'
        )

        demo.launch(server_name = self.config.tts.server.host, server_port = self.config.tts.server.port)
        