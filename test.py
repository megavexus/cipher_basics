import base64

res = []
data = [0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0]
for i in range(len(data)):
    if(i%6):
        res.extend([0,0])
    res.append(data[i])
n = ''.join(chr(data))
print(text_from_bits(n))
print(base64.b64encode(text_from_bits(n)))

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
