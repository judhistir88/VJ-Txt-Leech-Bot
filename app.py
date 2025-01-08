import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background: antiquewhite;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                height: 100vh;
                margin: 0;
                font-family: monospace;
            }
            .ascii-art {
                white-space: pre-wrap;
                font-size: 1em;
                color: black;
            }
            footer {
                position: absolute;
                bottom: 10px;
                width: 100%;
                text-align: center;
                background: antiquewhite;
                font-size: 1.2em;
                padding: 10px;
            }
        </style>
    </head>
    <body>
        <div class="ascii-art">
            ███████████████████████████<br>
            ███████▀▀▀░░░░░░░▀▀▀███████<br>
            ████▀░░░░░░░░░░░░░░░░░▀████<br>
            ███│░░░░░░░░░░░░░░░░░░░│███<br>
            ██▌│░░░░░░░░░░░░░░░░░░░│▐██<br>
            ██░└┐░░░░░░░░░░░░░░░░░┌┘░██<br>
            ██░░└┐░░░░░░░░░░░░░░░┌┘░░██<br>
            ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██<br>
            ██▌░│██████▌░░░▐██████│░▐██<br>
            ███░│▐███▀▀░░▄░░▀▀███▌│░███<br>
            ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██<br>
            ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██<br>
            ████▄─┘██▌░░░░░░░▐██└─▄████<br>
            █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████<br>
            ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████<br>
            █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████<br>
            ███████▄░░░░░░░░░░░▄███████<br>
            ██████████▄▄▄▄▄▄▄██████████<br>
            ███████████████████████████
        </div>
        <footer>
            Made with 💕 In India
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
