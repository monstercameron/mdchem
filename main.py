from config.config import app
from services.require_login import require
from routes.index import simple_page
from routes.login import login
from routes.register import register
from routes.recover import recover
from routes.contact import contact
from routes.admin import admin
from routes.logout import logout
from API.rest import all_users
from API.users import users
from API.save import save
from API.news import news

app.register_blueprint(require)
app.register_blueprint(simple_page)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(recover)
app.register_blueprint(contact)
app.register_blueprint(admin)
app.register_blueprint(all_users)
app.register_blueprint(users, url_prefix='/api/')
app.register_blueprint(save, url_prefix='/api/')
app.register_blueprint(news, url_prefix='/api/')


if __name__ == '__main__':
    app.run()
