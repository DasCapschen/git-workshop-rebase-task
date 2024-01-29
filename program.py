from math import sin, cos


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

    rotate_str = input("Enter Rotation as Euler Angles in Form X,Y,Z: ")
    rx, ry, rz = rotate_str.split(',')
    rx = float(rx.strip()) * (3.1415926 / 180.0)
    ry = float(ry.strip()) * (3.1415926 / 180.0)
    rz = float(rz.strip()) * (3.1415926 / 180.0)

    rx_matrix = [
        [ 1,       0,        0, 0],
        [ 0, cos(rx), -sin(rx), 0],
        [ 0, sin(rx),  cos(rx), 0],
        [ 0,       0,        0, 1]
    ]
    ry_matrix = [
        [ cos(ry), 0, sin(ry), 0],
        [       0, 1,       0, 0],
        [-sin(ry), 0, cos(ry), 0],
        [       0, 0,       0, 1]
    ]
    rz_matrix = [
        [cos(rz), -sin(rz), 0, 0],
        [sin(rz),  cos(rz), 0, 0],
        [      0,        0, 1, 0],
        [      0,        0, 0, 1]
    ]

    rot_matrix = multiply_matrix(rx_matrix, ry_matrix)
    rot_matrix = multiply_matrix(rot_matrix, rz_matrix)

    res = multiply_matrix(translate_matrix, rot_matrix)

    print("Your final Transformation Matrix is: ")
    for i in range(4):
        print("[", end="")
        for j in range(4):
            print(f"{res[i][j]:9.2f}", end="")
        print("]")


def multiply_matrix(a, b):
    c = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                c[i][j] += (a[i][k] * b[k][i])
    return c


if __name__ == "__main__":
    main()
