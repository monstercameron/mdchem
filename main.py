from config.config import app
import routes.index as index

@app.route('/', methods=['GET'])
def index():
    return 'test'

if __name__ == '__main__':
    app.run()
