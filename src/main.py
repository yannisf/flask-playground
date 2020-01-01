from flask import Flask, request, jsonify

print("Flask server")

app = Flask(__name__)


@app.route('/')
def index():
    return "root"


@app.route("/app/api/v1/string/<value>")
def act1(value):
    return value


@app.route("/app/api/v1/int/<int:value>")
def act2(value):
    return str(value)


@app.route("/app/api/v1/get", methods=['GET'])
def act3():
    value = request.args['q']
    return str(value)


@app.route("/app/api/v1/post", methods=['POST'])
def act4():
    val1 = request.form.get('key1')
    val2 = request.form.get('key2')
    rmap = {'key1': val1, 'key2': val2}
    return jsonify(rmap)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

