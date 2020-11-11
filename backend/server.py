import random
from flask import Flask, jsonify

app = Flask(__name__)

excuses = [
    {
        'category': 'late',
        'excuse': 'Sorry I\'m late, I was stuck in traffic'
    }, 
    {
        'category': 'late', 
        'excuse': 'I swear it wasn\'t my fault my neighbour forced me to stay in bed.'
    },
    {
        'category': 'skip_event',
        'excuse': 'I can\'t come, I have to go fishing in the morning.'
    },
    {
        'category': 'homework',
        'excuse': 'My dog ate my homework.'
    },
    {
        'category': 'homework',
        'excuse': 'I didn\'t do my homework because this isn\'t the homework you\'re looking for'
    }
]

@app.route('/api/v1/excuse', methods=['GET'])
@app.route('/api/v1/excuse/<category>', methods=['GET'])
def get_excuse(category='random'):
    if category == 'random':
        return jsonify(random.choice(excuses))
    else:
        return jsonify(random.choice([excuse for excuse in excuses if excuse['category'] == category])) 

if __name__ == '__main__':
    app.run()