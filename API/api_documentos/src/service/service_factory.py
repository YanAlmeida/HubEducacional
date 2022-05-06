from api_documentos.src.persistence.documento_dao import DocumentoDao
from api_documentos.src.service.documento_service import DocumentoService


def get_documento_service():
    dao = DocumentoDao()
    return DocumentoService(dao)