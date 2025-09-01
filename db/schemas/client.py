def client_schema(client) -> dict:
    return {
        "clientID": str(client["_id"]),
        "username": client["username"],
        "name": client["name"],
        "email": client["email"],
        "disabled": client["disabled"]
    }

def clientDB_schema(clientDB) -> dict:
    return {
        "clientID": str(clientDB["_id"]),
        "username": clientDB["username"],
        "name": clientDB["name"],
        "email": clientDB["email"],
        "disabled": clientDB["disabled"],
        "password": clientDB["password"]
    }