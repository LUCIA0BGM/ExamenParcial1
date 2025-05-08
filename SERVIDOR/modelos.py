from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Crear la base de datos
engine = create_engine("sqlite:///base_datos.db", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class ResultadoNReinas(Base):
    __tablename__ = 'resultados_nreinas'
    id = Column(Integer, primary_key=True)
    tamanio = Column(Integer)
    resuelto = Column(Boolean)
    pasos = Column(Integer)
    fecha = Column(DateTime, default=datetime.now)

class ResultadoCaballo(Base):
    __tablename__ = 'resultados_caballo'
    id = Column(Integer, primary_key=True)
    posicion_inicial = Column(String)
    movimientos = Column(Integer)
    completo = Column(Boolean)
    fecha = Column(DateTime, default=datetime.now)

class ResultadoHanoi(Base):
    __tablename__ = 'resultados_hanoi'

    id = Column(Integer, primary_key=True)
    discos = Column(Integer)  # Número de discos
    movimientos = Column(Integer)  # Número de movimientos realizados
    resuelto = Column(Boolean)  # Si el juego fue resuelto o no

    def __init__(self, discos, movimientos, resuelto):
        self.discos = discos
        self.movimientos = movimientos
        self.resuelto = resuelto
