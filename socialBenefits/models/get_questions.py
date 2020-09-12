import json
from database.benefits import json_pensioner
from database.criteria import json_criteria


class Quiz:
    def __init__(self, criterias, benefit):
        r_input = criterias["Критерии"]
        r = sorted(r_input.items(), key=lambda item: item[1]["вес"])
        self.criterias = r

        self.choosed_options = []
        self.benefit = benefit

    def getNextQuestion(self):
        if self.choosed_options == []:
            return self.criterias[0]


table_benefits = json.loads(json_pensioner)
table_criteria = json.loads(json_criteria)

q = Quiz(table_criteria, table_benefits["Пенсионер"])
print(q.getNextQuestion())
