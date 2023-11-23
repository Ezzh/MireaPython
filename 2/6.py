def write_in_file(file_name: str, line: str):
    with open(file=file_name, mode="a") as f:
        f.write(line+"\n")
    return

write_in_file("bebebe", "bebebe")

