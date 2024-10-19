from flask import Flask, render_template
import os
import time
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/htop')
def htop():
    username = 'Darshan'
    
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5*3600))
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    return f"""
    <html>
        <head><title>Server Stats</title></head>
        <body>
            <h1>Server Stats</h1>
            <p><strong>Name:</strong>Darshan Shetty</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <h2>Top Output</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
