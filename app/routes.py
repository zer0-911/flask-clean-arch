from app import app
from app.controllers.userController import user_bp

app.register_blueprint(user_bp, url_prefix='/users')