from pydantic import BaseModel

class LoggerModel(BaseModel):
    environment: str

class ServerModel(BaseModel):
    host: str
    port: int

class PathModel(BaseModel):
    output_dir: str

class WhisperttsModel(BaseModel):
    model_name: str

class TortoisettsModel(BaseModel):
    model_name: str

class MetavoiceModel(BaseModel):
    model_name: str

class TTSModel(BaseModel):
    whispertts: WhisperttsModel
    tortoisetts: TortoisettsModel
    metavoice:MetavoiceModel

class Model(BaseModel):
    logger: LoggerModel
    server: ServerModel
    paths: PathModel
    tts_model: TTSModel
