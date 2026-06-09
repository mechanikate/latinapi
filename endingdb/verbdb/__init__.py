from endingdb.verbdb import first, second, third, third_istem, fourth
def apply_changes(database):
    database["verb"] = {}
    database = first.apply_changes(database)
    database = second.apply_changes(database)
    database = third.apply_changes(database)
    database = third_istem.apply_changes(database)
    database = fourth.apply_changes(database)
    return database
