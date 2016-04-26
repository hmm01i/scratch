from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    msg = "ESP Sensor"
    return msg

@app.route("/api/v1/temp")
def temp():
    msg = "71"
    return msg

@app.route("/api/v1/humid")
def humid():
    msg ="humidity: 83%"
    return msg

@app.route("/api/v1/firmware")
def firmware():
    msg ="Firmware: 0.1.2"
    return msg

if __name__ == "__main__":
    app.run(debug=True)
