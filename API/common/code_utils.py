from functools import wraps
from datetime import date, datetime
from common.exceptions import ItemNaoEncontradoException, Handable
import json


def check_404(item, message="Nenhum item encontrado"):
    if not item:
        raise ItemNaoEncontradoException(message)


def exception_handler(func):
    @wraps(func)
    def _exception_handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, Handable):
                return e.handle()
            return "Erro desconhecido.", 500

    return _exception_handler


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date,)):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]