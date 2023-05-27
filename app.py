from flask import Flask , render_template ,jsonify

app = Flask(__name__)

CHARACTER=[
    {
        'name' : 'Ross Geller',
        'dia' : 'We were on a break!',
        'pair': 'Ross-Rachel',
        'be' : "The One With Unagi (Season 6, Episode 17)"
    },
    {
        'name' : 'Chandler',
        'dia' : "Hi, I'm Chandler. I make jokes when I'm uncomfortable.",
        'pair': 'Mondler',
        'be' : "The One With the Blackout"
    },
    {
        'name' : 'Joey',
        'dia' : "Joey doesn't share food!",
        'pair': 'Single',
        'be' : "The One With Joey's Award (Season 7, Episode 18)"
    },
    {
        'name' : 'Rachel',
        'dia' : "You Fell Asleep?",
        'pair': 'Ross-Rachel',
        'be' : "The One Where Rachel Finds Out (Season 1, Episode 24)"
    },
    {
        'name' : 'Monica',
        'dia' : "Your little Harmonica is hammered.",
        'pair': 'Mondler',
        'be' : "THE ONE WITH ALL THE THANKSGIVINGS (SEASON 5, EPISODE 8)"
    },
    {
        'name' : 'Pheobe',
        'dia' : "My eyes! My eyes!.",
        'pair': 'Mike-Pheobe',
        'be' : "The One Where Everyone Finds Out (Season 5, Episode 14)"
    },
    
]

@app.route("/")
def greeting():
    return render_template("home.html",character=CHARACTER)

@app.route("/api/characters")
def list_character():
    return jsonify(CHARACTER)


if __name__ == '__main__':
    app.run(debug=True)