#
#
#
from flask import request, Flask
import json, socket


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
# curl -d "{ \"password\" : \"xxxxxxxx\" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"
#

#password should be 8 or more characters and have a capital letter and number

@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    password = request.json['password']
    password_length = len(password)
    
    var1 = False
    var2 = False
    
    for i in range(password_length):
        if(password[i]>='A' and password[i]<='Z'):
            var1 = True
    for i in range(10):
        n = str(i)
        for j in range(password_length):
            if (password[j] == n):
                var2 = True

    returnDictionary = {}
    returnDictionary["password"] = password
    returnDictionary["length"] = password_length
    returnDictionary["contains_number"] = var2
    returnDictionary["contains_uppercase_letter"] = var1

    if password_length >= 8 and var1 == True and var2 == True:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
