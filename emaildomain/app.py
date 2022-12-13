from flask import request, Flask
import json, socket

import sys
sys.path.insert(0,"..")

import my_imports.top

app = Flask(__name__)

#
# curl http://localhost:9002
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9002/check
#
@app.route("/check", methods=["POST"])
def compute():

    hostName = socket.gethostname()
    email = request.json['email']
    var = False

    A =[ "gmail.com"	,
		"yahoo.com"	,
    "outlook.com",
		"hotmail.com",	
		"aol.com"	,
		"hotmail.co.uk",	
		"hotmail.fr",	
		"msn.com"	,
		"yahoo.fr"	,
		"orange.fr"	,
		"comcast.net"]

    for i in range(len(A)):
      if email.count(A[i]) > 0:
        var = True

    returnDictionary = {}
    returnDictionary["email"] = email

    if var >= 1:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
