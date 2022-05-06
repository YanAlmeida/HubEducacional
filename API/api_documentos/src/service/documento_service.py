from common.persistence_utils import transactional


class DocumentoService:
    def __init__(self, documento_dao):
        self.__documento_dao = documento_dao

    @transactional
    def persistir_documento(self, documento):
        return self.__documento_dao.persistir(documento)
    
    @transactional
    def recuperar_documentos(self):
        return self.__documento_dao.recuperar_documentos()
