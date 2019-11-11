def Miller_Rabin_test(number):
    a = 2
    k = 1
    q = 0
    result = 0
    while q % 2 == 0:
        q  = (number-1) / (2**k)
        k+=1

    if a**q % number == 1:
        return 1
    for i in range(0, k):
        if a**(2*i*q) % number == number-1:
            return 1

    return 0

def mod_inverse(a, m):
    a = a%m
    for i in range(1, m+1):
        if (a*i) % m == 1:
            return i

def Encryption(M, e, n):
    return M**e % n

def Decryption(C, d, p, q, n):
    a_1 = C**(d % (p-1)) % p;
    a_2 = C**(d % (q-1)) % q;
    c_1 = (n/p) * mod_inverse(n/p, p);
    c_2 = (n/q) * mod_inverse(n/q, q);

    return (a_1*c_1 + a_2*c_2) % n;

M = 2
e = 23
n = 56153
p = 0
q = 0
C = Encryption(M, e, n)
for i in range(233, 242):
    for j in range(233, 242):
        if  i*j == n:
            p = i
            q = j

d = mod_inverse(e, (p-1)*(q-1))
for i in range(233, 242, 2):
    print(str(Miller_Rabin_test(i)) + "-" + str(i))
print("Answer - " + str(Decryption(C, d, p, q, n)))
