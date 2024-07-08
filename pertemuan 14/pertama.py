p = 11
q = 5
r = 4
bool_a = (p - r) == (r + q)
print("a. ((p - r) == (r + q)):", bool_a)
bool_b = ((p % 3) + q) != (r % 2)
print("b. (((p % 3) + q) != (r % 2)):", bool_b)
bool_c = (q - 3) == (p % 2 + q)
print("c. ((q - 3) == (p % 2 + q)):", bool_c)
bool_d = (r + q) != ((p * 2) % 2)
print("d. ((r + q) != ((p * 2) % 2)):", bool_d)
bool_e = ((q % 3) + p) > (r % 2)
print("e. ((((q % 3) + p) > (r % 2))):", bool_e)
bool_f = (r + p) <= (q * 5)
print("f. (((r + p) <= (q * 5))):", bool_f)