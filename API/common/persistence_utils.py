from functools import wraps
from common.db_connection import DBConnectionSingleton


def transactional(func):
    @wraps(func)
    def _transactional(*args, **kwargs):
        try:
            func_result = func(*args, **kwargs)
            DBConnectionSingleton().commit_conn()
            return func_result
        except Exception as e:
            DBConnectionSingleton().rollback_conn()
            raise e
        finally:
            DBConnectionSingleton().end_conn()
    return _transactional