from flask import Flask, jsonify
from models.Motivation import Motivation

app = Flask(__name__)

# Sample motivation sentences
motivations = [
    Motivation(1, "You can do it!"),
    Motivation(2, "Believe in yourself."),
    Motivation(3, "Stay focused and never give up."),
    Motivation(4, "Success is just around the corner."),
    Motivation(5, "Keep pushing forward."),
]

@app.route('/motivations', methods=['GET'])
def get_motivations():
    return jsonify([motivation.__dict__ for motivation in motivations])

if __name__ == '__main__':
    app.run()