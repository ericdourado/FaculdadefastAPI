from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    '''
    CONFIGURACOES PARA O APP
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root:root@localhost:3306/faculdade?charset=utf8mb4'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True 

settings = Settings()