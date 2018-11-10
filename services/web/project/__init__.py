from flask import Flask,jsonify


#instantiate the app 
app = Flask(__name__)

#set the configuration
app.config.from_object('config.DevelopmentConfig')

@app.route('/',methods=['GET'])
def home():
    return jsonify(
        {
            'status':'success',
            'message' : 'pong'
        }
    )

