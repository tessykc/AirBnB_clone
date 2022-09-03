#!/usr/bin/python3

class City(BaseModel, Base):
    """Representationof of City"""
    if models.storage_t == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), name = models.ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullabe=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)