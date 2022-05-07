from common.persistence_utils import transactional


class AlunoService:
    def __init__(self, aluno_dao):
        self.__aluno_dao = aluno_dao

    @transactional
    def persistir_aluno(self, aluno):
        return self.__aluno_dao.persistir(aluno)
    
    @transactional
    def recuperar_aluno(self, user):
        return self.__aluno_dao.recuperar_por_user(user)