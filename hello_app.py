from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Billy's Ranch"
    return "Sponsored by Action News; Bringing action to you!"
    return ""
    return "Billy's Ranch can be found in your local black market"
    return ""

if __name__ == "__main__":
    port = os.environ.get("PORT")
    app.run(
        "0.0.0.0"
    , port    
    )
