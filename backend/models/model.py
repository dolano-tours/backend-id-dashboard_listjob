# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from ..config.database import Base


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pekerjaan_id = Column(ForeignKey('pekerjaan.id'), primary_key=True, nullable=False, index=True)
    pekerja_id = Column(ForeignKey('pekerja.id'), primary_key=True, nullable=False, index=True)
    path_file = Column(Text, nullable=False)

    pekerja = relationship('Pekerja', primaryjoin='Document.pekerja_id == Pekerja.id', backref='documents')
    pekerjaan = relationship('Pekerjaan', primaryjoin='Document.pekerjaan_id == Pekerjaan.id', backref='documents')
    def to_dict(self):
        return{
            "id":self.id,
            "Pekerjaan id":self.pekerjaan_id,
            "pekerja id":self.pekerja_id,
            
            }


class Hasil(Base):
    __tablename__ = 'hasil'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pekerjaan_id = Column(ForeignKey('pekerjaan.id'), primary_key=True, nullable=False, index=True)
    pekerja_id = Column(ForeignKey('pekerja.id'), primary_key=True, nullable=False, index=True)
    path_file = Column(Text, nullable=False)

    pekerja = relationship('Pekerja', primaryjoin='Hasil.pekerja_id == Pekerja.id', backref='hasils')
    pekerjaan = relationship('Pekerjaan', primaryjoin='Hasil.pekerjaan_id == Pekerjaan.id', backref='hasils')
    def to_dict(self):
        return{
            "id":self.id,
            "Pekerjaan id":self.pekerjaan_id,
            "pekerja id":self.pekerja_id,
            
            }

class Pekerja(Base):
    __tablename__ = 'pekerja'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_employee = Column(Integer, nullable=False)
    tipe_pekerja_id = Column(ForeignKey('tipe_pekerja.id'), primary_key=True, nullable=False, index=True)

    tipe_pekerja = relationship('TipePekerja', primaryjoin='Pekerja.tipe_pekerja_id == TipePekerja.id', backref='pekerjas')
    def to_dict(self):
        return{
            "id":self.id,
            "id employee":self.id_employee,
            "tipe pekerja id":self.tipe_pekerja_id
            }


class Pekerjaan(Base):
    __tablename__ = 'pekerjaan'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pemberi_tugas_id = Column(ForeignKey('pekerja.id'), primary_key=True, nullable=False, index=True)
    pekerja_id = Column(ForeignKey('pekerja.id'), primary_key=True, nullable=False, index=True)
    nama = Column(String(45), nullable=False)
    status = Column(ENUM('approve', 'revisi', 'review'), nullable=False)

    pekerja = relationship('Pekerja', primaryjoin='Pekerjaan.pekerja_id == Pekerja.id', backref='pekerja_pekerjaans')
    pemberi_tugas = relationship('Pekerja', primaryjoin='Pekerjaan.pemberi_tugas_id == Pekerja.id', backref='pekerja_pekerjaans_0')

    def to_dict(self):
        return{
            "id":self.id,
            "pemberi tugas id":self.pemberi_tugas_id,
            "pekerja id":self.pekerja_id,
            "nama":self.nama,
            "status":self.status
          
        }



class TipePekerja(Base):
    __tablename__ = 'tipe_pekerja'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(15), nullable=False)
    
    def to_dict(self):
        return{
            "id":self.id,
            "nama":self.nama
        }
