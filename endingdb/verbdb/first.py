
def apply_changes(database):
    database["verb"]["11"] = {} 
    database["verb"]["11"]["active"] = {} 
    database["verb"]["11"]["passive"] = {} 
    database["verb"]["11"]["active"]["infinitive"] = {
        "present": {
            "*": {
                "*": (1, "are")
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
    database["verb"]["11"]["passive"]["infinitive"] = {
        "present": {
            "*": {
                "*": (1, "ari")
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
    database["verb"]["11"]["active"]["imperative"] = {
        "*": {
            "singular": {
                "*": (1, "a")
            }
        },
        "*": {
            "plural": {
                "*": (1, "ate")
            }
        }
    }
    database["verb"]["11"]["passive"]["imperative"] = {
        "*": {
            "singular": {
                "*": (1, "are")
            }
        },
        "*": {
            "plural": {
                "*": (1, "amini")
            }
        }
    }
    database["verb"]["11"]["active"]["indicative"] = {
        "present": {
            "singular": {
                "1": (1, "o"),
                "2": (1, "as"),
                "3": (1, "at")
            },
            "plural": {
                "1": (1, "amus"),
                "2": (1, "atis"),
                "3": (1, "ant")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "abam"),
                "2": (1, "abas"),
                "3": (1, "abat")
            },
            "plural": {
                "1": (1, "abamus"),
                "2": (1, "abatis"),
                "3": (1, "abant")
            }
        },
        "future": {
            "singular": {
                "1": (1, "abo"),
                "2": (1, "abis"),
                "3": (1, "abit")
            },
            "plural": {
                "1": (1, "abimus"),
                "2": (1, "abitis"),
                "3": (1, "abunt")
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
    database["verb"]["11"]["passive"]["indicative"] = {
        "present": {
            "singular": {
                "1": (1, "or"),
                "2": (1, "aris"),
                "3": (1, "atur")
            },
            "plural": {
                "1": (1, "amur"),
                "2": (1, "amini"),
                "3": (1, "antur")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "abar"),
                "2": (1, "abaris"),
                "3": (1, "abatur")
            },
            "plural": {
                "1": (1, "abamur"),
                "2": (1, "abamini"),
                "3": (1, "abantur")
            }
        },
        "future": {
            "singular": {
                "1": (1, "abor"),
                "2": (1, "aberis"),
                "3": (1, "abitur")
            },
            "plural": {
                "1": (1, "abimur"),
                "2": (1, "abimini"),
                "3": (1, "abuntur")
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
    database["verb"]["11"]["active"]["subjunctive"] = {
        "present": {
            "singular": {
                "1": (1, "em"),
                "2": (1, "es"),
                "3": (1, "et")
            },
            "plural": {
                "1": (1, "emus"),
                "2": (1, "etis"),
                "3": (1, "ent")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "arem"),
                "2": (1, "ares"),
                "3": (1, "aret")
            },
            "plural": {
                "1": (1, "aremus"),
                "2": (1, "aretis"),
                "3": (1, "arent")
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
    database["verb"]["11"]["passive"]["subjunctive"] = {
        "present": {
            "singular": {
                "1": (1, "er"),
                "2": (1, "eris"),
                "3": (1, "etur")
            },
            "plural": {
                "1": (1, "emur"),
                "2": (1, "emini"),
                "3": (1, "entur")
            }
        },
        "imperfect": {
            "singular": {
                "1": (1, "arer"),
                "2": (1, "areris"),
                "3": (1, "aretur")
            },
            "plural": {
                "1": (1, "aremur"),
                "2": (1, "aremini"),
                "3": (1, "arentur")
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
