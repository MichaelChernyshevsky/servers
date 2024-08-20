from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def addIntoDB(model):
    db.session.add(model)
    db.session.commit()

def getAllFromTable(table):
    print('/'*100)
    return db.query(table).all()

def getById(table,id):
    return db.get(table,id)

def getByFilter(table,filter):
    return db.query(table).filter(filter).all()

def deleteFromDB(element):
    db.delete(element)  
    db.commit()  