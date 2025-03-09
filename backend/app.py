from flask import Flask
from flask_cors import CORS  
from api.api import api

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
# Register the API Blueprint
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)

