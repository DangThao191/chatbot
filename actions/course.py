import json

def get_course(define, attribute):
    try:
        with open("data/course.json", "r") as f:
            langues = json.loads(f.read())
            for langue in langues:
                if langue["define"] == str.lower(define):
                    return langues[str.lower(attribute)]
    except Exception as e:
        print(str(e))



   

