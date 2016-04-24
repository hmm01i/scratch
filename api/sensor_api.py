from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    msg = "ESP Sensor!\n\
          Firmware: 0.1.2\n\
          (c) Jacob Sohl\n\
          MIT License"
    return msg

if __name__ == "__main__":
    app.run()
