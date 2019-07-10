import sys
script, encoding, error = sys.argv


def main(language_file, encoding, error)
    line = language_file.readline()
    if line:
        print_line(line, encoding, error)
        return main(language_file, encoding, error)


def print_line(line, encoding, error)
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


language = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
