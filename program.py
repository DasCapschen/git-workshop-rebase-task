def main():
    translate_str = input("Enter Translation in form X,Y,Z: ")
    tx, ty, tz = translate_str.split(",")
    tx = float(tx.strip())
    ty = float(ty.strip())
    tz = float(tz.strip())

    scale_str = input("Enter scaling in form X,Y,Z: ")
    sx, sy, sz = scale_str.split(',')
    sx = float(sx.strip())
    sy = float(sy.strip())
    sz = float(sz.strip())

    st_matrix = [
        [sx, 0, 0, tx],
        [0, sy, 0, ty],
        [0, 0, sz, tz],
        [0, 0, 0,  1]
    ]

    print("Your final Transformation Matrix is: ")
    for i in range(4):
        print("[", end="")
        for j in range(4):
            print(f"{st_matrix[i][j]:9.2f}", end="")
        print("]")


if __name__ == "__main__":
    main()
