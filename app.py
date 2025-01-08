import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
    <div class="container">
        <div class="text-container">
            <h1><span class="highlight">All</span><br>Set<br>✅<span class="dot">.</span></h1>
            <p class="hashtag">made with love <span class="trend">💌</span> in india</p>
        </div>
    </div>
    </center>
    <style>
        body {
            background-color: #000;
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            font-family: 'Arial', sans-serif;
        }

        .container {
            position: relative;
            text-align: left;
        }

        .text-container {
            position: relative;
            z-index: 10;
        }

        h1 {
            font-size: 8vw;
            line-height: 1;
            font-weight: bold;
            color: white;
            margin: 0;
            text-transform: uppercase;
        }

        .highlight {
            color: #00bfff;
            position: relative;
            z-index: 1;
        }

        .dot {
            color: #00bfff;
        }

        .hashtag {
            font-size: 2vw;
            margin-top: 20px;
            font-weight: bold;
            color: white;
        }

        .trend {
            color: #00bfff;
        }

        /* Bubbles Background */
        .bubbles {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            top: 0;
            left: 0;
            z-index: 0;
        }

        .bubble {
            position: absolute;
            bottom: -100px;
            width: 20px;
            height: 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            animation: float 10s infinite ease-in-out;
        }

        .bubble:nth-child(1) {
            left: 10%;
            width: 40px;
            height: 40px;
            animation-duration: 12s;
            animation-delay: 0s;
        }

        .bubble:nth-child(2) {
            left: 30%;
            width: 25px;
            height: 25px;
            animation-duration: 8s;
            animation-delay: 2s;
        }

        .bubble:nth-child(3) {
            left: 50%;
            width: 30px;
            height: 30px;
            animation-duration: 10s;
            animation-delay: 4s;
        }

        .bubble:nth-child(4) {
            left: 70%;
            width: 20px;
            height: 20px;
            animation-duration: 14s;
            animation-delay: 6s;
        }

        .bubble:nth-child(5) {
            left: 90%;
            width: 35px;
            height: 35px;
            animation-duration: 16s;
            animation-delay: 8s;
        }

        @keyframes float {
            0% {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
            50% {
                transform: translateY(-50vh) scale(1.2);
                opacity: 0.7;
            }
            100% {
                transform: translateY(-100vh) scale(1.5);
                opacity: 0;
            }
        }
    </style>

    <div class="bubbles">
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
    </div>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

