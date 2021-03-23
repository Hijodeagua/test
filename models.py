def create_classes(db):
    class bars(db.Model):
        __tablename__ = 'breweries'

        brewery_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)

        def __repr__(self):
            return '<breweries %r>' % (self.name)
    return bars
