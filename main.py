from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    combos = request.form["combos"].splitlines()
    results = []

    for combo in combos:
        if combo.strip() == "":
            continue
        
        if "test" in combo:
            results.append(combo + " : VALID")
        else:
            results.append(combo + " : INVALID")

    return "<br>".join(results)

app.run(host="0.0.0.0", port=3000)
