from flask import Flask, redirect, url_for, render_template, request
import os
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

# OAuth2 config
CLIENT_ID = 'BOT_CLIENT_ID'
CLIENT_SECRET = 'BOT_CLIENT_SECRET'
REDIRECT_URI = 'https://yoursite.com/callback'
API_BASE_URL = 'https://discord.com/api'

WHITELIST = {'ID1', 'ID2' } # И т.д

def get_token(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(f'{API_BASE_URL}/oauth2/token', data=data, headers=headers)
    return r.json()

def get_user_info(token):
    headers = {'Authorization': f"Bearer {token}"}
    r = requests.get(f"{API_BASE_URL}/users/@me", headers=headers)
    return r.json()

@app.route('/')
def index():
    user = session.get('user')
    allowed = False
    if user and user.get('id') in WHITELIST:
        allowed = True
    return render_template('index.html', user=user, allowed=allowed)

@app.route('/login')
def login():
    return redirect(
        f"{API_BASE_URL}/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify"
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_data = get_token(code)
    access_token = token_data.get('access_token')
    user_info = get_user_info(access_token)
    session['user'] = user_info
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))
import random
from flask import jsonify, session

ITEMS = [
    "Karpaty Lviv",
    "Ajax",
    "Shakhtar Donetsk",
    "Mazan",
    "Fc Freiburg",
    "Trifecta",
    "Dynamo Kyiv",
    "Cleveland Cavaliers",
    "Melbourne",
    "Ac. Losc Lille",
    "Chelsea",
    "Wolverhampton", #1
    "Scarlet Devils",
    "Bayern Munchen",
    "Juventus",
    "Dnipro"
]


@app.route('/spin')
def spin():
    user = session.get('user')
    if not user or user.get('id') not in WHITELIST:
        return jsonify({'error': 'unauthorized'}), 403

    history = session.get('history', [])

    available_items = [item for item in ITEMS if item not in history]

    if not available_items:
        session['history'] = []
        return jsonify({'error': 'Команды закончились.'}), 200

    item = random.choice(available_items)

    history.append(item)
    session['history'] = history

    return jsonify({'item': item})


if __name__ == '__main__':
    app.run(debug=True)
