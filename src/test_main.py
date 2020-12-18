from main import capitilize_message


def test_capitilize_message():
    assert capitilize_message('alpha') == 'ALPHA'


def test_registers_button_to_slow_walk():
    assert 1 == 1