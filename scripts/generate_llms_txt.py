#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate llms.txt file for Context7 based on examples directory.
This script scans the examples directory, extracts code examples and their descriptions,
and formats them according to the Context7 llms.txt format.

Note: This script follows PEP 8 style guidelines.
"""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os
import re
import codecs
import argparse
import importlib
import inspect
from pathlib import Path

# Constants
SEPARATOR = "-" * 40
REPO_URL = "https://github.com/phenom-films/dayu_widgets"


def get_example_files(examples_dir):
    """Get all example files from the examples directory."""
    result = []
    for file_name in os.listdir(examples_dir):
        if file_name.startswith("__") or not file_name.endswith(".py") or file_name == "demo.py":
            continue
        result.append(file_name)
    return result


def extract_class_docstring(file_path):
    """Extract the class docstring from a file."""
    with codecs.open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Find class definition
    class_match = re.search(r"class\s+(\w+)\(.*\):", content)
    if not class_match:
        return None, None

    class_name = class_match.group(1)

    # Try to find docstring
    docstring_match = re.search(r'class\s+{}.*?:\s*[\'"]([^\'"]*)[\'"]'.format(class_name), content, re.DOTALL)
    if docstring_match:
        return class_name, docstring_match.group(1).strip()

    return class_name, None


def extract_main_example(file_path, class_name):
    """Extract the main example code from a file."""
    with codecs.open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Find the main example code (the if __name__ == "__main__" block)
    main_match = re.search(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?=\n\S|$)", content, re.DOTALL)
    if main_match:
        main_code = main_match.group(1).strip()
        return main_code

    return None


def extract_init_ui_method(file_path, class_name):
    """Extract the _init_ui method from a class."""
    with codecs.open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Find the _init_ui method
    init_ui_match = re.search(r"def\s+_init_ui\s*\(\s*self.*?\):(.*?)(?=\n\s*def|\n\s*if\s+__name__|$)", content, re.DOTALL)
    if init_ui_match:
        init_ui_code = init_ui_match.group(1).strip()
        return init_ui_code

    return None


def format_code_snippet(title, description, source, language, code):
    """Format a code snippet according to the Context7 llms.txt format."""
    snippet = f"TITLE: {title}\n"
    snippet += f"DESCRIPTION: {description}\n"
    snippet += f"SOURCE: {source}\n"
    snippet += f"LANGUAGE: {language}\n"
    snippet += f"CODE: ```\n{code}\n```"
    return snippet


def generate_llms_txt(examples_dir, output_file):
    """Generate the llms.txt file."""
    example_files = get_example_files(examples_dir)
    snippets = []

    for file_name in example_files:
        file_path = os.path.join(examples_dir, file_name)
        class_name, docstring = extract_class_docstring(file_path)

        if not class_name:
            continue

        # Extract main example
        main_code = extract_main_example(file_path, class_name)
        if main_code:
            title = f"Using {class_name} Widget"
            description = docstring or f"Example of how to use the {class_name} widget from dayu_widgets library."
            source = f"{REPO_URL}/blob/master/examples/{file_name}#L1"
            snippets.append(format_code_snippet(title, description, source, "Python", main_code))

        # Extract _init_ui method
        init_ui_code = extract_init_ui_method(file_path, class_name)
        if init_ui_code:
            title = f"Initializing {class_name} UI"
            description = f"Example of how to initialize and configure the UI for {class_name} widget."
            source = f"{REPO_URL}/blob/master/examples/{file_name}#L1"
            snippets.append(format_code_snippet(title, description, source, "Python", init_ui_code))

    # Add import example
    import_snippet = format_code_snippet(
        "Importing dayu_widgets in Python",
        "This code snippet demonstrates how to import the dayu_widgets library into a Python script. This import statement is the prerequisite for using any of the UI components provided by the library.",
        f"{REPO_URL}/blob/master/README.md#L1",
        "Python",
        "import dayu_widgets"
    )
    snippets.insert(0, import_snippet)

    # Write to file
    with codecs.open(output_file, "w", encoding="utf-8") as f:
        f.write("\n{}\n".format(SEPARATOR).join(snippets))

    print(f"Generated {output_file} with {len(snippets)} code snippets.")


def main():
    parser = argparse.ArgumentParser(description="Generate llms.txt file for Context7")
    parser.add_argument("--examples-dir", default="examples", help="Path to examples directory")
    parser.add_argument("--output", default="llms.txt", help="Output file path")
    args = parser.parse_args()

    examples_dir = os.path.abspath(args.examples_dir)
    output_file = os.path.abspath(args.output)

    generate_llms_txt(examples_dir, output_file)


if __name__ == "__main__":
    main()
