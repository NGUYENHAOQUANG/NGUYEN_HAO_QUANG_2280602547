from flask import Flask, request, jsonify
from cipher.caesar import caesarCipher


from cipher.vigenere import VigenereCipher
app = Flask(__name__)


cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['Key']
    encrypted_text = cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    encrypted_text = data['encrypted_text']
    key = data['Key']
    decrypted_text = cipher.vigenere_decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})

caesar_cipher =caesarCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data=request.json
    plain_text = data['plain_text']
    key = int(data['Key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encryoted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['Key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decryted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)