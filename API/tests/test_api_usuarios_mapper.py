from API.common.auth_utils import generate_password
from api_usuarios.src.model.dto.aluno_dto import AlunoDTO
from api_usuarios.src.model.form.aluno_form import AlunoForm
from api_usuarios.src.model import mapper
from api_usuarios.src.model.entities.aluno import Aluno


def test_aluno_to_dto():
    aluno = Aluno("1234", "user", "senha", "nome")
    result = mapper.aluno_to_dto(aluno)

    assert isinstance(result, AlunoDTO)
    assert result.__dict__ == AlunoDTO(aluno.user, aluno.nome, aluno.registro).__dict__

def form_to_aluno():
    senha_str = "senha"
    senha = generate_password(senha_str)

    form = AlunoForm("user", "nome", "123", senha_str)
    aluno = mapper.form_to_aluno(form)

    assert isinstance(aluno, Aluno)
    assert aluno.__dict__ == Aluno(form.registro, form.user, senha, form.nome).__dict__
