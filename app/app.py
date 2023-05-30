@app.route('/generate_python_code', methods=['GET', 'POST'])
def generate_python_code():
    if request.method == 'POST':
        data = request.form
        user_story = data.get('user_story')
        python_code = generate_python_code_from_user_story(user_story)
        if python_code:
            return jsonify({'status': 'success', 'result': python_code})
        else:
            return jsonify({'status': 'failed', 'message': 'Failed to generate python code'})
    else:
        return jsonify({'status': 'failed', 'message': 'Invalid request method'})