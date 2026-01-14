from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>For My Darling Nimisha💕</title>
            <style>
                body {
                    background-color: #fff0f5;
                    font-family: 'Segoe UI', sans-serif;
                    text-align: center;
                    padding-top: 100px;
                    color: #ff1493;
                }
                h1 {
                    font-size: 48px;
                    animation: pulse 2s infinite;
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
            </style>
        </head>
        <body>
            <h1>💖 Love you darling 💖</h1>
            <p>🌹 You light up my world 🌹</p>
            <p>💌 This little app is just for you 💌</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)