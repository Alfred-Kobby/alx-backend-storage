#!/usr/bin/env python3
""" PyMongo """


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school
    document based on name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
