from .instance import Instance
from .block_storage import BlockStorage
from .database import Database

class Action:
    @staticmethod
    def instance() -> Instance:
        return Instance()
    
    @staticmethod
    def block_storage() -> BlockStorage:
        return BlockStorage()
    
    @staticmethod
    def database() -> type[Database]:
        return Database