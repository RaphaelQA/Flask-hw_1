import json


def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def get_all(data):
    condidate = []

    for item in data:
        condidate.append(item["name"])
    return condidate


def get_by_pk(pk, data):
    for user in data:
        for key, value in user.items():
            if value == pk:
                return f"""
                {user['name']}\n
                {user['position']}\n
                {user['skills']}\n
                """


def get_url(pk, data):
    for user in data:
        for key, value in user.items():
            if value == pk:
                url = user["picture"]
                return url


def get_by_skill(skill: str, data):
    name = []
    result = " "
    for user in data:
        if skill in user["skills"].lower().split(", "):
            name.append(user)
    for n in name:
        result += f"""
        {n['name']}\n
        {n['position']}\n
        {n['skills']}\n
        """
    return result
