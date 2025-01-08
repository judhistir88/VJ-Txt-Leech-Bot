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
        <title>ASCII Art</title>
        <style>
            body {
                background: antiquewhite;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                height: 100vh;
                font-family: monospace;
            }
            #ascii {
                white-space: pre; /* Preserve spacing for ASCII art */
                text-align: center; /* Center align the ASCII art */
                margin: 0;
            }
            footer {
                text-align: center;
                padding: 10px;
                background: antiquewhite;
                font-size: 1.2em;
                width: 100%;
                position: fixed;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <div id="ascii">
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
