from api_usuarios.src.persistence.aluno_dao import AlunoDao
from api_usuarios.src.service.aluno_service import AlunoService


def get_aluno_service():
    dao = AlunoDao()
    return AlunoService(dao)