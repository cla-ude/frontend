from flask import Flask
import os

app = Flask(__name__)
app.host = "0.0.0.0"
app.port = os.getenv("PORT") 

@app.route("/")
@app.route("/home")
def home():
  return "Hello, World!"

if __name__ == "__main__":
  app.run(host=app.host, port=app.port)
