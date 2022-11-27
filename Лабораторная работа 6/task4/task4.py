import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ",", new_line: str = "\n") -> list[dict]:
    list_dict = []
    with open(filename) as f:
        lines = [line.rstrip(new_line) for line in f]
        list_lines = [line.split(delimiter) for line in lines]
        columns = list_lines[0]
        values = list_lines[1:]
        for i in range(len(values)):
            list_dict.append(dict(zip(columns, values[i])))

        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
