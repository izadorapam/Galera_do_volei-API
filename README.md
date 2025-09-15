# 🚀 Projeto Galera do Vôlei - API

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Este projeto consiste em uma **API para organização de partidas e comunidade Galera do Vôlei**, desenvolvida com **FastAPI**. A API permite cadastro de jogadores, criação de partidas, adesão, avaliações e rankings de organizadores.

---

## 🎯 Funcionalidades Principais

- Cadastro de jogadores
- Criação de partidas
- Solicitação e aprovação de adesão
- Listagem de partidas abertas
- Desistência de partidas
- Encerramento de partidas
- Avaliação de partidas e jogadores
- Ranking de organizadores
- Sistema de convites para novos usuários

---

## 🛠️ Pré-requisitos

- Python 3.10 ou superior
- Git (opcional, caso clone o repositório)

---

## ⚙️ Configuração do Ambiente

### 1. Criar ambiente virtual (`venv`)
```
python -m venv venv

.\venv\Scripts\Activate

pip install fastapi uvicorn pydantic[email]

uvicorn main:app --reload

```

## 📚 Documentação Interativa
### Swagger UI:
```
http://127.0.0.1:8000/docs
```
### Redoc:
```
http://127.0.0.1:8000/redoc





