def apply_changes(database):
    database["noun"]["21"] = {
        "singular": {
            "nominative": (0, "us"),
            "vocative": (1, "e"),
            "genitive": (1, "i"),
            "dative": (1, "o"),
            "accusative": (1, "um"),
            "ablative": (1, "o")
        },
        "plural": {
            "nominative": (1, "i"),
            "vocative": (1, "i"),
            "genitive": (1, "orum"),
            "dative": (1, "is"),
            "accusative": (1, "os"),
            "ablative": (1, "is")
        }
    }
    database["noun"]["22"] = {
        "singular": {
            "nominative": (1, "um"),
            "vocative": (1, "e"),
            "genitive": (1, "i"),
            "dative": (1, "o"),
            "accusative": (1, "um"),
            "ablative": (1, "o")
        },
        "plural": {
            "nominative": (1, "a"),
            "vocative": (1, "i"),
            "genitive": (1, "orum"),
            "dative": (1, "is"),
            "accusative": (1, "a"),
            "ablative": (1, "is")
        }
    }
    return database
