## Wordcount

# Ejemplo para casos de uso
# python3 -m homework data/input data/output


import argparse

from homework.src._internals.read_all_lines import read_all_lines


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def preprocess_lines(lines):
    pass


def split_into_words(preprocessed_lines):
    pass


def count_words(words):
    pass


def write_word_count(output_path, word_count):
    pass


def main():
    input, output = parse_args()
    lines = read_all_lines(input)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_count = count_words(words)
    write_word_count(output, word_count)
