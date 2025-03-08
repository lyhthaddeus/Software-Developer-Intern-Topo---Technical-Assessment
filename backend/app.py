from flask import Flask
from api.api import api

app = Flask(__name__)

# Register the API Blueprint
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)

