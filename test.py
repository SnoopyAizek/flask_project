from app import create_app
from app import models, db
from sqlalchemy import select

app = create_app()
app.app_context().push()
try:
    stmt = select(models.User)
    user = db.session.execute(stmt)
    print(user.scalar())
except Exception:
    print('Ошибка')
