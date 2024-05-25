from flask import Blueprint, jsonify
from backend.models.Motivation import Motivation

motivation_routes = Blueprint('motivation_routes', __name__)

# Endpoint for fetching a list of motivation sentences
@motivation_routes.route('/motivation', methods=['GET'])
def get_motivation_sentences():
    # Fetch the motivation sentences from the database or any other data source
    sentences = Motivation.get_all_sentences()

    # Return the list of motivation sentences as JSON response
    return jsonify(sentences)

# Endpoint for adding a new motivation sentence
@motivation_routes.route('/motivation', methods=['POST'])
def add_motivation_sentence():
    # Get the new motivation sentence from the request body
    sentence = request.json.get('sentence')

    # Create a new instance of the Motivation class with the sentence
    new_sentence = Motivation(sentence)

    # Save the new sentence to the database or any other data source
    new_sentence.save()

    # Return a success message as JSON response
    return jsonify({'message': 'Motivation sentence added successfully'})

# Endpoint for deleting a motivation sentence
@motivation_routes.route('/motivation/<int:sentence_id>', methods=['DELETE'])
def delete_motivation_sentence(sentence_id):
    # Delete the motivation sentence with the given ID from the database or any other data source
    Motivation.delete_sentence(sentence_id)

    # Return a success message as JSON response
    return jsonify({'message': 'Motivation sentence deleted successfully'})