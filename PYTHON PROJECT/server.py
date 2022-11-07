print("server file running")
from flask_app import app
from flask_app.controllers import display_controllers
from flask_app.controllers import dashboard_controllers
# EDIT CONTROLLERS
# FLASK_APP_API_KEY=RANDOMAPIKEY

# client ID
# xDt4_emqahl9YBaRVGDkvw

# API KEY
# hQD93KZujlrqW8RqMZh70FJw99u_bO-K5YXJE0aQG_ob5YQcczn2J-Xvyh7hmzifQ8cXlkHz8aENf8O9SFkAaO21CJPlUV7_cW5wv38-mLF7d9IQAncylG8FbNsGY3Yx

import requests
import json

import os
print( os.environ.get("FLASK_APP_API_KEY") )

            
if __name__ == "__main__":
    app.run(debug=True) 