W, H, w, h = map(int, input().split())

if W >= w and H >= h:
    print('STRAIGHT')
elif W >= h and H >= w:
    print('TURN')
else:
    print('NO')