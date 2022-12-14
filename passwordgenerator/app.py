from flask import request, Flask
import json, socket

import string
import random


app = Flask(__name__)

#
# curl http://localhost:9003
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"password\" : \"10\" }" -X POST http://localhost:9003/check  -H "Content-type: application/json"
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    password = request.json['password']
    password_l = int(password)

    char_list = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "?"]

    new_password = ""

    for i in range(password_l):
      char = random.randint(0, len(char_list))
      new_password = new_password + char_list[char]
      

  

    returnDictionary = {}
    returnDictionary["password"] = new_password
    returnDictionary["length"] = password_l

    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)
