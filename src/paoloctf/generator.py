#!/usr/bin/env python3
"""Generator module for creating CTF challenge directory structures."""

import os
from pathlib import Path


class Generator:
    """Generate CTF challenge directory structures compliant with CTF-Checker."""
    
    # Default checker template (hex-encoded to preserve formatting)
    CHECKER_TEMPLATE = bytes.fromhex(
        '23212f7573722f62696e2f656e7620707974686f6e330a0a696d706f7274206f730a'
        '696d706f72742072657175657374730a66726f6d2070776e20696d706f7274202a0a'
        '696d706f7274206c6f6767696e670a6c6f6767696e672e64697361626c6528290a0a'
        '2320506572206c65206368616c6c656e6765207765620a55524c203d206f732e656e'
        '7669726f6e2e676574282255524c222c2022687474703a2f2f746f646f2e6368616c'
        '6c732e746f646f2e697422290a69662055524c2e656e64737769746828222f22293a'
        '0a20202055524c203d2055524c5b3a2d315d0a0a23205365206368616c6c656e6765'
        '207463700a484f5354203d206f732e656e7669726f6e2e6765742822484f5354222c'
        '2022746f646f2e6368616c6c732e746f646f2e697422290a504f5254203d20696e74'
        '286f732e656e7669726f6e2e6765742822504f5254222c20333430303129290a0a23'
        '20436865636b206368616c6c656e67650a666c6167203d2022666c61677b746f646f'
        '7d220a7072696e7428666c6167290a'
    ).decode()
    
    # Files to create with their default content
    FILES = [
        ('attachments/.gitkeep', ''),
        ('src/.gitkeep', ''),
        ('writeup/README.md', 'TODO'),
        ('checker/__main__.py', CHECKER_TEMPLATE),
        ('authors.txt', 'TODO Nome Cognome <@nickname>'),
        ('description.md', 'TODO'),
        ('endpoint.txt', 'tcp,todo.challs.todo.it,1337'),
        ('flags.txt', 'flag{todo}'),
        ('order.txt', '0'),
        ('points.txt', '500'),
        ('tags.txt', ''),
        ('timeout.txt', '10'),
        ('title.txt', 'challenge'),
    ]
    
    def new(self, category: str, name: str = 'challenge') -> Path:
        """Create a new CTF challenge directory structure.
        
        Args:
            category: The challenge category (e.g., web, pwn, crypto, misc)
            name: The name of the challenge directory
            
        Returns:
            Path to the created challenge directory
        """
        challenge_path = Path(name)
        
        for filename, content in self.FILES:
            file_path = challenge_path / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Special handling for tags.txt - use the category
            if filename == 'tags.txt':
                file_path.write_text(f'{category}\n')
            else:
                file_path.write_text(f'{content}\n' if content else '\n')
        
        return challenge_path
