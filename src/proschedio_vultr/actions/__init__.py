from .instance import Instance
from .block_storage import BlockStorage

class Action:
    @staticmethod
    def instance() -> Instance:
        return Instance()
    
    @staticmethod
    def block_storage() -> BlockStorage:
        return BlockStorage()