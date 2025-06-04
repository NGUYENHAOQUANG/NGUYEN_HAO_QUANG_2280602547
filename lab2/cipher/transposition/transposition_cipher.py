import math
class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        if not text or key <= 0:
            return ""
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        if not text or key <= 0:
            return ""
        num_rows = math.ceil(len(text) / key)
        num_cols = key
        num_empty = (num_rows * num_cols) - len(text)
        grid = [''] * num_cols
        pos = 0
        for col in range(num_cols):
            rows_in_col = num_rows if col < (num_cols - num_empty) else num_rows - 1
            for _ in range(rows_in_col):
                if pos < len(text):
                    grid[col] += text[pos]
                    pos += 1
        decrypted_text = ''
        for row in range(num_rows):
            for col in range(num_cols):
                if row < len(grid[col]):
                    decrypted_text += grid[col][row]
        return decrypted_text
