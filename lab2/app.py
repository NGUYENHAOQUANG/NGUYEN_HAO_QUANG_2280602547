from flask import Flask, render_template, request
from cipher.caesar import caesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

# Router route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for encryption
@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        cipher_type = request.form['cipher_type']
        text = request.form['inputText']
        key = request.form['inputKey']
        
        if not text or not key:
            return "Lỗi: Text và Key không được để trống!"
        
        result = ""
        
        if cipher_type == 'caesar':
            cipher = caesarCipher()
            result = cipher.encrypt_text(text, int(key))
        elif cipher_type == 'playfair':
            
            if not key.isalpha():
                return "Lỗi: Playfair cipher chỉ nhận khóa là chữ cái (A-Z), không phải số!"
            cipher = PlayFairCipher()
            matrix = cipher.create_playfair_matrix(key)
            result = cipher.playfair_encrypt(text, matrix)
        elif cipher_type == 'railfence':
            cipher = RailFenceCipher()
            result = cipher.rail_fence_encrypt(text, int(key))
        elif cipher_type == 'transposition':
            cipher = TranspositionCipher()
            result = cipher.encrypt(text, int(key))
        elif cipher_type == 'vigenere':
           
            if not key.isalpha():
                return "Lỗi: Vigenère cipher chỉ nhận khóa là chữ cái (A-Z), không phải số!"
            cipher = VigenereCipher()
            result = cipher.vigenere_encrypt(text, key)
        else:
            return "Lỗi: Loại mã hóa không hợp lệ!"
            
        return f"Mã hóa thành công!  Kết quả: {result}"
        
    except ValueError:
        return "Lỗi: Key phải là số nguyên cho Caesar, Rail Fence và Transposition cipher!"
    except Exception as e:
        return f"Lỗi: {str(e)}"


@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        cipher_type = request.form['cipher_type']
        text = request.form['inputText']
        key = request.form['inputKey']
        
        if not text or not key:
            return "Lỗi: Text và Key không được để trống!"
        
        result = ""
        
        if cipher_type == 'caesar':
            cipher = caesarCipher()
            result = cipher.decrypt_text(text, int(key))
        elif cipher_type == 'playfair':
            
            if not key.isalpha():
                return "Lỗi: Playfair cipher chỉ nhận khóa là chữ cái (A-Z), không phải số!"
            cipher = PlayFairCipher()
            matrix = cipher.create_playfair_matrix(key)
            result = cipher.playfair_decrypt(text, matrix)
        elif cipher_type == 'railfence':
            cipher = RailFenceCipher()
            result = cipher.rail_fence_decrypt(text, int(key))
        elif cipher_type == 'transposition':
            cipher = TranspositionCipher()
            result = cipher.decrypt(text, int(key))
        elif cipher_type == 'vigenere':
            
            if not key.isalpha():
                return "Lỗi: Vigenère cipher chỉ nhận khóa là chữ cái (A-Z), không phải số!"
            cipher = VigenereCipher()
            result = cipher.vigenere_decrypt(text, key)
        else:
            return "Lỗi: Loại mã hóa không hợp lệ!"
            
        return f"Giải mã thành công! Kết quả: {result}"
        
    except ValueError:
        return "Lỗi: Key phải là số nguyên cho Caesar, Rail Fence và Transposition cipher!"
    except Exception as e:
        return f"Lỗi: {str(e)}"

# Main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
