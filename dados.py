from pymongo import ASCENDING, MongoClient
CONNECTION_STRING = "mongodb+srv://cassino:cassino@cluster0.rjggj.mongodb.net/betano?retryWrites=true&w=majority"

def SelecionaTodosSinais(tipo):
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('registros')
    return registros.find({'type' : tipo}).sort([('created_at', ASCENDING)])


def selecionaTodosClientes():
    client = MongoClient(CONNECTION_STRING)
    db =  client['betano']
    registros = db.get_collection('clientes')
    return registros.find({})



def inserirNovoUsuario(chat_id):
    client = MongoClient(CONNECTION_STRING)
    db = client['betano']
    clientes = db.get_collection('clientes')
    clientes.delete_one({'chat_id' : chat_id})
    clientes.insert_one({'chat_id' : chat_id})