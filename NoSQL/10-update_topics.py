#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""
def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
