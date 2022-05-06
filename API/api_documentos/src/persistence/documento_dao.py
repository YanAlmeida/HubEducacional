from common.db_connection import DBConnectionSingleton
from common.code_utils import check_404
from api_documentos.src.model.entities.documento import Documento


class DocumentoDao:

    _table_name = "doc_estudos"
    _field_primary_key = "registro"
    _fields = [
        "tema",
        "autor",
        "area_conhecimento",
        "fonte",
        "file_path",
        "registro"
    ]

    def recuperar_documentos(self):
        with DBConnectionSingleton().get_cursor() as cursor:
            query = f"SELECT {','.join(self._fields)} FROM {self._table_name};"
            cursor.execute(query)
            result = cursor.fetchall()
            check_404(result)
        return list(map(lambda tupla: Documento(*tupla), result))

    def persistir(self, documento):
        with DBConnectionSingleton().get_cursor() as cursor:
            values_insert = (documento.tema, documento.autor, documento.area_conhecimento, documento.fonte, documento.file_path, documento.registro_criador,)
            query = f"INSERT INTO {self._table_name}({','.join(self._fields)}) VALUES ({','.join(['%s']*len(self._fields))});"
            cursor.execute(query, values_insert)
        return
