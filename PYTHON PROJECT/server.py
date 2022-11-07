print("server file running")
from flask_app import app
from flask_app.controllers import display_controllers
from flask_app.controllers import dashboard_controllers
# EDIT CONTROLLERS



import requests
import json

import os
print( os.environ.get("FLASK_APP_API_KEY") )

            
if __name__ == "__main__":
    app.run(debug=True) 
