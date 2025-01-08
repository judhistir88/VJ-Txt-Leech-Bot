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

        .circle {
            position: absolute;
            width: 50%;
            height: 50%;
            background: #00bfff;
            border-radius: 50%;
            top: 10%;
            left: -10%;
            z-index: 0;
        }
    </style>

    <div class="circle"></div>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
