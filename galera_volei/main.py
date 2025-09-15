from fastapi import FastAPI, Path, Query, status, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, List

app = FastAPI(
    title="Galera do Vôlei API",
    version="1.0.0",
    description="API para organização de partidas e comunidade Galera do Vôlei"
)

# ---------------------------
# MODELOS
# ---------------------------
class Jogador(BaseModel):
    nome: str
    sexo: str
    idade: int
    categoria: str

class Partida(BaseModel):
    local: str
    data: str  # formato "YYYY-MM-DD"
    categoria: str
    tipo: str

class Adesao(BaseModel):
    jogador_id: int

class AprovarAdesao(BaseModel):
    status: str  # "Aprovado" ou "Rejeitado"

class AvaliacaoPartida(BaseModel):
    jogador_id: int
    nota: int
    comentario: Optional[str]

class AvaliacaoJogador(BaseModel):
    organizador_id: int
    jogador_id: int
    nota: int

class Convite(BaseModel):
    email: EmailStr
    responsavel_id: int

class AceitarConvite(BaseModel):
    nome: str
    sexo: str

# ---------------------------
# RAIZ / HOME
# ---------------------------
@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"mensagem": "API Galera do Vôlei rodando!"}

# ---------------------------
# ENDPOINTS JOGADORES
# ---------------------------
@app.post("/jogadores", status_code=status.HTTP_201_CREATED)
def criar_jogador(jogador: Jogador):
    # Validações
    if jogador.idade < 10:
        raise HTTPException(status_code=400, detail="Jogador deve ter no mínimo 10 anos")
    if jogador.sexo not in ["Masculino", "Feminino", "M", "F"]:
        raise HTTPException(status_code=400, detail="Sexo inválido")
    return {"id": 1, "nome": jogador.nome, "sexo": jogador.sexo, "categoria": jogador.categoria}

# ---------------------------
# ENDPOINTS PARTIDAS
# ---------------------------
@app.post("/partidas", status_code=status.HTTP_201_CREATED)
def criar_partida(partida: Partida):
    if not partida.local or not partida.data:
        raise HTTPException(status_code=400, detail="Local e data são obrigatórios")
    return {"id": 10, "local": partida.local, "situacao": "Nova"}

@app.post("/partidas/{id}/adesao", status_code=status.HTTP_200_OK)
def solicitar_adesao(id: int, adesao: Adesao):
    if adesao.jogador_id <= 0:
        raise HTTPException(status_code=400, detail="ID do jogador inválido")
    return {"mensagem": "Pedido enviado", "status": "Pendente"}

@app.put("/partidas/{id}/adesao/{id_jogador}", status_code=status.HTTP_200_OK)
def aprovar_adesao(id: int, id_jogador: int, aprovacao: AprovarAdesao):
    if aprovacao.status not in ["Aprovado", "Rejeitado"]:
        raise HTTPException(status_code=400, detail="Status inválido")
    mensagem = "Jogador aprovado" if aprovacao.status == "Aprovado" else "Jogador rejeitado"
    return {"mensagem": mensagem}

@app.get("/partidas", status_code=status.HTTP_200_OK)
def listar_partidas(status: str = Query(..., example="Em_Adesao")):
    return [{"id": 10, "local": "IFPI Quadra A", "data": "2023-09-15"}]

@app.delete("/partidas/{id}/desistencia", status_code=status.HTTP_200_OK)
def desistir_partida(id: int, adesao: Adesao):
    if adesao.jogador_id <= 0:
        raise HTTPException(status_code=400, detail="ID do jogador inválido")
    return {"mensagem": "Jogador retirado da partida"}

@app.put("/partidas/{id}/encerrar", status_code=status.HTTP_200_OK)
def encerrar_partida(id: int):
    return {"id": id, "situacao": "Encerrada"}

@app.post("/partidas/{id}/avaliacao", status_code=status.HTTP_200_OK)
def avaliar_partida(id: int, avaliacao: AvaliacaoPartida):
    if not (1 <= avaliacao.nota <= 5):
        raise HTTPException(status_code=400, detail="Nota deve ser entre 1 e 5")
    return {"mensagem": "Avaliação registrada"}

@app.post("/partidas/{id}/avaliacao_jogador", status_code=status.HTTP_200_OK)
def avaliar_jogador(id: int, avaliacao: AvaliacaoJogador):
    if not (1 <= avaliacao.nota <= 5):
        raise HTTPException(status_code=400, detail="Nota deve ser entre 1 e 5")
    return {"mensagem": "Avaliação registrada"}

# ---------------------------
# ENDPOINTS RANKING
# ---------------------------
@app.get("/ranking/organizadores", status_code=status.HTTP_200_OK)
def ranking_organizadores():
    return [{"organizador": "Carlos", "media": 4.7}]

# ---------------------------
# ENDPOINTS CONVITES
# ---------------------------
@app.post("/convites", status_code=status.HTTP_201_CREATED)
def enviar_convite(convite: Convite):
    return {"mensagem": "Convite enviado"}

@app.post("/convites/{token}/aceitar", status_code=status.HTTP_201_CREATED)
def aceitar_convite(token: str, convidado: AceitarConvite):
    if convidado.sexo not in ["Masculino", "Feminino", "M", "F"]:
        raise HTTPException(status_code=400, detail="Sexo inválido")
    return {"id": 7, "nome": convidado.nome, "responsavel_id": 3}
