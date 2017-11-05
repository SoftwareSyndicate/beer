from flask import Flask
import routes
app = Flask(__name__)

routes.bind_routes(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"
