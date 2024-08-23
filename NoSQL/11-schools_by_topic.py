def schools_by_topic(mongo_collection, topic):
    """Returns the list of school documents that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
