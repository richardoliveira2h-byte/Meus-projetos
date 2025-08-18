#Projeto semana 2


# Neste código e feito um Banco de dados com as informações de toda a turma.


# Instalação do Firebase Admin SDK (se necessário)
# !pip install firebase-admin


import firebase_admin
from firebase_admin import credentials, db


# Inicialização da conexão com o Firebase
cred = credentials.Certificate('/content/drive/MyDrive/FIREBASE/bancodd-f30da-firebase-adminsdk-fbsvc-1aa3fdaf5c.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bancodd-f30da-default-rtdb.firebaseio.com/'
})


# ---------------------------
# Aventureiros
# ---------------------------
aventureiros_ref = db.reference('/aventureiros')


aventureiros_ref.set({
    '001': {'nome': 'André Luiz', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '002': {'nome': 'Angelina Brito', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '003': {'nome': 'Arthur Silva', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Assombro'},
    '004': {'nome': 'Bruno Bonatto', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '005': {'nome': 'Cauê', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '006': {'nome': 'Enzo', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '007': {'nome': 'Eryck', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '008': {'nome': 'Giullia', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '009': {'nome': 'Guilherme Pescuma', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '010': {'nome': 'Lucas Mendes', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '011': {'nome': 'Lucas Souza', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '012': {'nome': 'Maria Luiza', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '013': {'nome': 'Nicole', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},
    '014': {'nome': 'NOME RESERVADO', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Vale do Espantalho'},  # Corrigido ID ausente
    '015': {'nome': 'Cauã', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '016': {'nome': 'Fábio', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '017': {'nome': 'Fernanda', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '018': {'nome': 'Gabriel', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '019': {'nome': 'Guilherme', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '020': {'nome': 'Gustavo', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '021': {'nome': 'João', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '022': {'nome': 'Maria Eduarda', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '023': {'nome': 'Raika', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'},
    '024': {'nome': 'Richard', 'classe': 'Aventureiro', 'nivel': 1, 'guilda': 'Aracna'}
})


# ---------------------------
# Missões Semanais
# ---------------------------
missoes_ref = db.reference('/missao_semanal')


missoes_ref.set({
    '001': {'nome': 'Tutorial', 'nome_boss': 'Espantalho', 'status': 'concluída'},
    '002': {'nome': 'Introdução', 'nome_boss': 'Goblins', 'status': 'concluída'},
    '003': {'nome': 'Introdução', 'nome_boss': 'Rei Goblin', 'status': 'concluída'}
})


# ---------------------------
# Ataques
# ---------------------------
ataque_ref = db.reference('/ataque')


ataque_ref.set({
    '001': {'espada_tipo': 'Espada Forte', 'dano_total': 2, 'ataca_em': '3,5,7', 'quantidade': 3},
    '002': {'espada_tipo': 'Espada Fraca', 'dano_total': 1, 'ataca_em': '3,5,7', 'quantidade': 9},
    '003': {'espada_tipo': 'Espada Forte', 'dano_total': 2, 'ataca_em': '1,3,5,7,9', 'quantidade': 5},
    '004': {'espada_tipo': 'Espada Fraca', 'dano_total': 1, 'ataca_em': '1,3,5,7,9', 'quantidade': 4}
})


# ---------------------------
# Estrelas
# ---------------------------
estrelas_ref = db.reference('/estrelas')


estrelas_ref.set({
    '001': {'id_aventureiros': '005', 'nome': 'Cauê', 'tipo_estrela': 'Roxa', 'quantidade': 2, 'ja_usou': False},
    '002': {'id_aventureiros': '018', 'nome': 'Gabriel', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': True},
    '003': {'id_aventureiros': '017', 'nome': 'Fernanda', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False},
    '004': {'id_aventureiros': '023', 'nome': 'Raika', 'tipo_estrela': 'Roxa', 'quantidade': 2, 'ja_usou': False},
    '005': {'id_aventureiros': '008', 'nome': 'Giullia', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False},
    '006': {'id_aventureiros': '022', 'nome': 'Maria Eduarda', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False},
    '007': {'id_aventureiros': '021', 'nome': 'João Matheus', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False},
    '008': {'id_aventureiros': '016', 'nome': 'Fábio', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False},
    '009': {'id_aventureiros': '010', 'nome': 'Lucas Mendes', 'tipo_estrela': 'Roxa', 'quantidade': 1, 'ja_usou': False}
})


# ---------------------------
# Classes
# ---------------------------
classes_ref = db.reference('/classes')


classes_ref.set({
    '001': {'nome_classe': 'Guerreiro', 'vida_p_m': 5, 'status': 'ativa'},
    '002': {'nome_classe': 'Artificier', 'vida_p_m': 4, 'status': 'ativa'},
    '003': {'nome_classe': 'Mago', 'vida_p_m': 2, 'status': 'ativa'},
    '004': {'nome_classe': 'Mercador', 'vida_p_m': 3, 'status': 'ativa'},
    '005': {'nome_classe': 'Herói', 'vida_p_m': 0, 'status': '

