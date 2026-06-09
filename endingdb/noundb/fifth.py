def apply_changes(database):
    database["noun"]["51"] = {
        "singular": {
            "nominative": (0, "es"),
            "vocative": (0, "es"),
            "genitive": (1, "ei"),
            "dative": (1, "ei"),
            "accusative": (1, "em"),
            "ablative": (1, "e")
        },
        "plural": {
            "nominative": (1, "es"),
            "vocative": (1, "es"),
            "genitive": (1, "erum"),
            "dative": (1, "ebus"),
            "accusative": (1, "es"),
            "ablative": (1, "ebus")
        }
    }
    return database
