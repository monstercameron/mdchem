from config.config import app
from routes.index import simple_page
from routes.login import login
from API.rest import all_users


app.register_blueprint(simple_page)
app.register_blueprint(login)
app.register_blueprint(all_users)


if __name__ == '__main__':
    app.run()
