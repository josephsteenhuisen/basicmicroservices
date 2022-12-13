from flask import request, Flask
import json, socket

import sys
sys.path.insert(0,"..")

import my_imports.top

app = Flask(__name__)

#
# curl http://localhost:9000
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    email = request.json['email']
    number_of_at_signs = email.count("@")
    number_of_dot_signs = email.count(".")
    var1 = False
    var2 = False
    if email[0] == "@" or email[-1] == "@": var1 = True
    if number_of_dot_signs >= 1: var2 = True

    returnDictionary = {}
    returnDictionary["email"] = email
    returnDictionary["at_signs"] = number_of_at_signs
    returnDictionary["at_sign_at_end_or_beginning"] = var1
    returnDictionary["assert_dot_in_email"] = var2
    

    if number_of_at_signs == 1 and var1 == False and var2 == True:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
