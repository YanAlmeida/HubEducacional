from mock import MagicMock

from api_usuarios.src.service.aluno_service import AlunoService

def test_persistir_aluno():
    dao = MagicMock()
    service = AlunoService(dao)
    service.persistir_aluno(MagicMock())

    dao.persistir.assert_called_once()

def test_recuperar_aluno():
    dao = MagicMock()
    service = AlunoService(dao)
    service.recuperar_aluno(user="TESTE")

    dao.recuperar_por_user.assert_called_once()