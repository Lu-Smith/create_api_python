from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == "_main_":
    app.run(debug=True)