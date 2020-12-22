from src.config import Config


class CraftingSpeedElement:
    def __init__(self, config: Config):
        self.config = config

    def modify(self, value):
        pass

    def get(self):
        raise Exception("Not implemented yet")