from src.server.serve import Server

class App:
    def __init__(self) -> None:
        self.server = Server()

    def run(self):
        self.server.gradio_serve()