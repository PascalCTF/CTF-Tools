#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fire, os

class Generator(object):
    FILES = [
        ('attachments/.gitkeep', ''), ('src/.gitkeep', ''), ('writeup/README.md', 'TODO'),
        ('checker/__main__.py', bytes.fromhex('23212f7573722f62696e2f656e7620707974686f6e330a0a696d706f7274206f730a696d706f72742072657175657374730a66726f6d2070776e20696d706f7274202a0a696d706f7274206c6f6767696e670a6c6f6767696e672e64697361626c6528290a0a2320506572206c65206368616c6c656e6765207765620a55524c203d206f732e656e7669726f6e2e676574282255524c222c2022687474703a2f2f746f646f2e6368616c6c732e746f646f2e697422290a69662055524c2e656e64737769746828222f22293a0a20202055524c203d2055524c5b3a2d315d0a0a23205365206368616c6c656e6765207463700a484f5354203d206f732e656e7669726f6e2e6765742822484f5354222c2022746f646f2e6368616c6c732e746f646f2e697422290a504f5254203d20696e74286f732e656e7669726f6e2e6765742822504f5254222c20333430303129290a0a2320436865636b206368616c6c656e67650a666c6167203d2022666c61677b746f646f7d220a7072696e7428666c6167290a').decode()),
        ('authors.txt', 'TODO Nome Cognome <@nickname>'), ('description.md', 'TODO'), 
        ('endpoint.txt', 'tcp,todo.challs.todo.it,1337'), ('flags.txt', 'flag{todo}'), 
        ('order.txt', '0'), ('points.txt', '500'), ('tags.txt', ''),
        ('timeout.txt', '10'), ('title.txt', 'challenge')
    ]

    def new(self, category, name='challenge'):
        for f in self.FILES:
            path = os.path.join(name, f[0])
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if f[0] == 'tags.txt':
                with open(path, 'w') as file:
                    file.write(f'{category}\n')
                continue
            with open(path, 'w') as file:
                file.write(f'{f[1]}\n')

if __name__ == '__main__':
    fire.Fire(Generator)