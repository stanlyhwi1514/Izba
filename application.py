from create_app import create_app
import os

from dotenv import load_dotenv
import os

load_dotenv()

print("DB URI loaded from .env:", os.getenv("SQLALCHEMY_DATABASE_URI"))


config_name = os.getenv('APP_ENV', 'development') 
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
