from flask import Flask, request
from flask_cors import CORS
import pywhatkit

app= Flask(__name__)
CORS(app)

def addToMinutes(minute):
    return int(minute) + 2

@app.route('/')
def index():
  return "<h1>Welcome to CodingX</h1>"

@app.route('/get-message', methods=["POST"])
def getMessages():
    return ""

@app.route("/send-user-message", methods=['POST'])    
def sendUserMsg():
    pywhatkit.sendwhatmsg_instantly('+541161427148',"hello")
    print("Msg send")
    return "user-send-msg"

@app.route('/send-message', methods=["POST"])
def sendMsg():
    request_data = request.get_json()
    cel = request_data['cel']
    user = request_data['user']
    comercio = request_data['comercio']
    now = request_data['now']

    hora = now.split(':')[0]
    min = addToMinutes(now.split(':')[1])
    pywhatkit.sendwhatmsg('+5411' + str(cel), str(user) + ' gracias por comprar en ' + str(comercio) , int(hora),int(min))
    return '<h2>Mensaje enviado con exito</h2>'

if __name__ == "__main__":
  app.run(debug=True)