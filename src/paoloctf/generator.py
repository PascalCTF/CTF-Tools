#!/usr/bin/env python3
"""Generator module for creating CTF challenge directory structures."""

from pathlib import Path


CHECKER_TEMPLATE = """\
#!/usr/bin/env python3

import os
import requests
from pwn import *
import logging
logging.disable()

# Per le challenge web
URL = os.environ.get("URL", "http://todo.challs.todo.it")
if URL.endswith("/"):
    URL = URL[:-1]

# Se challenge tcp
HOST = os.environ.get("HOST", "todo.challs.todo.it")
PORT = int(os.environ.get("PORT", 34001))

# Check challenge
flag = "flag{todo}"
print(flag)
"""


class Generator:
    """Generate CTF challenge directory structures compliant with CTF-Checker."""

    # Files to create with their default content
    FILES = [
        ("attachments/.gitkeep", ""),
        ("src/.gitkeep", ""),
        ("writeup/README.md", "TODO"),
        ("checker/__main__.py", CHECKER_TEMPLATE),
        ("authors.txt", "TODO Nome Cognome <@nickname>"),
        ("description.md", "TODO"),
        ("endpoint.txt", "tcp,todo.challs.todo.it,1337"),
        ("flags.txt", "flag{todo}"),
        ("order.txt", "0"),
        ("points.txt", "500"),
        ("tags.txt", ""),
        ("timeout.txt", "10"),
        ("title.txt", "challenge"),
    ]

    def new(self, category: str, name: str = "challenge") -> Path:
        """Create a new CTF challenge directory structure.

        Args:
            category: The challenge category (e.g., web, pwn, crypto, misc)
            name: The name of the challenge directory

        Returns:
            Path to the created challenge directory

        Raises:
            FileExistsError: If the challenge directory already exists
        """
        challenge_path = Path(name)

        if challenge_path.exists():
            raise FileExistsError(
                f"Directory '{name}' already exists. "
                "Choose a different name or remove the existing directory."
            )

        for filename, content in self.FILES:
            file_path = challenge_path / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Special handling for tags.txt - use the category
            if filename == "tags.txt":
                file_path.write_text(f"{category}\n")
            elif filename == "title.txt":
                file_path.write_text(f"{name}\n")
            else:
                file_path.write_text(f"{content}\n" if content else "\n")

        return challenge_path
