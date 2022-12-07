def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    signal_patterns = [x.replace("\n", "").split(' | ')[0].split(" ") for x in lines]
    output_values = [x.replace("\n", "").split(' | ')[1].split(" ") for x in lines]
    return signal_patterns, output_values

def part_one():
    signal_patterns, output_values = read_input('input.txt')
    number_of_searched = 0
    for outputline in output_values:
        for output_value in outputline:
            if len(output_value) in [2, 3, 4, 7]:
                number_of_searched += 1
    return number_of_searched

def part_two():
    signal_patterns, output_values = read_input('input.txt')
    found_outputs = []
    segment_mapping = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }
    for line_id, outputline in enumerate(output_values):
        signal_pattern = signal_patterns[line_id]
        signal_pattern_occurences = {
            'e': 0,
            'b': 0,
            'd': 0,
            'g': 0,
            'a': 0,
            'c': 0,
            'f': 0,
        }
        pattern_mapping = {
            'a': '',
            'b': '',
            'c': '',
            'd': '',
            'e': '',
            'f': '',
            'g': '',
        }
        one_pattern = ''
        four_pattern = ''
        for signal_patter_digit in signal_pattern:
            if len(signal_patter_digit) == 2:
                one_pattern = signal_patter_digit
            if len(signal_patter_digit) == 4:
                four_pattern = signal_patter_digit
            for letter in signal_patter_digit:
                signal_pattern_occurences[letter] += 1
        
        for signal_pattern_letter in signal_pattern_occurences:
            number_of_occurance = signal_pattern_occurences[signal_pattern_letter]
            if (number_of_occurance == 4):
                pattern_mapping[signal_pattern_letter] = 'e'
            elif (number_of_occurance == 6):
                pattern_mapping[signal_pattern_letter] = 'b'
            elif (number_of_occurance == 7):
                if signal_pattern_letter in four_pattern:
                    pattern_mapping[signal_pattern_letter] = 'd'
                else:
                    pattern_mapping[signal_pattern_letter] = 'g'
            elif (number_of_occurance == 8):
                if signal_pattern_letter in one_pattern:
                    pattern_mapping[signal_pattern_letter] = 'c'
                else:
                    pattern_mapping[signal_pattern_letter] = 'a'            
            elif (number_of_occurance == 9):
                pattern_mapping[signal_pattern_letter] = 'f'

        current_real_output = ''
        for output_value in outputline:
            new_output_value = ''
            for output_value_letter in output_value:
                new_output_value += pattern_mapping[output_value_letter]
            sorted_characters = sorted(new_output_value)
            new_output_value = "".join(sorted_characters)
            current_real_output += str(segment_mapping[new_output_value])
        found_outputs.append(int(current_real_output))

    return sum(found_outputs)

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()