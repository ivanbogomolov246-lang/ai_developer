import json
developer = {
    "name": "Иван",
    "age": 20,
    "goal": "AI Developer",
    "skills": ["Python", "Git", "JSON"]
}
developer_json = json.dumps(developer, ensure_ascii=False, indent=4)
print(developer_json)
print(type(developer_json))
not_json = json.loads(developer_json)
print(not_json)
print(type(not_json))
with open("developer.json", "w", encoding="utf-8") as file:
    json.dump(developer, file, ensure_ascii=False, indent=4)
with open("developer.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data["name"])
    print(", ".join(data["skills"]))
