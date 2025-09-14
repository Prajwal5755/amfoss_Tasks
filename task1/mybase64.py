import base64

n = int(input("Enter 1 for ascii to base64, 2 for base64 to ascii: "))

if n == 1:
    s = input("Enter ascii: ")
    s_bytes = s.encode()
    encoded = base64.b64encode(s_bytes)
    print(encoded.decode())
else:
    s = input("Enter base64: ")
    s_bytes = s.encode()
    decoded_bytes = base64.b64decode(s_bytes)
    print(decoded_bytes.decode()) 

