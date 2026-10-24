import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_posts():
    """Hilfsfunktion zum Laden der Posts aus der JSON-Datei."""
    with open("blogposts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Hilfsfunktion zum Speichern der Posts in der JSON-Datei."""
    with open("blogposts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Formulardaten auslesen
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        posts = load_posts()

        # Eindeutige ID vergeben
        new_id = max([p['id'] for p in posts], default=0) + 1

        # Neuen Beitrag an die Liste anhängen
        posts.append({
            "id": new_id,
            "author": author,
            "title": title,
            "content": content
        })

        # Aktualisierte Liste in JSON-Datei speichern
        save_posts(posts)

        # Nach dem Speichern zurück zur Startseite weiterleiten
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    posts = load_posts()

    # Klassische Schleife statt List Comprehension
    updated_posts = []
    for post in posts:
        if post['id'] != post_id:
            updated_posts.append(post)

    save_posts(updated_posts)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)