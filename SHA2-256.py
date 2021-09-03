def NOT(bits):
    return [not bit for bit in bits]
def AND(bits_a, bits_b):
    return [bit_a and bits_b[i] for i, bit_a in enumerate(bits_a)]
def XOR(bits_a, bits_b):
    return [bit_a != bits_b[i] for i, bit_a in enumerate(bits_a)]
def sumaMOD2_32(bits_a, bits_b):
    bits_a = bits_a[::-1]
    bits_b = bits_b[::-1]
    n_a = 0
    n_b = 0
    for i, bit_a in enumerate(bits_a):
        n_a += bit_a*2**i
        n_b += bits_b[i]*2**i
    return intToBits((n_a+n_b)%2**32, 32)
def RotR(bits, n):
    return bits[-n:]+bits[:-n]
def ShR(bits, n):
    bits = bits[:-n]
    for bit in range(n):
        bits.insert(0, False)
    return bits

def sigma0(bits):
    return XOR(XOR(RotR(bits, 7), RotR(bits, 18)), ShR(bits, 3))
def sigma1(bits):
    return XOR(XOR(RotR(bits, 17), RotR(bits, 19)), ShR(bits, 10))
def Ch(bits_a, bits_b, bits_c):
    return XOR(AND(bits_a, bits_b), AND(NOT(bits_a), bits_c))
def Maj(bits_a, bits_b, bits_c):
    return XOR(XOR(AND(bits_a, bits_b), AND(bits_a, bits_c)), AND(bits_b, bits_c))
def sumatorio0(bits):
    return XOR(XOR(RotR(bits, 2), RotR(bits, 13)), RotR(bits, 22))
def sumatorio1(bits):
    return XOR(XOR(RotR(bits, 6), RotR(bits, 11)), RotR(bits, 25))

def intToBits(n, l):
    bits = []
    while n > 0:
        bits.append(bool(n%2))
        n = n//2
    while len(bits) < l:
        bits.append(False)
    return bits[::-1]
def textToBits(text):
    text = ''.join(format(ord(i), '08b') for i in text)
    bits = []
    for t in text:
        bits.append(bool(int(t)))
    return bits

def algorithm(text):
    bits = textToBits(text)
    bits.append(True)
    for bit in range((448-len(text)*8-1) % 512):
        bits.append(False)
    bits = bits+intToBits(len(text)*8, 64)
    n=[]
    for i in range(len(bits)//512):
        n.append(bits[i*512:512*(i+1)])
    k = [[False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False],[False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True],[True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True],[True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True],[False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True],[False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True],[True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False],[True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True],[True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False],[False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True],[False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False],[False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True],[False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False],[True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False],[True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True],[True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False],[True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True],[True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False],[False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False],[False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False],[False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True],[False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False],[False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False],[False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False],[True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False],[True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True],[True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False],[True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True],[True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True],[True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True],[False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True],[False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True],[False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True],[False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False],[False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False],[False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True],[False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False],[False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True],[True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False],[True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True],[True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True],[True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True],[True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False],[True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True],[True,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True],[True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False],[True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True],[False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False],[False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False],[False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False],[False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False],[False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True],[False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True],[False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False],[False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True],[False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True],[False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False],[False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True],[True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False],[True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False],[True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False],[True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True],[True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True],[True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False]]
    h = [[False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True],[True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True],[False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False],[True,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False],[False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True],[True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False],[False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True],[False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True]]
    for n_ in n:
        a_ = h[0]
        b_ = h[1]
        c_ = h[2]
        d_ = h[3]
        e_ = h[4]
        f_ = h[5]
        g_ = h[6]
        h_ = h[7]
        w = []
        for i in range(16):
            w.append(n_[i*32:32*(i+1)])
        for i in range(48):
            w.append(sumaMOD2_32(sumaMOD2_32(sumaMOD2_32(sigma1(w[i+16-2]), w[i+16-7]), sigma0(w[i+16-15])), w[i+16-16]))
        for i, w_ in enumerate(w):
            T1 = sumaMOD2_32(sumaMOD2_32(sumaMOD2_32(sumaMOD2_32(h_, sumatorio1(e_)), Ch(e_, f_, g_)), k[i]), w_)
            T2 = sumaMOD2_32(sumatorio0(a_), Maj(a_, b_, c_))
            h_ = g_
            g_ = f_
            f_ = e_
            e_ = sumaMOD2_32(d_, T1)
            d_ = c_
            c_ = b_
            b_ = a_
            a_ = sumaMOD2_32(T1, T2)
        h[0] = sumaMOD2_32(a_, h[0])
        h[1] = sumaMOD2_32(b_, h[1])
        h[2] = sumaMOD2_32(c_, h[2])
        h[3] = sumaMOD2_32(d_, h[3])
        h[4] = sumaMOD2_32(e_, h[4])
        h[5] = sumaMOD2_32(f_, h[5])
        h[6] = sumaMOD2_32(g_, h[6])
        h[7] = sumaMOD2_32(h_, h[7])
    bits = h[0]+h[1]+h[2]+h[3]+h[4]+h[5]+h[6]+h[7]
    b = ""
    for i in range(64):
        n = bits[i*4:4*(i+1)]
        if not n[0] and not n[1] and not n[2] and not n[3]:
            b += "0"
        elif not n[0] and not n[1] and not n[2] and n[3]:
            b += "1"
        elif not n[0] and not n[1] and n[2] and not n[3]:
            b += "2"
        elif not n[0] and not n[1] and n[2] and n[3]:
            b += "3"
        elif not n[0] and n[1] and not n[2] and not n[3]:
            b += "4"
        elif not n[0] and n[1] and not n[2] and n[3]:
            b += "5"
        elif not n[0] and n[1] and n[2] and not n[3]:
            b += "6"
        elif not n[0] and n[1] and n[2] and n[3]:
            b += "7"
        elif n[0] and not n[1] and not n[2] and not n[3]:
            b += "8"
        elif n[0] and not n[1] and not n[2] and n[3]:
            b += "9"
        elif n[0] and not n[1] and n[2] and not n[3]:
            b += "A"
        elif n[0] and not n[1] and n[2] and n[3]:
            b += "B"
        elif n[0] and n[1] and not n[2] and not n[3]:
            b += "C"
        elif n[0] and n[1] and not n[2] and n[3]:
            b += "D"
        elif n[0] and n[1] and n[2] and not n[3]:
            b += "E"
        elif n[0] and n[1] and n[2] and n[3]:
            b += "F"
        else:
            print(n)
    return b

if __name__ == "__main__":
    print(algorithm(input("Write your message: ")))
