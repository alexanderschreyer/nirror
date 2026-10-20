class Output:
    def __init__(self, output_id, output_name):
        self.output_id = output_id
        self.output_name = output_name

    
def get_as_dict(outputs: list[Output]) -> dict[str, str]:
    as_list: list[dict[str, str]] = []
    for output in outputs:
        as_dict: dict[str, str] = {}
        as_dict["id"] = output.output_id
        as_dict["name"] = output.output_name
        as_list.append(as_dict)
    final: dict[str, list[dict[str, str]]] = {"outputs" : as_list}
    return final