from app.models import db

def upgrade():
    db.create_all()

def downgrade():
    db.drop_all()