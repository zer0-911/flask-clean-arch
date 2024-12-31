from app import app
from app.controllers.userController import user_bp
from app.controllers.pageController import page_bp

app.register_blueprint(page_bp, url_prefix='/')
app.register_blueprint(user_bp, url_prefix='/users')
