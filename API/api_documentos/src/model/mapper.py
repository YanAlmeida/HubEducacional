from pydoc import Doc
from api_documentos.src.model.dto.documento_dto import DocumentoDTO
from api_documentos.src.model.entities.documento import Documento


def documento_to_dto(documento):
    return DocumentoDTO(documento.tema, documento.autor, documento.area_conhecimento,
        documento.fonte, documento.file_path, documento.registro_criador)


def form_to_documento(documento_form):
    return Documento(documento_form.tema, documento_form.autor, documento_form.area_conhecimento,
        documento_form.fonte, documento_form.file_path, documento_form.registro_criador)