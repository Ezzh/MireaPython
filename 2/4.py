bd = {}

def append_worker(bd: dict, name: str, age: int, state: str, number_workspace: int, secret: bool):
    bd.update([(name, {"age": age, "state": state, "number_workspace": number_workspace, "secret": secret})])
    return

append_worker(bd, "Nikita", 19, "IT", 23, True)
print(bd)