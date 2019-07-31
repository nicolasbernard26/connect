from abc import abstractmethod


class BaseRepository:

    @staticmethod
    @abstractmethod
    def get_by_id(id: int):
        pass
