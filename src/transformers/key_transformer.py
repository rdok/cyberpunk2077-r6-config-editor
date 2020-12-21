class KeyTransformer:
    def transform(self, key):
        if key == 'Caps_Lock':
            return 'CapsLock'
        if key.startswith('Alt_'):
            return 'Alt'
        if key.startswith('Shift_L'):
            return 'LShift'
        if key.startswith('Control_'):
            return 'Ctrl'

        return key
