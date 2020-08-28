from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "Dummy Load Test with Locust - Scalable"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
