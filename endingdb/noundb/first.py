def apply_changes(database):
    database["noun"]["11"] = {
        "singular": {
            "nominative": (0, "a"),
            "vocative": (0, "a"),
            "genitive": (1, "ae"),
            "dative": (1, "ae"),
            "accusative": (1, "am"),
            "ablative": (1, "a")
        },
        "plural": {
            "nominative": (1, "ae"),
            "vocative": (1, "ae"),
            "genitive": (1, "is"),
            "dative": (1, "ae"),
            "accusative": (1, "as"),
            "ablative": (1, "is")
        }
    }
    return database
