kol_vo_chisel = int(input())
if kol_vo_chisel % 2 == 0:
    for i in range(1, kol_vo_chisel // 2 + 1):
        print(i, end=" ")
    for i in range(kol_vo_chisel // 2, 0, -1):
        print(i, end=" ")
else:
    for i in range(1, kol_vo_chisel // 2 + 2):
        print(i, end=" ")
    for i in range(kol_vo_chisel // 2, 0, -1):
        print(i, end=" ")