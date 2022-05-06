from api_usuarios.src.model.dto.aluno_dto import AlunoDTO
from api_usuarios.src.model.entities.aluno import Aluno
from common.auth_utils import generate_password


def aluno_to_dto(aluno):
    return AlunoDTO(aluno.user, aluno.nome, aluno.registro)


def form_to_aluno(aluno_form):
    senha = generate_password(aluno_form.senha)
    return Aluno(aluno_form.registro, aluno_form.user, senha, aluno_form.nome)