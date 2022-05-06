from abc import ABCMeta, abstractmethod
import json

class Handable(Exception, metaclass=ABCMeta):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

    @abstractmethod
    def handle(self):
        pass


class ItemNaoEncontradoException(Handable):

    def __init__(self, message):
        super().__init__(message)

    def handle(self):
        return json.dumps({"message": self.message}), 404


class AcessoNegadoException(Handable):
    def __init__(self, message):
        super().__init__(message)

    def handle(self):
        return json.dumps({"message": self.message}), 403