import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Typography Art</title>
        <style>
            body {
                background: linear-gradient(to bottom, #282c34, #61dafb);
                color: #ffffff;
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }

            .container {
                text-align: center;
                padding: 20px;
                max-width: 80%;
            }

            h1 {
                font-size: 4rem;
                font-weight: 900;
                margin: 0;
                line-height: 1.2;
                animation: fadeIn 2s ease-in-out;
            }

            h2 {
                font-size: 2rem;
                font-weight: 700;
                margin: 20px 0;
                color: #ffd700;
                animation: slideIn 2s ease-in-out;
            }

            p {
                font-size: 1.5rem;
                font-weight: 400;
                color: #c0c0c0;
                margin: 15px 0;
                animation: fadeInUp 2s ease-in-out;
            }

            /* Particle effect */
            .particles-container {
                position: absolute;
                width: 100%;
                height: 100%;
                overflow: hidden;
                top: 0;
                left: 0;
            }

            .particle {
                position: absolute;
                width: 6px;
                height: 6px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 50%;
                animation: float 5s infinite ease-in-out;
            }

            /* Animations */
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            @keyframes slideIn {
                from { transform: translateY(-30px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }

            @keyframes fadeInUp {
                from { transform: translateY(30px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }

            @keyframes float {
                0% { transform: translateY(0) translateX(0); opacity: 1; }
                50% { transform: translateY(-50px) translateX(30px); opacity: 0.5; }
                100% { transform: translateY(0) translateX(0); opacity: 1; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Typography Art</h1>
            <h2>Discover the beauty of words</h2>
            <p>Crafting visuals with the art of typefaces.</p>
            <p>Typography is not just about words; it's about how they speak.</p>
        </div>

        <!-- Particle background -->
        <div class="particles-container">
            <!-- Generating particles -->
            <div class="particle" style="top: 10%; left: 20%; animation-delay: 0s;"></div>
            <div class="particle" style="top: 30%; left: 40%; animation-delay: 1s;"></div>
            <div class="particle" style="top: 50%; left: 60%; animation-delay: 2s;"></div>
            <div class="particle" style="top: 70%; left: 80%; animation-delay: 3s;"></div>
            <div class="particle" style="top: 90%; left: 50%; animation-delay: 4s;"></div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
