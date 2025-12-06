import os


def write_word_count(output_path, word_count):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file = os.path.join(output_path, "wordcount.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in word_count.items():
            f.write(f"{word}\t{count}\n")
