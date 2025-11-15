from pathlib import Path
import argparse, csv, json

FILES = [
    "title.txt", "description.md", "tags.txt", "points.txt", 
    "flags.txt", ""
]

TYPE = "dynamic" #TODO: change to static or dynamic based on CTF type
STATE = "visible" #TODO: change to hidden or visible based on CTF state
MAX_ATTEMPTS = 0 #TODO: change to max attempts if applicable
MINIMUM_POINTS = 50 #TODO: change to minimum points if applicable
DECAY_POINTS = 50 #TODO: change to decay points if applicable

def load_challenge(path: Path):
    assert all((path / file).exists() for file in FILES if file), f"Missing required files in {path}"
    
    files = {file: (path / file).read_text().strip() for file in FILES if file}

    return {
        "name": files["title.txt"],
        "description": files["description.md"],
        "category": files["tags.txt"],
        "value": files["points.txt"],
        "type": TYPE,
        "state": STATE,
        "max_attempts": MAX_ATTEMPTS,
        "flags": files["flags.txt"],
        "tags": "",
        "hints": "",
        "type_data": json.dumps(
            {
                "initial": files["points.txt"],
                "minimum": MINIMUM_POINTS,
                "decay": DECAY_POINTS,
            }
        ),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a CTF into a CSV from a specified path.")
    parser.add_argument("path", type=str, help="The path to the CTF directory.")
    args = parser.parse_args()

    ctf_path = Path(args.path)
    ctfd = csv.writer(open("challenges.csv", "w", newline=""))
    
    for dir in ctf_path.iterdir():
        if dir.is_dir():
            ctfd.writerow(load_challenge(dir))