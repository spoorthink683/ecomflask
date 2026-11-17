from flask import Flask
SHIPPING_ANNOUNCEMENT="Arriving soon"
@app.route("/")
def home():
    return "Welcome"
