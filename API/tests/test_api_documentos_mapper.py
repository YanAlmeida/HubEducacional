from api_documentos.src.model.dto.documento_dto import DocumentoDTO
from api_documentos.src.model.form.documento_form import DocumentoForm
from api_documentos.src.model import mapper
from api_documentos.src.model.entities.documento import Documento

def test_documento_to_dto():
    documento = Documento("tema", "autor", "area_conhecimento", "fonte", "path", "123")
    dto = mapper.documento_to_dto(documento)

    assert isinstance(dto, DocumentoDTO)
    assert dto.__dict__ == DocumentoDTO(documento.tema, documento.autor, documento.area_conhecimento,
                                            documento.fonte, documento.file_path, documento.registro_criador).__dict__


def test_form_to_documento():
    form = DocumentoForm("tema", "autor", "area_conhecimento", "fonte", "path", "123")
    documento = mapper.form_to_documento(form)

    assert isinstance(documento, Documento)
    assert documento.__dict__ == Documento(form.tema, form.autor, form.area_conhecimento,
                                            form.fonte, form.file_path, form.registro_criador).__dict__
