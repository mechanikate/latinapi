
def apply_changes(database):
    database["verb"]["31"] = {} 
    database["verb"]["31"]["active"] = {} 
    database["verb"]["31"]["passive"] = {} 
    database["verb"]["31"]["active"]["infinitive"] = {
        "present": {
            "*": {
                "*": (1, "ere")
            }
        },
        "future": {
            "*": {
                "*": (3, "urus esse")
            }
        },
        "perfect": {
            "*": {
                "*": (2, "isse")
            }
        }
    }
    database["verb"]["31"]["passive"]["infinitive"] = {
        "present": {
            "*": {
                "*": (1, "i")
            }
        },
        "future": {
            "*": {
                "*": (3, "tum iri")
            }
        },
        "perfect": {
            "*": {
                "*": (3, "us esse")
            }
        }
    }
    database["verb"]["31"]["active"]["imperative"] = {
        "*": {
            "singular": {
                "*": (1, "e")
            }
        },
        "*": {
            "plural": {
                "*": (1, "ite")
            }
        }
    }
    database["verb"]["31"]["passive"]["imperative"] = {
        "*": {
            "singular": {
                "*": (1, "ere")
            }
        },
        "*": {
            "plural": {
                "*": (1, "imini")
            }
        }
    }
    database["verb"]["31"]["active"]["indicative"] = {
        "present": {
            "singular": {
                "1": (1, "io"),
                "2": (1, "is"),
                "3": (1, "it")
            },
            "plural": {
                "1": (1, "imus"),
                "2": (1, "itis"),
                "3": (1, "iunt")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "iebam"),
                "2": (1, "iebas"),
                "3": (1, "iebat")
            },
            "plural": {
                "1": (1, "iebamus"),
                "2": (1, "iebatis"),
                "3": (1, "iebant")
            }
        },
        "future": {
            "singular": {
                "1": (1, "iam"),
                "2": (1, "ies"),
                "3": (1, "iet")
            },
            "plural": {
                "1": (1, "iemus"),
                "2": (1, "ietis"),
                "3": (1, "ient")
            }
        },
        "perfect": {
            "singular": {
                "1": (2, "i"),
                "2": (2, "isti"),
                "3": (2, "it")
            },
            "plural": {
                "1": (2, "imus"),
                "2": (2, "istis"),
                "3": (2, "erunt")
            }
        },
        "pluperfect": {
            "singular": {
                "1": (2, "eram"),
                "2": (2, "eras"),
                "3": (2, "erat")
            },
            "plural": {
                "1": (2, "eramus"),
                "2": (2, "eratis"),
                "3": (2, "erant")
            }
        },
        "future_perfect": {
            "singular": {
                "1": (2, "ero"),
                "2": (2, "eris"),
                "3": (2, "erit")
            },
            "plural": {
                "1": (2, "erimus"),
                "2": (2, "eristis"),
                "3": (2, "erint")
            }
        }
    } 
    database["verb"]["31"]["passive"]["indicative"] = {
        "present": {
            "singular": {
                "1": (1, "ior"),
                "2": (1, "eris"),
                "3": (1, "itur")
            },
            "plural": {
                "1": (1, "imur"),
                "2": (1, "imini"),
                "3": (1, "untur")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "iebar"),
                "2": (1, "iebaris"),
                "3": (1, "iebatur")
            },
            "plural": {
                "1": (1, "iebamur"),
                "2": (1, "iebamini"),
                "3": (1, "iebantur")
            }
        },
        "future": {
            "singular": {
                "1": (1, "iar"),
                "2": (1, "ieris"),
                "3": (1, "ietur")
            },
            "plural": {
                "1": (1, "iemur"),
                "2": (1, "iemini"),
                "3": (1, "ientur")
            }
        },
        "perfect": {
            "singular": {
                "1": (3, "us sum"),
                "2": (3, "us es"),
                "3": (3, "us est")
            },
            "plural": {
                "1": (3, "i sumus"),
                "2": (3, "i estis"),
                "3": (3, "i sunt")
            }
        },
        "pluperfect": {
            "singular": {
                "1": (3, "us eram"),
                "2": (3, "us eras"),
                "3": (3, "us erat")
            },
            "plural": {
                "1": (3, "i eramus"),
                "2": (3, "i eratis"),
                "3": (3, "i erant")
            }
        },
        "future_perfect": {
            "singular": {
                "1": (3, "us ero"),
                "2": (3, "us eris"),
                "3": (3, "us erit")
            },
            "plural": {
                "1": (3, "i erimus"),
                "2": (3, "i eristis"),
                "3": (3, "i erint")
            }
        }
    } 
    database["verb"]["31"]["active"]["subjunctive"] = {
        "present": {
            "singular": {
                "1": (1, "iam"),
                "2": (1, "ias"),
                "3": (1, "iat")
            },
            "plural": {
                "1": (1, "iamus"),
                "2": (1, "iatis"),
                "3": (1, "iant")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "erem"),
                "2": (1, "eres"),
                "3": (1, "eret")
            },
            "plural": {
                "1": (1, "eremus"),
                "2": (1, "eretis"),
                "3": (1, "erent")
            }
        },
        "perfect": {
            "singular": {
                "1": (2, "erim"),
                "2": (2, "eris"),
                "3": (2, "erit")
            },
            "plural": {
                "1": (2, "erimus"),
                "2": (2, "eritis"),
                "3": (2, "erint")
            }
        },
        "pluperfect": {
            "singular": {
                "1": (2, "issem"),
                "2": (2, "isses"),
                "3": (2, "isset")
            },
            "plural": {
                "1": (2, "issemus"),
                "2": (2, "issetis"),
                "3": (2, "issent")
            }
        }
    } 
    database["verb"]["31"]["passive"]["subjunctive"] = {
        "present": {
            "singular": {
                "1": (1, "iar"),
                "2": (1, "iaris"),
                "3": (1, "iatur")
            },
            "plural": {
                "1": (1, "iamur"),
                "2": (1, "iamini"),
                "3": (1, "iantur")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "erer"),
                "2": (1, "ereris"),
                "3": (1, "eretur")
            },
            "plural": {
                "1": (1, "eremur"),
                "2": (1, "eremini"),
                "3": (1, "erentur")
            }
        },
        "perfect": {
            "singular": {
                "1": (3, "us sim"),
                "2": (3, "us sis"),
                "3": (3, "us sit")
            },
            "plural": {
                "1": (3, "i simus"),
                "2": (3, "i sitis"),
                "3": (3, "i sint")
            }
        },
        "pluperfect": {
            "singular": {
                "1": (3, "us essem"),
                "2": (3, "us esses"),
                "3": (3, "us esset")
            },
            "plural": {
                "1": (3, "i essemus"),
                "2": (3, "i essetis"),
                "3": (3, "i essent")
            }
        }
    }
    return database
