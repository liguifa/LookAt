class BaseService:
    def __init__(self):
        from .. import db
        self.db = db
