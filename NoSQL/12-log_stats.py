#!/usr/bin/env python3
"""


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documnets({"method"}: method})
        print("\tmethod {}: {}.format(method, count)")

    status = collection.count_documnets({
        "method": "GET",
        "path": "/status"
    })

    print(" {} status check".format(status))
