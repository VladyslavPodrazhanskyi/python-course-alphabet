from flask import Flask, render_template, request

app = Flask(__name__)


vegetables_list = ['carrot', 'potato', 'cucumber', 'tomatto', 'beet', 'cabbage']

fruites_list = ['apple', 'pair', 'plum', 'apricot', 'gooseberry', 'raspberry', 'cherry']



def do_get(template, data_list):
    return render_template(template, data_list=data_list)

def do_post(value, data_list):
    data_list.append(value)
    return "Successfully added new vegetable."

def do_delete(value, data_list):
    if value in data_list:
        data_list.remove(value)
        return "Successfully deleted the item"
    else:
        return "The item is not available in the list"


@app.route("/")
def get_main():
    return render_template("main.html")


@app.route("/vegetables")
@app.route("/vegetables/<string:value>", methods=["GET", "POST", "DELETE"])
def vegetables_methods(value=None):
    if request.method == "POST":
        return do_post(value, vegetables_list)

    elif request.method == "DELETE":
        return do_delete(value, vegetables_list)

    else:
        return do_get("vegetables.html", vegetables_list)




@app.route("/fruites")
@app.route("/fruites/<string:value>", methods=["GET", "POST", "DELETE"])
def fruites_methods(value=None):
    if request.method == "POST":
        return do_post(value, fruites_list)
    elif request.method == "DELETE":
        return do_delete(value, fruites_list)
    else:
        return do_get("fruites.html", fruites_list)




if __name__ == "__main__":
    app.run()