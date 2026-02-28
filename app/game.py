from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Emoji choices
rock = "🪨"
paper = "📃"
scissors = "✂️"
game_images = [rock, paper, scissors]

# HTML Template with CSS (embedded in Python file)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rock Paper Scissors</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #1d2671, #c33764);
            color: white;
            margin: 0;
            padding: 0;
        }
        h1 {
            margin-top: 30px;
            font-size: 2.5em;
        }
        .container {
            margin-top: 40px;
        }
        .choice-btn {
            background: #fff;
            border: none;
            font-size: 2em;
            padding: 15px;
            margin: 10px;
            border-radius: 15px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .choice-btn:hover {
            transform: scale(1.2);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        .result {
            margin-top: 30px;
            font-size: 1.5em;
            font-weight: bold;
        }
        .winner {
            font-size: 2em;
            margin-top: 20px;
        }
        .user { color: #00ff88; }
        .computer { color: #ff4d4d; }
        .draw { color: #ffd700; }
    </style>
</head>
<body>
    <h1>🎮 Rock Paper Scissors 🎮</h1>
    <form method="POST">
        <button class="choice-btn" name="choice" value="0">🪨</button>
        <button class="choice-btn" name="choice" value="1">📃</button>
        <button class="choice-btn" name="choice" value="2">✂️</button>
    </form>

    {% if user_symbol %}
    <div class="container">
        <p>You chose: {{ user_symbol }}</p>
        <p>Computer chose: {{ computer_symbol }}</p>
        <p class="result">{{ result_message }}</p>
        <p class="winner {{ winner }}">
            {% if winner == "user" %} 🏆 You Win! 🏆 {% endif %}
            {% if winner == "computer" %} 💻 Computer Wins! 💻 {% endif %}
            {% if winner == "draw" %} 🤝 It's a Draw! 🤝 {% endif %}
        </p>
    </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def rps_game():
    user_symbol = ""
    computer_symbol = ""
    result_message = ""
    winner = ""

    if request.method == "POST":
        user_choice = int(request.form["choice"])
        computer_choice = random.randint(0, 2)

        user_symbol = game_images[user_choice]
        computer_symbol = game_images[computer_choice]

        # Determine winner
        if user_choice == computer_choice:
            result_message = "It's a Draw! 😐"
            winner = "draw"
        elif user_choice == 0 and computer_choice == 2:
            result_message = "Hurray, You Win! 🥳"
            winner = "user"
        elif user_choice == 2 and computer_choice == 0:
            result_message = "You Lose! 👎"
            winner = "computer"
        elif user_choice > computer_choice:
            result_message = "Hurray, You Win! 🥳"
            winner = "user"
        else:
            result_message = "You Lose! 👎"
            winner = "computer"

    return render_template_string(
        html_template,
        user_symbol=user_symbol,
        computer_symbol=computer_symbol,
        result_message=result_message,
        winner=winner
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)