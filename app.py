from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        data = request.get_json()
        code = data.get("code")
        
        mal_keywords = set(['os','subprocess','sys','shutil','pathlib'])
        for i in code.split():
            if i in mal_keywords:
                return jsonify({"error" : "Malicious Code Detected",'details':"Please write ethical code."})
        
        
        if not code:
            return jsonify({"error": "No code provided",'details': "Please provide some code"})
            
        result = subprocess.run(
            ['python', '-c', code],
            text=True,
            capture_output=True,
            timeout=5
        )        

        if result.returncode:
            return jsonify({
                "error": "Error in code",
                "details": result.stderr
            })
        

        return jsonify({
            "output": result.stdout
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Time Limit Exceeded"})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
