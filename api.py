import sys

from search import *
from flask import Flask, jsonify, request
from conjugate import retrieve_verb, retrieve_noun

app = Flask(__name__)
@app.route("/v1/", methods=["GET"])
def main_info():
    return jsonify({
        "message": "Welcome to latinAPI; more info at https://github.com/mechanikate/latinapi."
    })
@app.route("/v1/searchSimilar/", methods=["GET"])
@app.route("/v1/getWord/", methods=["GET"])
@app.route("/v1/getSimilar/", methods=["GET"])
@app.route("/v1/stem/any/", methods=["GET"])
@app.route("/v1/stem/conjugate/", methods=["GET"])
@app.route("/v1/stem/decline/", methods=["GET"])
@app.route("/v1/stem/<form>/", methods=["GET"])
def _error_missing_param_word(form=""):
    return jsonify({
        "error": 1,
        "message": "Missing parameter(s): word"
    })
@app.route("/v1/stem/", methods=["GET"])
def _error_missing_param_form_word():
    return jsonify({
        "error": 1,
        "message": "Missing parameter(s): stem, word"
    })
@app.route("/v1/searchSimilar/<word>", methods=["GET"])
def search_similar_word(word):
    return jsonify(search_dictionary(word, db_name="lewis"))

@app.route("/v1/getWord/<word>", methods=["GET"])
def get_exact_word(word):
    if word not in dbs["lewis"]:
        return jsonify({"error": 404, "message": "No word found."})
    return jsonify(dbs["lewis"][word])

@app.route("/v1/getSimilar/<word>", methods=["GET"])
def get_similar_word(word):
    return jsonify(dbs["lewis"][search_dictionary(word, db_name="lewis")[0]])

@app.route("/v1/stem/any/<word>", methods=["GET"])
def get_stem(word):
    closest_word=search_dictionary(word, db_name="whitaker")[0]
    closest_entry=dbs["whitaker"][closest_word]
    return_dict = {}
    
    return_dict["stems"]=closest_entry["stems"]
    if "pos" in closest_entry:
        return_dict["partOfSpeech"]=closest_entry["pos"]
    if "gender" in closest_entry:
        return_dict["gender"]=closest_entry["gender"]
    return_dict["form"]=[closest_entry["conjugation"] if "conjugation" in closest_entry else closest_entry["declension"], closest_entry["conjugation_variant"] if "conjugation_variant" in closest_entry else closest_entry["declension_variant"]]
    return jsonify(return_dict)

@app.route("/v1/stem/<form>/<word>", methods=["GET"])
def get_stem_form(form, word):
    return _get_stem_form(form, word)
def _get_stem_form(form, word):
    closest_word=search_dictionary_pos(word, db_name="whitaker", pos=form)[0]
    closest_entry=dbs["whitaker"][closest_word]
    return_dict = {}
    
    return_dict["stems"]=closest_entry["stems"]
    if "pos" in closest_entry:
        return_dict["partOfSpeech"]=closest_entry["pos"]
    if "gender" in closest_entry:
        return_dict["gender"]=closest_entry["gender"]
    return_dict["form"]=[closest_entry["conjugation"] if "conjugation" in closest_entry else closest_entry["declension"], closest_entry["conjugation_variant"] if "conjugation_variant" in closest_entry else closest_entry["declension_variant"]]
    return return_dict

@app.route("/v1/conjugate/<word>", methods=["GET"])
def get_conjugated(word):
    stem_form = get_stem_form("V", word)
    try: 
        conjugated, warning = retrieve_verb(stem_form["stems"], stem_form["form"][0], stem_form["form"][1], request.args.get("voice"), request.args.get("mood"), request.args.get("case") or "*", request.args.get("number") or "*", request.args.get("person") or "*")
        return jsonify({
            "result": conjugated,
            "warning": warning
        })
    except:
        return jsonify({
            "error": 1,
            "message": "Missing verb parameter(s). All parameters: voice, mood, case, number, person."
        })
@app.route("/v1/decline/<word>", methods=["GET"])
def get_declined(word):
    stem_form = get_stem_form("N", word)
    declined, warning = retrieve_noun(stem_form["stems"], stem_form["form"][0], stem_form["form"][1], request.args.get("number"), request.args.get("case"))
    try:
        return jsonify({
            "result": declined,
            "warning": warning
        })
    except:
        return jsonify({
            "error": 1,
            "message": "Missing noun parameter(s). All parameters: number, case."
        })

@app.errorhandler(Exception)
def generic_error(e):
    print(e, file=sys.stderr)
    return jsonify({
        "error": e.code if hasattr(e, "code") else 0, 
        "message": f"Miscellaneous error: {e.name}"
    })
if __name__ == "__main__":
    app.run()
