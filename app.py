import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_posts():
    """Lädt alle Blogbeiträge aus der lokalen JSON-Datei.

    Returns:
        list: Eine Liste von Dictionaries, die jeweils einen Blogbeitrag darstellen.
    """
    with open("blogposts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Speichert die übergebene Beitragsliste in der JSON-Datei.

    Args:
        posts (list): Die zu speichernde Liste von Blogbeiträgen.
    """
    with open("blogposts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    """Sucht einen einzelnen Blogbeitrag anhand seiner eindeutigen ID.

    Args:
        post_id (int): Die ID des gesuchten Beitrags.

    Returns:
        dict oder None: Das Beitragsobjekt bei Treffer, sonst None.
    """
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/")
def index():
    """Zeigt die Startseite mit allen vorhandenen Blogbeiträgen an."""
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Erstellt einen neuen Blogbeitrag.

    GET: Zeigt das Formular zum Erstellen an.
    POST: Verarbeitet die Formulardaten, vergibt eine neue ID und speichert den Beitrag.
    """
    if request.method == "POST":
        # Formulardaten aus dem POST-Request auslesen
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        posts = load_posts()

        # Eindeutige ID generieren (höchste bestehende ID + 1)
        new_id = max([p["id"] for p in posts], default=0) + 1

        posts.append(
            {"id": new_id, "author": author, "title": title, "content": content}
        )

        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    """Löscht einen spezifischen Blogbeitrag anhand seiner ID.

    Args:
        post_id (int): Die ID des zu löschenden Beitrags.
    """
    posts = load_posts()

    # Alle Beiträge behalten, außer den mit der zu löschenden ID
    updated_posts = []
    for post in posts:
        if post["id"] != post_id:
            updated_posts.append(post)

    save_posts(updated_posts)
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Bearbeitet einen bestehenden Blogbeitrag.

    GET: Zeigt das mit den Beitragsdaten vorausgefüllte Formular an.
    POST: Überschreibt die geänderten Felder und speichert die Datei ab.

    Args:
        post_id (int): Die ID des zu bearbeitenden Beitrags.
    """
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        posts = load_posts()

        # Den passenden Beitrag suchen und Felder aktualisieren
        for p in posts:
            if p["id"] == post_id:
                p["author"] = request.form.get("author")
                p["title"] = request.form.get("title")
                p["content"] = request.form.get("content")
                break

        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("update.html", post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
