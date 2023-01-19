from flask import (Response, Flask, flash, redirect, render_template, request,
                   send_from_directory, session, url_for)


app = Flask(__name__)
app.config["SECRET_KEY"] = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'



# That is home page like scrapping tool and scrape the data into given website urls
@app.route("/", methods=["GET","POST"])
def home():
    """
    That route can show landing page while user can login
    """
    try:
        if request.method == "POST":
            return render_template("index.html")
        else:
            return render_template("index.html")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # db.create_all()
    app.run(
        host="127.0.0.1",
        port=8080,
        debug=True)

