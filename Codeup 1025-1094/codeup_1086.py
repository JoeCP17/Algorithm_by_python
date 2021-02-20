w, h , b  = map(int,input().split())


aa = w * h * b

aa_bit = aa / 8
aa_byte = aa_bit / 1024
aa_mb = aa_byte / 1024

print("%.2f MB" %aa_mb)