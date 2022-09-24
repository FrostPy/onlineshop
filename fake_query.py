from app import db
from app.models import Brand


brands_list = Brand.query.all()
db.session.delete(brands_list[0])
db.session.commit()