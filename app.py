from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/sub',methods=['GET'])
def jkfjk():
    try:
        a=int(request.args.get('num1'))
        b=int(request.args.get('num2'))
        t=a+b
    except:
        return jsonify({'Error':'invalid data'})
    return jsonify({'Answer':t})