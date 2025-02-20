# FastAPI Auth JWT

Um sistema de autenticação utilizando **FastAPI**, **JWT** e **PassLib (bcrypt)** para o hash de senhas. Este projeto serve como base para a construção de APIs seguras e escaláveis, seguindo as recomendações de organização da documentação do FastAPI.

## Tecnologias Utilizadas

- **Python 3.12** (ou superior)
- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI para executar a aplicação
- **PyJWT** - Geração e verificação de tokens JWT
- **PassLib** - Criptografia de senhas (usando *bcrypt*)
- **bcrypt** - Biblioteca para hashing seguro de senhas

> **Observação:**  
> Os arquivos `__init__.py` podem estar vazios. Eles servem para definir as pastas como pacotes Python.

## Instalação

1. **Clone o repositório:**

    ```bash
      git clone https://github.com/seu-usuario/fastapi_auth_example.git
      cd fastapi_auth_example
    ```

2. Entre na pasta do projeto:
  ```bash
    python -m venv env
    source env/bin/activate
  ```

  ```bash
    python -m venv env
    env\Scripts\activate
  ```
3. Crie e ative um ambiente virtual:
- No Linux/Mac:

```bash
  python -m venv env
  source env/bin/activate
```

- No Windows:
```bash
  python -m venv env
  env\Scripts\activate
```

4. Instalar dependencias:
```bash
  pip install -r requirements.txt
```


## Como Iniciar a Aplicação
1. Execute a aplicação utilizando o Uvicorn:

```bash
  uvicorn app.main:app --reload
```

- Acesse a documentação interativa da API:
Abra o navegador e acesse http://127.0.0.1:8000/docs.

## Funcionalidades
Autenticação via JWT:
Utilize o endpoint /api/v1/auth/token para obter um token de acesso após realizar o login.

Proteção de Endpoints:
O endpoint /api/v1/auth/users/me retorna informações do usuário logado e está protegido, exigindo um token válido.

Criptografia de Senhas:
As senhas dos usuários são armazenadas de forma criptografada utilizando bcrypt via PassLib.

