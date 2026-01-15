from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>For My Darling 💕</title>
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
            img {
                margin-top: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                max-width: 80%;
                height: auto;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <h1>💖 Love You Darling Nimisha 💖</h1>
        <p>🌹 You are the sunshine in my life 🌹</p>
        <p>💌 This little app is just for you 💌</p>
        <img src="/static/nimisha.jpg" alt="Our Special Photo">
        <div class="emoji">🥰 😘 💞</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)