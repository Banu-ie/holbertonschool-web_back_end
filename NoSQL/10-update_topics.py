#!/usr/bin/env python3
"""Change school topics."""

def update_topics(mongo_collection, name, topics):
    """Update topics of all school documents with given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
