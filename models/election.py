# -*- coding: utf-8 -*-

from sqlalchemy import CHAR, Column, Enum, Integer
from sqlalchemy.orm import backref, relationship
from models.base import Base

class Election(Base):
    __tablename__ = 'election'

    id = Column(Integer, autoincrement=True, primary_key=True)
    type = Column(Enum('assembly', 'mayor', 'president', name='enum_election_type'), nullable=False, index=True)
    nth = Column(Integer, nullable=False, index=True)
    date = Column(CHAR(8), index=True)

    candidates = relationship('Candidacy',
            primaryjoin='and_(Candidacy.election_id==Election.id)',
            backref=backref('election', lazy=False))
    winners = relationship('Candidacy',
            primaryjoin='and_(Candidacy.election_id==Election.id,'
                             'Candidacy.is_electied==True)')


