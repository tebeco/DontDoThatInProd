from flask import Flask
app = Flask(__name__)

global Alive = True
global Healthy = True

@app.route("/")
def hello():
    return "Hello World from python!"

@app.route("/live")
def live():
    if Alive:
        return ("I am alive", 200)
    else:
        return ("I am dead", 503)

@app.route("/kill")
def kill():
    Alive = False
    return "The Liveness probe should now be down"

@app.route("/health")
def health():
    if Healthy:
        return ("I am Healthy", 200)
    else:
        return ("I am not healthy", 503)

@app.route("/down")
def down():
    Healthy = False
    return "The Readiness probe should now be down"

@app.route("/up")
def up():
    Healthy = True
    return "The Readiness probe should now be up"

if __name__ == "__main__":
    app.run()

