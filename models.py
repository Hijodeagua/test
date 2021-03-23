def create_classes(db):
    class bars(db.Model):
        __tablename__ = 'project'

        brewery_id = db.Column(db.Varchar, primary_key=True)
        name = db.Column(db.Varchar)
        lat = db.Column(db.Decimal)
        lon = db.Column(db.Decimal)

        def __repr__(self):
            return '<bars %r>' % (self.name)
    return bars
