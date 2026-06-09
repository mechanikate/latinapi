def apply_changes(database):
    database["noun"]["31"] = {
        "singular": {
            "nominative": (0, ""),
            "vocative": (0, ""),
            "genitive": (1, "is"),
            "dative": (1, "i"),
            "accusative": (1, "em"),
            "ablative": (1, "e")
        },
        "plural": {
            "nominative": (1, "es"),
            "vocative": (1, "es"),
            "genitive": (1, "um"),
            "dative": (1, "ibus"),
            "accusative": (1, "es"),
            "ablative": (1, "ibus")
        }
    }
    database["noun"]["32"] = {
        "singular": {
            "nominative": (0, ""),
            "vocative": (0, ""),
            "genitive": (1, "is"),
            "dative": (1, "i"),
            "accusative": (1, "em"),
            "ablative": (1, "o")
        },
        "plural": {
            "nominative": (1, "es"),
            "vocative": (1, "i"),
            "genitive": (1, "um"),
            "dative": (1, "ibus"),
            "accusative": (1, "es"),
            "ablative": (1, "ibus")
        }
    }
    return database
