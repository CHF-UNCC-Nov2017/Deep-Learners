from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from train import * 
from numpy import * 

app = Flask(__name__)
api = Api(app)



class PaaS(Resource):
    def get(self):
        return jsonify({"testing": "Hello World!"}) 
 
    def put(self):
        data = request.json['data']
        r = LR()
        r.fit()
        result= r.predict([data])
        result = result.tolist()
        print result 
        return jsonify(result)

api.add_resource(PaaS, '/paas/regression')


if __name__ == '__main__':
    app.run(debug=True)


