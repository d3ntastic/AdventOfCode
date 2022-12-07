import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    template = input[0]
    replacements = [x.split(' -> ') for x in input[2:]]
    return template, replacements


def part_one():
    template, replacements = read_input('./testinput.txt')
    for i in range(10):
        print("Iteration: {}".format(i))
        new_template = template
        current_replacements = []
        for replacement in replacements:
            find = replacement[0]
            find_result = [i for i in range(len(new_template)) if new_template.startswith(find, i)]
            for result in find_result:
                current_replacements.append([result + 1, replacement[1]])
        current_replacements.sort(key=lambda x: x[0], reverse=True)
        for replacement in current_replacements:
            new_template = new_template[:replacement[0]] + replacement[1] + new_template[replacement[0]:]
        template = new_template
    # get list of all letters and their counts
    counts = [template.count(x) for x in set(template)]
    counts.sort()
    return counts[-1] - counts[0]

def part_two():
    template, replacements = read_input('./input.txt')
    letter_pairs = {}
    letter_counts = {}
    for i in range(len(template)):
        pair = template[i:i+2]
        if len(pair) == 2:
            if pair in letter_pairs:
                letter_pairs[pair] += 1
            else:
                letter_pairs[pair] = 1
        if template[i] in letter_counts:
            letter_counts[template[i]] += 1
        else:
            letter_counts[template[i]] = 1

    for i in range(40):
        print("Iteration: {}".format(i))
        new_pairs = {}

        for replacement in replacements:
            find = replacement[0]
            if find not in letter_pairs or letter_pairs[find] == 0: continue
            number_of_replacements = letter_pairs[find]
            letter_pairs[find] = 0

            if find[0] + replacement[1] in new_pairs:
                new_pairs[find[0] + replacement[1]] += number_of_replacements
            else:
                new_pairs[find[0] + replacement[1]] = number_of_replacements

            if replacement[1] + find[1] in new_pairs:
                new_pairs[replacement[1] + find[1]] += number_of_replacements
            else:
                new_pairs[replacement[1] + find[1]] = number_of_replacements

            if replacement[1] in letter_counts:
                letter_counts[replacement[1]] += number_of_replacements
            else:
                letter_counts[replacement[1]] = number_of_replacements

        for pair in new_pairs:
            if pair in letter_pairs:
                letter_pairs[pair] += new_pairs[pair]
            else:
                letter_pairs[pair] = new_pairs[pair]
        
    letter_counts = list(letter_counts.values())
    letter_counts.sort()
    return letter_counts[-1] - letter_counts[0]

def main():
    #print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()