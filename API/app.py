from os import getenv
from flask import Flask, request
from flask_cors import CORS
import json
import jwt
from common.auth_utils import check_password, check_token, generate_token
from common.code_utils import exception_handler
from api_usuarios.src.service.service_factory import get_aluno_service
from api_usuarios.src.model.form.aluno_form import AlunoForm
from api_usuarios.src.model import mapper as mapper_aluno
from api_documentos.src.model import mapper as mapper_doc
from api_documentos.src.model.form.documento_form import DocumentoForm
from api_documentos.src.service.service_factory import get_documento_service

app = Flask(__name__)

CORS(app)

@app.route("/api/alunos", methods=["POST"])
@exception_handler
def cadastrar_aluno():
    service = get_aluno_service()
    aluno_form = AlunoForm(**request.json)
    aluno = mapper_aluno.form_to_aluno(aluno_form)
    service.persistir_aluno(aluno)
    return "", 204
    

@app.route("/api/autenticar", methods=["POST"])
@exception_handler
def recuperar_aluno():

    dados_aluno = request.json

    service = get_aluno_service()
    aluno = service.recuperar_aluno(dados_aluno["user"])
    check_password(dados_aluno["senha"], aluno.senha)
    aluno_dto = mapper_aluno.aluno_to_dto(aluno)

    token = generate_token(aluno_dto)

    return json.dumps({"token": token}), 200


@app.route("/api/documentos", methods=["GET"])
@exception_handler
def recuperar_documentos():

    token = request.headers.get("Authorization").split()[1]
    check_token(token)

    service = get_documento_service()

    documentos = service.recuperar_documentos()
    documentos_dto = list(map(lambda x: mapper_doc.documento_to_dto(x).__dict__, documentos))

    return json.dumps({"data": documentos_dto}), 200


@app.route("/api/documentos", methods=["POST"])
@exception_handler
def publicar_documento():
    
    token = request.headers.get("Authorization").split()[1]
    registro_criador = check_token(token)["registro"]

    service = get_documento_service()

    documento_form = request.json
    documento_form["registro_criador"] = registro_criador
    documento = mapper_doc.form_to_documento(DocumentoForm(**documento_form))

    service.persistir_documento(documento)

    return "", 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=getenv('PORT'))
    
