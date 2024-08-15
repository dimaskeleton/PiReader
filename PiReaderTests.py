from PiReader import *

def test_read_file():
    content = read_file("pi_million_digits.txt")
    assert content.startswith("3.14")

def test_read_file_not_found():
    content = read_file("non_existent_file.txt")
    assert content == "The file was not found"

def test_digit_frequency():
    freq = digit_frequency("839239759234")
    assert freq['1'] == 0
    assert freq['5'] == 1
    assert freq['2'] == 2
    assert freq['3'] == 3

def test_digit_search():
    result_found = digit_search("928374574205778234582845", "577")
    assert result_found == "The sequence 577 was found at position 11 in the pi digits."

    result_not_found = digit_search("31415994856829243", "629")
    assert result_not_found == "The sequence 629 was not found in the pi digits."

def test_remove_digit():
    test_file_import = "pi_removed_digits.txt"
    test_file = read_file(test_file_import)
    assert "8" not in test_file

# Updated tests to make sure file handling works properly with all the functions

def test_read_file_with_specific_content():
    file_path = 'pi_tester.txt'
    contents = read_file(file_path)
    expected_start = "3.1415926535979"
    assert contents.startswith(expected_start)

def test_read_file_not_found():
    non_existent_file = 'file_deleted.txt'
    content = read_file(non_existent_file)
    assert content == "The file was not found"


def test_digit_frequency_from_file():
    file_path = 'pi_tester.txt'
    contents = read_file(file_path)
    expected_frequency = {'0': 0, '1': 2, '2': 1, '3': 2, '4':  1, '5': 3, '6': 1, '7': 1, '8': 0, '9': 3}
    frequency = digit_frequency(contents)
    assert frequency == expected_frequency

def test_digit_search_from_file():
    file_path = 'pi_tester.txt'
    sequence = "979"
    expected_position = 12
    contents = read_file(file_path)
    result = digit_search(contents, sequence)
    assert f"The sequence {sequence} was found at position {expected_position}" in result

def test_digit_search_sequence_not_found_in_file():
    file_path = 'pi_tester.txt'
    sequence_not_in_file = "9999"
    contents = read_file(file_path)
    result = digit_search(contents, sequence_not_in_file)
    assert result == f"The sequence {sequence_not_in_file} was not found in the pi digits."

def test_remove_digit_and_check_file():
    input_file_path = 'pi_tester.txt'
    output_file_path = 'pi_digit_removal_test.txt'
    digit_to_remove = "9"
    contents = read_file(input_file_path)
    remove_digit(contents, digit_to_remove, output_file_path)

    updated_contents = read_file(output_file_path)
    assert digit_to_remove not in updated_contents
