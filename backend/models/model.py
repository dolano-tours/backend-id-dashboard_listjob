# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class Aset(Base):
    __tablename__ = 'aset'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pekerjaan_id = Column(ForeignKey('pekerjaan.id'), primary_key=True, nullable=False, index=True)
    path_file = Column(Text, nullable=False)
    is_hasil = Column(ENUM('HASIL', 'DOKUMEN', 'REVIEW'), nullable=False)
    pekerjaan = relationship('Pekerjaan', primaryjoin='Aset.pekerjaan_id == Pekerjaan.id', backref='asets')
    def to_dict(self):
        return{
            "id":self.id,
            "pekerjaan_id":self.pekerjaan_id,
            "path_file":self.path_file,
            "is_hasil":self.is_hasil
        }


class Pekerja(Base):
    __tablename__ = 'pekerja'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(Integer, nullable=False)
    nama_pekerja = Column(String(45), nullable=False)
    def to_dict(self):
        return{
            "id":self.id,
            "id_employee":self.id_employee,
            "nama_pekerja":self.nama_pekerja
        }
    



class PekerjaPekerjaan(Base):
    __tablename__ = 'pekerja_pekerjaan'

    pekerjaan_id = Column(ForeignKey('pekerjaan.id'), primary_key=True, nullable=False, index=True)
    pekerja_id = Column(ForeignKey('pekerja.id'), primary_key=True, nullable=False, index=True)
    position = Column(ENUM('pekerja', 'pembantu', 'petugas'), nullable=False)

    pekerja = relationship('Pekerja', primaryjoin='PekerjaPekerjaan.pekerja_id == Pekerja.id', backref='pekerja_pekerjaans')
    pekerjaan = relationship('Pekerjaan', primaryjoin='PekerjaPekerjaan.pekerjaan_id == Pekerjaan.id', backref='pekerja_pekerjaans')
    def to_dict(self):
        return{
            "pekerjaan_id":self.pekerjaan_id,
            "pekerja_id":self.pekerja_id,
            "position":self.position
            
        }

class Pekerjaan(Base):
    __tablename__ = 'pekerjaan'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(45), nullable=False)
    def to_dict(self):
        return{
            "id":self.id,
            "nama":self.nama
        }


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pekerjaan_id = Column(ForeignKey('pekerjaan.id'), primary_key=True, nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False)
    type = Column(ENUM('available', 'started', 'approved', 'amend', 'review'), nullable=False)
    due_date = Column(DateTime, nullable=False)

    pekerjaan = relationship('Pekerjaan', primaryjoin='Pekerjaan.id == Status.pekerjaan_id', backref='statuses')
    def to_dict(self):
        return{
            "id":self.id,
            "pekerjaan_id":self.pekerjaan_id,
            "timestamp":self.timestamp,
            "type":self.type,
            "due_date":self.due_date
        }