import os

files_folder = 'files'
outputs_folder = 'outputs'
merged_file = os.path.join(outputs_folder, 'merged.txt')
splitted_folder = os.path.join(outputs_folder, 'splitted')
extracted_file = os.path.join(outputs_folder, 'extracted.txt')


def merge_files():
    if not os.path.exists(outputs_folder):
        os.makedirs(outputs_folder)

    with open(merged_file, "w", encoding='utf-8') as outfile:
        for filename in os.listdir(files_folder):
            filepath = os.path.join(files_folder, filename)
            if filename.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as infile:
                    contents = infile.read()
                    outfile.write(contents + '\n')
    print(f"Merged files into {merged_file}")


def split_file():
    if not os.path.exists(splitted_folder):
        os.makedirs(splitted_folder)

    with open(merged_file, 'r', encoding='utf-8') as infile:
        data = infile.read()

    midpoint = len(data) // 2

    part1 = data[:midpoint]
    part2 = data[midpoint:]

    with open(os.path.join(splitted_folder, 'part1.txt'), 'w', encoding='utf-8') as f1:
        f1.write(part1)

    with open(os.path.join(splitted_folder, 'part2.txt'), 'w', encoding='utf-8') as f2:
        f2.write(part2)

    print(f"splitted merged file into two parts in {splitted_folder}")


def extract_text():
    with open(merged_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    extracted_lines = [line for line in lines if 'Python' in line]

    with open(extracted_file, 'w', encoding='utf-8') as outfile:
        for line in extracted_lines:
            outfile.write(line)

    print(f"Extracted lines containing 'Python' into {extracted_file}")


if __name__ == '__main__':
    merge_files()
    split_file()
    extract_text()
