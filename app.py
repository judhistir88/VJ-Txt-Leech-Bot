import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
    <div class="header">
        <h1>Text 2 Leech</h1>
    </div>
    <div class="art-container">
        <div class="hero-content">
            <h2>All Set 👍✅!
        🟥🟥🟥🟧🟧🟧🟨🟨🟨</h2>
        </div>
    </div>
    </center>
    <style>
        body {
            background: linear-gradient(to bottom, #ff6a00, #ee0979);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
            color: white;
            overflow: hidden;
            position: relative;
        }

        .header {
            text-align: center;
            animation: fadeIn 2s ease-out;
        }

        h1 {
            font-size: 4em;
            font-weight: bold;
            animation: slideIn 2s ease-out;
        }

        .art-container {
            position: relative;
            width: 100%;
            height: 60%;
            margin-top: 50px;
            z-index: 10;
        }

        .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            z-index: 2;
            animation: fadeInUp 2s ease-out;
        }

        .hero-content h2 {
            font-size: 3em; /* Increased font size */
            font-weight: bold; /* Made font bold */
            margin: 0;
        }

        /* Double Exposure Effect */
        .double-exposure {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://source.unsplash.com/featured/?nature,landscape');
            background-size: cover;
            opacity: 0.3;
            pointer-events: none;
            z-index: 1;
            animation: doubleExposure 15s ease-in-out infinite;
        }

        /* Keyframes for Animation */
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

        @keyframes doubleExposure {
            0% { opacity: 0.3; }
            50% { opacity: 0.6; }
            100% { opacity: 0.3; }
        }

        /* Particle Animation */
        .particle {
            position: absolute;
            width: 10px;
            height: 10px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: particleMovement 4s infinite ease-in-out;
        }

        @keyframes particleMovement {
            0% { transform: translate(0, 0); opacity: 1; }
            50% { transform: translate(200px, 200px); opacity: 0.5; }
            100% { transform: translate(0, 0); opacity: 1; }
        }

        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 1.2em;
        }

        footer a {
            color: #ffeb3b;
            text-decoration: none;
        }
    </style>

    <div class="double-exposure"></div>

    <!-- Particle generation -->
    <div class="particles-container">
        <div class="particle" style="top: 10%; left: 15%; animation-delay: 0s;"></div>
        <div class="particle" style="top: 20%; left: 30%; animation-delay: 1s;"></div>
        <div class="particle" style="top: 30%; left: 45%; animation-delay: 2s;"></div>
        <div class="particle" style="top: 40%; left: 60%; animation-delay: 3s;"></div>
        <div class="particle" style="top: 50%; left: 70%; animation-delay: 4s;"></div>
    </div>

    <footer>
        <p>Made with 💕 in India | <a href="#">Visit us</a></p>
    </footer>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
