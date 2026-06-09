import endingdb.verbdb, endingdb.noundb
database = {}
database = verbdb.apply_changes(database)
database = noundb.apply_changes(database)
