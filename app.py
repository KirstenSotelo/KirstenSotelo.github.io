from flask import Flask, render_template, send_from_directory # send_from_directory is for filepathing issues
import os

# NOTE: Flask defaults to having a certain filepaths explained below:
# Index.html should be in a 'templates' folder
# styles.css should be in a 'static' folder
# I override this by specifying template folder and routing the styles css manually for the sake of this lab10c problem

# template folder to the current directory
app = Flask(__name__, template_folder=os.path.dirname(__file__))

@app.route("/")
def index():
    return render_template("index.html")

# The routing below is for if the file 
@app.route("/styles.css")
def serve_styles():
    return send_from_directory(".", "styles.css")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
