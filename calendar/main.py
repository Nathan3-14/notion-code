from src import better_json as bjson

data = bjson.load("data.json")
data_exams = data.get("exams")
data_people = data.get("people")