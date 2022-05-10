from mock import MagicMock

from api_documentos.src.service.documento_service import DocumentoService


def test_persistir_documento():
    dao = MagicMock()
    service = DocumentoService

    service.persistir_documento(MagicMock())

    dao.persistir.assert_called_once()

def test_recuperar_documentos():
    dao = MagicMock()
    service = DocumentoService

    service.recuperar_documentos()
    dao.recuperar_documentos.assert_called_once()
