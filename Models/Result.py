class Result:
    def __init__(self, id, text, status):
        self.id = id
        self.text = text
        self.status = status

    def to_json(self):
        return {
            "id": self.id,
            "text": self.text,
            "status": self.status
        }

class ResultList:
    def __init__(self):
        self.result = []

    def add_result(self, id, text, status):
        self.result.append(Result(id, text, status))

    def to_json(self):
        return {
            "result": [result.to_json() for result in self.result]
        }