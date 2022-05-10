from hashlib import sha256
from os import getenv
from api_usuarios.src.model.dto.aluno_dto import AlunoDTO
from common.code_utils import DateTimeEncoder
from common.auth_utils import generate_password, check_password, check_token, generate_token
from common.exceptions import AcessoNegadoException
from pytest import raises
from datetime import datetime, timedelta
import jwt


def test_generate_password():
    digestor = sha256()
    digestor.update("senha".encode("utf-8"))
    senha_result = digestor.hexdigest()

    assert senha_result == generate_password("senha")

def test_check_password_fail():
    senha = "senha"
    senha_criptografada = generate_password("senha_cripto")
    with raises(AcessoNegadoException) as e:
        check_password(senha, senha_criptografada)


def test_check_password_success():
    check_password("senha", generate_password("senha"))
    return


def test_generate_token():
    aluno_dto = AlunoDTO("teste", "teste", "123")
    token = generate_token(aluno_dto)

    dict = jwt.decode(token, verify=False)

    assert dict["user"] == aluno_dto.user
    assert dict["nome"] == aluno_dto.nome
    assert dict["registro"] == aluno_dto.registro
    assert (dict["expiration"] - dict["creation"]).seconds/3600 == 1


def test_check_token_ok():
    aluno_dto = AlunoDTO("teste", "teste", "123")
    token = generate_token(aluno_dto)

    check_token(token)
    return


def test_check_token_err_expired():
    aluno_dto = AlunoDTO("teste", "teste", "123")
    token = generate_token(aluno_dto)

    decoded_token = jwt.decode(token, verify=False)

    decoded_token["expiration"] = datetime.now() - timedelta(hours=1)
    encoded_token = jwt.encode(decoded_token, getenv("SIGNATURE"), json_encoder=DateTimeEncoder).decode("utf-8")
    
    with raises(AcessoNegadoException, match="Token expirado.") as e:
        check_token(encoded_token)


def test_check_token_err_signature():

    aluno_dto = AlunoDTO("teste", "teste", "123")
    token = generate_token(aluno_dto)

    decoded_token = jwt.decode(token, verify=False)
    encoded_token = jwt.encode(decoded_token, "INVALID_SIGNATURE", json_encoder=DateTimeEncoder).decode("utf-8")

    with raises(AcessoNegadoException, match="Falha na identificação da origem da autenticação.") as e:
        check_token(encoded_token)
