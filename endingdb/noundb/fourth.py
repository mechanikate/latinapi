def apply_changes(database):
    database["noun"]["41"] = {
        "singular": {
            "nominative": (0, "us"),
            "vocative": (0, "us"),
            "genitive": (1, "us"),
            "dative": (1, "ui"),
            "accusative": (1, "um"),
            "ablative": (1, "u")
        },
        "plural": {
            "nominative": (1, "us"),
            "vocative": (1, "us"),
            "genitive": (1, "uum"),
            "dative": (1, "ibus"),
            "accusative": (1, "us"),
            "ablative": (1, "ibus")
        }
    }
    database["noun"]["42"] = {
        "singular": {
            "nominative": (1, "u"),
            "vocative": (1, "u"),
            "genitive": (1, "us"),
            "dative": (1, "u"),
            "accusative": (1, "u"),
            "ablative": (1, "u")
        },
        "plural": {
            "nominative": (1, "ua"),
            "vocative": (1, "ua"),
            "genitive": (1, "uum"),
            "dative": (1, "ibus"),
            "accusative": (1, "ua"),
            "ablative": (1, "ibus")
        }
    }
    return database
