from flask import Flask, request, jsonify
app = Flask(__name__)
machines = ['Machine1', 'Machine2', 'Machine3']
@app.route('/machines', methods=['GET'])
def get_machines():
    return jsonify(machines)
if __name__ == '__main__':
    app.run(debug=True)