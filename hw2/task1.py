def generate_table(data):
    table = "\\begin{tabular}{" + "c" * len(data[0]) + "}\n"
    for row in data:
        table += " & ".join(row) + " \\\\\n"
    table += "\\end{tabular}"
    return table


if __name__ == "__main__":
    data = [["A", "B", "C"],
            ["1", "2", "3"],
            ["4", "5", "6"]]

    filename = "artifacts/table.tex"
    with open(filename, "w") as file:
        file.write(generate_table(data))
