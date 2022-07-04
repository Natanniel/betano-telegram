from pymongo import ASCENDING, DESCENDING, MongoClient
#CONNECTION_STRING = "mongodb+srv://cassino:cassino@cluster0.rjggj.mongodb.net/betano?retryWrites=true&w=majority"
CONNECTION_STRING = "mongodb://localhost:27017/betano"

def SelecionaTodasRoletas():
    

    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    roletas = db.get_collection('roletas')
    dados = roletas.find()    
    return dados

def excluirSinais(roleta):
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    roletas = db.get_collection('roletas')
   # roletas.update_one({'roletas.nome' : roleta},{"$set": { "roletas.$.resultados": [] }},upsert=True)
    


def SelecionaTodosSinais(roleta):
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('roletas')
    return registros.find({'roletas.nome' : roleta}).sort([('created_at', DESCENDING)]).limit(30)




def SelecionaEstrategias():
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('estrategias')
    return registros.find({})


def SelecionaSinalExistente(tipo,nomeRoleta):
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('sinal')
    return registros.find({'tipo':tipo , 'roleta' : nomeRoleta, 'ativo': 1 })


def inserirSinal(tipo,nomeRoleta):
    client = MongoClient(CONNECTION_STRING)
    db = client['betano']
    sinais = db.get_collection('sinal')
    sinais.insert_one({'tipo':tipo , 'roleta' : nomeRoleta, 'ativo': 1, 'status': 1, 'jogadas':0 })

def confirmaSinal(tipo,nomeRoleta,jogadas):
    client = MongoClient(CONNECTION_STRING)
    db = client['betano']
    sinais = db.get_collection('sinal')
    sinais.update_one({'tipo':tipo , 'roleta' : nomeRoleta.replace('-',' ') },  {"$set": {'status': 2, 'jogadas': jogadas}} )


def resultadoSinal(tipo,nomeRoleta,resultado):
    client = MongoClient(CONNECTION_STRING)
    db = client['betano']
    sinais = db.get_collection('sinal')
    sinais.update_one({'tipo':tipo , 'roleta' : nomeRoleta.replace('-',' ') },  {"$set": {'ativo': 2, 'status' : resultado }} )
    
    db2 = client['betano']    
    registros = db2.get_collection('registros')
    registros.delete_many({"roulette": nomeRoleta })

def selecionaTodosClientes():
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('clientes')
    return registros.find({})



def inserirNovoUsuario(chat_id,hash):
    client = MongoClient(CONNECTION_STRING)
    db = client['betano']
    clientes = db.get_collection('grupos')
    clientes.delete_one({'chat_id' : chat_id})
    clientes.insert_one({'chat_id' : chat_id})

