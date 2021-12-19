from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """Function with guess the number game."""
    if request.method == "GET":
        return render_template("game_start.html")
    else:
        minimum = int(request.form.get("min"))
        maximum = int(request.form.get("max"))
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))
        if answer == "za dużo":
            maximum = guess
        elif answer == "za mało":
            minimum = guess
        elif answer == "wygrałeś":
            return render_template("game_win.html")

        guess = (maximum - minimum) // 2 + minimum

        return render_template("game.html", guess=guess, maximum=maximum, minimum=minimum)


if __name__ == "__main__":
    app.run(debug=True)
