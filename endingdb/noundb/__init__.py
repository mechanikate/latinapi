from endingdb.noundb import first, second, third, fourth, fifth
def apply_changes(database):
    database["noun"] = {}
    database = first.apply_changes(database)
    database = second.apply_changes(database)
    database = third.apply_changes(database)
    database = fourth.apply_changes(database)
    database = fifth.apply_changes(database)
    return database
