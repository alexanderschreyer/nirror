import subprocess

from fastapi import FastAPI
from domain.output import Output, get_as_dict


app = FastAPI()


@app.get("/get_outputs")
def get_outputs():
    return get_niri_outputs()


def get_niri_outputs() -> None:
    res = subprocess.run(["niri", "msg", "outputs"], capture_output=True, text=True)
    outputs = parse_niri_outputs(res.stdout)
    return get_as_dict(outputs)


def parse_niri_outputs(stdout: str) -> list[Output]:
    outputs: list[Output] = []
    lines: list[str] = stdout.splitlines()
    for line in lines:
        if "Output" in line:
            line = line.replace('Output "', '')
            parts = line.split('" ')
            name: str = parts[0]
            id: str = parts[1]
            id = id.replace('(', '')
            id = id.replace(')', '')
            outputs.append(Output(id, name))
    return outputs
