import datetime
from hashlib import sha256
from common.exceptions import AcessoNegadoException
from common.code_utils import DateTimeEncoder
from os import getenv
import jwt


def generate_password(senha):
    digestor = sha256()
    digestor.update(senha.encode("utf-8"))
    return digestor.hexdigest()


def check_password(senha, senha_criptografada):
    digestor = sha256()
    digestor.update(senha.encode("utf-8"))
    
    if digestor.hexdigest() != senha_criptografada:
        raise AcessoNegadoException("Senha incorreta.")


def generate_token(aluno_dto):
    dict_aluno = aluno_dto.__dict__
    now = datetime.datetime.now()
    expiration = now + datetime.timedelta(hours=1)

    dict_expiration = {
        "creation": now,
        "expiration": expiration
    }

    token_encode = {**dict_aluno, **dict_expiration}


    return jwt.encode(token_encode, getenv("SIGNATURE"), json_encoder=DateTimeEncoder).decode("utf-8")


def check_token(token):
    now = datetime.datetime.now()

    try:
        token_decoded = jwt.decode(token, getenv("SIGNATURE"))
    except jwt.exceptions.InvalidSignatureError:
        raise AcessoNegadoException("Falha na identificação da origem da autenticação.")

    if now > datetime.datetime.fromisoformat(token_decoded["expiration"]):
        raise AcessoNegadoException("Token expirado.")

    return token_decoded