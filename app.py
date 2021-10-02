import json
import time as t

import flask
import numpy as np

app = flask.Flask(__name__, static_folder="public")


@app.route("/")
def app_route():
    return app.send_static_file("index.html")


@app.route("/api/data")
def app_sequence():
    t.sleep(0.5)
    return json.dumps(
        {
            "x": np.random.random(100).tolist(),
            "y": np.random.random(100).tolist(),
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)