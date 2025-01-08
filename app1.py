import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
        <div class="header">
            <h1>All Set 👍✅!</h1>
            <p class="subheading">Made with 💕 in India</p>
        </div>
    </center>
    <style>
        body {
            background: linear-gradient(to bottom, #6a11cb, #2575fc);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
            color: white;
        }
        .header {
            text-align: center;
            animation: fadeIn 3s ease-out;
        }
        h1 {
            font-size: 4em;
            font-weight: bold;
            animation: slideIn 2s ease-out;
        }
        .subheading {
            font-size: 1.5em;
            margin-top: 10px;
            font-style: italic;
            color: #ffeb3b;
            animation: fadeInUp 2s ease-out;
        }
        footer {
            text-align: center;
            padding: 15px;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            font-size: 1.3em;
            position: absolute;
            width: 100%;
            bottom: 0;
        }
        footer a {
            color: #ffeb3b;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        @keyframes slideIn {
            0% { transform: translateY(-50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        @keyframes fadeInUp {
            0% { transform: translateY(50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
    </style>
    <footer>
        <p>Made with 💕 in India | <a href="#">Visit us</a></p>
    </footer>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
