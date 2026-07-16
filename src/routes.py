from flask import Blueprint, render_template, request, jsonify
from .openai_service import ai_service

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    system_prompt = data.get('system_prompt', 'You are a helpful assistant.')
    chat_history = data.get('history', [])

    result = ai_service.get_ai_response(user_message, system_prompt, chat_history)
    return jsonify(result)
