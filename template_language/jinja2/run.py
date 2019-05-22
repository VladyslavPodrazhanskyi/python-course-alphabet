from flask import Flask, render_template # rendering html templates

app = Flask(__name__)  # creation of flask application


@app.route("/")                 # декоратор позволяет задать путь в котором будет размещаться шаблон
def template_test():
    """
    This function renders current templates with current variables.
    """
    return render_template('update_template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])





if __name__ == '__main__':
    app.run(debug=True)      # запуск вэб приложения.