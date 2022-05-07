from common.db_connection import DBConnectionSingleton
from common.code_utils import check_404
from api_usuarios.src.model.entities.aluno import Aluno


class AlunoDao:

    _table_name = "aluno"
    _field_user = "user"
    _fields = [
        "registro",
        "user",
        "senha",
        "nome"
    ]

    def recuperar_por_user(self, user):
        with DBConnectionSingleton().get_cursor() as cursor:
            query = f"SELECT {','.join(self._fields)} FROM {self._table_name} WHERE {self._field_user} = %s;"
            cursor.execute(query, (user,))
            result = cursor.fetchone()
            check_404(result)
        return Aluno(*result)

    def persistir(self, aluno):
        with DBConnectionSingleton().get_cursor() as cursor:
            values_insert = (aluno.registro, aluno.user, aluno.senha, aluno.nome,)
            query = f"INSERT INTO {self._table_name}({','.join(self._fields)}) VALUES ({','.join(['%s']*len(self._fields))});"
            cursor.execute(query, values_insert)
        return
