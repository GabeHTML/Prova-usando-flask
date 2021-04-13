from video import Video
from typing import List

class Categoria:

    __id:int
    __nome:str
    __video_list: List

    def __init__(self, id, nome, video_list):
        self.__id = id
        self.__nome = nome
        self.__video_list = video_list

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_video_list(self):
        return self.__video_list