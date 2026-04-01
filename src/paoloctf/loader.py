#!/usr/bin/env python3
"""Loader module for parsing CTF challenges into CSV format."""

import csv
import json
from pathlib import Path
from typing import Dict, Any, List


class Loader:
    """Parse CTF challenge directories into CTFd-compatible CSV format."""
    
    # Required files for a valid challenge
    REQUIRED_FILES = [
        "title.txt",
        "description.md", 
        "tags.txt",
        "points.txt",
        "flags.txt",
    ]
    
    # Default configuration
    DEFAULT_CONFIG = {
        "type": "dynamic",      # dynamic or static scoring
        "state": "visible",     # visible or hidden
        "max_attempts": 0,      # 0 = unlimited
        "minimum_points": 50,   # minimum points for dynamic scoring
        "decay_points": 50,     # decay rate for dynamic scoring
    }
    
    def __init__(self, **config):
        """Initialize loader with optional custom configuration.
        
        Args:
            **config: Override default configuration values
        """
        self.config = {**self.DEFAULT_CONFIG, **config}
    
    def load_challenge(self, path: Path) -> Dict[str, Any]:
        """Load a single challenge from a directory.
        
        Args:
            path: Path to the challenge directory
            
        Returns:
            Dictionary with challenge data ready for CSV export
            
        Raises:
            FileNotFoundError: If required files are missing
        """
        # Validate required files exist
        missing = [f for f in self.REQUIRED_FILES if not (path / f).exists()]
        if missing:
            raise FileNotFoundError(
                f"Missing required files in {path}: {', '.join(missing)}"
            )
        
        # Read all required files
        files = {
            name: (path / name).read_text().strip() 
            for name in self.REQUIRED_FILES
        }
        
        return {
            "name": files["title.txt"],
            "description": files["description.md"],
            "category": files["tags.txt"],
            "value": files["points.txt"],
            "type": self.config["type"],
            "state": self.config["state"],
            "max_attempts": self.config["max_attempts"],
            "flags": files["flags.txt"],
            "tags": "",
            "hints": "",
            "type_data": json.dumps({
                "initial": int(files["points.txt"]),
                "minimum": self.config["minimum_points"],
                "decay": self.config["decay_points"],
            }),
        }
    
    def parse(self, path: str, output: str = "challenges.csv") -> List[Dict[str, Any]]:
        """Parse all challenges in a directory to CSV.
        
        Args:
            path: Path to the CTF directory containing challenge subdirectories
            output: Output CSV filename
            
        Returns:
            List of challenge dictionaries that were exported
        """
        ctf_path = Path(path)
        challenges = []
        
        if not ctf_path.exists():
            raise FileNotFoundError(f"CTF directory not found: {path}")
        
        # Collect all valid challenges
        for challenge_dir in sorted(ctf_path.iterdir()):
            if challenge_dir.is_dir() and not challenge_dir.name.startswith('.'):
                try:
                    challenge = self.load_challenge(challenge_dir)
                    challenges.append(challenge)
                except FileNotFoundError as e:
                    print(f"Warning: Skipping {challenge_dir.name}: {e}")
        
        if not challenges:
            print("Warning: No valid challenges found")
            return []
        
        # Write to CSV
        fieldnames = list(challenges[0].keys())
        with open(output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(challenges)
        
        return challenges
