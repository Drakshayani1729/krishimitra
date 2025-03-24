from flask import Flask, jsonify
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    if os.environ.get('FLASK_ENV') == 'development':
        CORS(app)
    else:
        CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Add root route directly to the app
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to KrishiMitra API"})
    
    # Register the API blueprint
    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app