

def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, \
        f"expected {expected_result}, got {actual_result}"


def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


test_substring('1','1')
