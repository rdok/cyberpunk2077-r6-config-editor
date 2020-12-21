import pytest

from src.config import Config
from src.transformers.key_transformer import KeyTransformer

config = Config()

key_transformer = KeyTransformer()


class TestKeyTransformer():
    @pytest.mark.parametrize("input, output", [
        ('Caps_Lock', 'CapsLock'), ('Alt_', 'Alt'), ('Control_L', 'Ctrl'),
        ('Control_R', 'Ctrl'), ('Shift_L', 'LShift')])
    def test_it_transforms_keys_to_cyberpunk2077_ones(self, input, output):
        assert key_transformer.transform(input) == output
