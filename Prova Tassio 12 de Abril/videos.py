class Video:

    __id: int
    __titulo: str

    def __init__(self, id, titulo):
        self.__id = id
        self.__titulo = titulo

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo