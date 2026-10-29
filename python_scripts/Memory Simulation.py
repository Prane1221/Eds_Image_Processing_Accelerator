W, H = 6, 6
img = [[r * W + c + 1 for c in range(W)] for r in range(H)]
buf1, buf2 = [0] * W, [0] * W
win = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ref = lambda r, c: [img[r - 2 + i][c - 2:c + 1] for i in range(3)]
all_ok = True
for r in range(H):
    for c in range(W):
        p = img[r][c]
        new_col = [buf2[c], buf1[c], p]
        for i in range(3):
            win[i][0] = win[i][1]
            win[i][1] = win[i][2]
            win[i][2] = new_col[i]
        buf2[c], buf1[c] = buf1[c], p
        if r >= 2 and c >= 2:
            match = win == ref(r, c)
            all_ok = all_ok and match
            print(f"({r},{c}) {'OK' if match else 'FAIL'}")
print("MATCH" if all_ok else "ERR")