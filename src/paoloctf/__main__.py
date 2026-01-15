#!/usr/bin/env python3
"""CLI entry point for paoloctf."""

import argparse
import sys

from . import __version__
from .generator import Generator
from .loader import Loader


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="paoloctf",
        description="CLI tool for creating and managing CTF challenges for PascalCTF.",
        epilog="For more information, visit: https://github.com/PascalCTF/CTF-Tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    
    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        metavar="<command>",
    )
    
    # Generate command
    gen_parser = subparsers.add_parser(
        "generate",
        aliases=["gen", "new"],
        help="Create a new CTF challenge directory structure",
        description="Generate a new CTF challenge with all required files and folders.",
        epilog="""
Examples:
  paoloctf generate web
  paoloctf generate pwn --name buffer_overflow
  paoloctf gen crypto --name rsa_challenge
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    gen_parser.add_argument(
        "category",
        metavar="CATEGORY",
        help="Challenge category (e.g., web, pwn, crypto, misc, forensics, rev)",
    )
    gen_parser.add_argument(
        "-n", "--name",
        default="challenge",
        metavar="NAME",
        help="Name of the challenge directory (default: challenge)",
    )
    
    # Load command
    load_parser = subparsers.add_parser(
        "load",
        aliases=["export"],
        help="Export CTF challenges to CSV for CTFd import",
        description="Parse CTF challenge directories and export them to a CTFd-compatible CSV file.",
        epilog="""
Examples:
  paoloctf load ./challenges
  paoloctf load ./ctf --output ctfd_import.csv
  paoloctf export ./challenges -o export.csv
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    load_parser.add_argument(
        "path",
        metavar="PATH",
        help="Path to the directory containing CTF challenge subdirectories",
    )
    load_parser.add_argument(
        "-o", "--output",
        default="challenges.csv",
        metavar="FILE",
        help="Output CSV filename (default: challenges.csv)",
    )
    
    return parser


def cmd_generate(args: argparse.Namespace) -> int:
    """Handle the generate command."""
    generator = Generator()
    
    try:
        path = generator.new(args.category, args.name)
        print(f"Created challenge '{args.name}' in ./{path}/")
        print(f"  Category: {args.category}")
        print(f"  Edit the files in the directory to configure your challenge.")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_load(args: argparse.Namespace) -> int:
    """Handle the load command."""
    loader = Loader()
    
    try:
        challenges = loader.parse(args.path, args.output)
        if challenges:
            print(f"Exported {len(challenges)} challenge(s) to '{args.output}'")
            for ch in challenges:
                print(f"  - {ch['name']} [{ch['category']}]")
        return 0
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.command is None:
        parser.print_help()
        print("\nUse 'paoloctf <command> --help' for more information on a command.")
        return 0
    
    # Route to command handlers
    if args.command in ("generate", "gen", "new"):
        return cmd_generate(args)
    elif args.command in ("load", "export"):
        return cmd_load(args)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
