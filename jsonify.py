from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/divide')
def divide():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 1))
        return jsonify(result=a / b)
    except ZeroDivisionError:
        return jsonify(error="Cannot divide by zero you silly!"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
