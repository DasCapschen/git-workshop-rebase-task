def main():
    translate_str = input("Enter Translation in form X,Y,Z: ")
    tx, ty, tz = translate_str.split(",")
    tx = float(tx.strip())
    ty = float(ty.strip())
    tz = float(tz.strip())

    translate_matrix = [
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ]

    print("Your final Transformation Matrix is: ")
    for i in range(4):
        print("[", end="")
        for j in range(4):
            print(f"{translate_matrix[i][j]:9.2f}", end="")
        print("]")


if __name__ == "__main__":
    main()
