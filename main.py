from utilus import load_candidates, get_by_pk, get_url, get_by_skill

from flask import Flask

filename = "candidates.json"

data = load_candidates(filename)

app = Flask(__name__)


@app.route("/")
def page_main():
    """Главня страница"""
    result = '<pre>'

    for condidate in data:
        result += f"""
        {condidate["name"]}\n
        {condidate["position"]}\n
        {condidate["skills"]}\n
        """
    result += '<pre>'
    return result


@app.route("/condidate/<int:pk>")
def page_codidate(pk):
    """Страница с кондидатом"""
    con = get_url(pk, data)
    result = f"<img src='{con}'>" + '<pre>' + get_by_pk(pk, data) + '<pre>'
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    skill_lower = skill.lower()
    """Страница кондидатов по навыкам"""
    result = '<pre>' + get_by_skill(skill_lower, data) + '<pre>'
    return result


app.run()
