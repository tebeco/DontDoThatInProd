from flask import Flask
app = Flask(__name__)

Alive = True
Healthy = True

@app.route("/")
def hello():
    return "Hello World from python!"

@app.route("/live")
def live():
    global Alive
    if Alive:
        return ("I am alive", 200)
    else:
        return ("I am dead", 503)

@app.route("/kill")
def kill():
    global Alive
    Alive = False
    return "The Liveness probe should now be down"

@app.route("/health")
def health():
    global Healthy
    if Healthy:
        return ("I am Healthy", 200)
    else:
        return ("I am not healthy", 503)

@app.route("/down")
def down():
    global Healthy
    Healthy = False
    return "The Readiness probe should now be down"

@app.route("/up")
def up():
    global Healthy
    Healthy = True
    return "The Readiness probe should now be up"

if __name__ == "__main__":
    app.run()

