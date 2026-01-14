from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>For My Darling Nimisha 💕</title>
        <style>
            body {
                background: linear-gradient(to right, #ffe6f0, #fff0f5);
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 50px;
                color: #d63384;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 0.2em;
                animation: pulse 2s infinite;
            }
            p {
                font-size: 1.5em;
                margin: 0.5em 0;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            .emoji {
                font-size: 2em;
                margin-top: 1em;
            }
        </style>
    </head>
    <body>
        <h1>💖 Love You Darling 💖</h1>
        <p>🌹 You are the sunshine in my life 🌹</p>
        <p>💌 This little app is just for you 💌</p>
        <div class="emoji">🥰😘💞</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)