import pytest

from src.Config import Config
from src.transformers.KeyTransformer import KeyTransformer

config = Config()

key_transformer = KeyTransformer()


class TestKeyTransformer:
    @pytest.mark.parametrize("input, output", [
        ('Caps_Lock', 'CapsLock'), ('Alt_', 'Alt'), ('Control_L', 'Ctrl'),
        ('Control_R', 'Ctrl'), ('Shift_L', 'LShift')])
    def test_it_normalizes_keys(self, input, output):
        assert key_transformer.transform(input) == output
