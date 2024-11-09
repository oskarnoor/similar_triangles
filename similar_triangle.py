def len_side(cords: list) -> int:
    x1, y1, x2, y2 = cords
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def triangle_side_from_cord(cords: list) -> list:
    s1 = [cords[0], cords[1], cords[2], cords[3]]
    s2 = [cords[2], cords[3], cords[4], cords[5]]
    s3 = [cords[0], cords[1], cords[4], cords[5]]

    return [len_side(s1), len_side(s2), len_side(s3)]


def main():
    kolmnurk1 = [int(x) for x in input().split()]  # 0 0 6 0 0 3
    kolmnurk2 = [int(x) for x in input().split()]  # -1 3 1 -1 -1 -1
    nurk1 = triangle_side_from_cord(kolmnurk1)
    nurk2 = triangle_side_from_cord(kolmnurk2)
    nurk1 = sorted(nurk1)
    nurk2 = sorted(nurk2)
    if nurk1[0] >= nurk2[0]:
        dif = nurk1[0] / nurk2[0]
        for i in range(2):
            if round(nurk2[i + 1] * dif, 4) == round(nurk1[i + 1], 4):
                continue
            else:
                print(-1)
                quit()
        print(round(dif, 4))
        quit()
    else:
        dif = nurk2[0] / nurk1[0]
        for i in range(2):
            if round(nurk1[i + 1] * dif, 4) == round(nurk2[i + 1], 4):
                continue
            else:
                print(-1)
                quit()
        print(round(dif, 4))
        quit()


if __name__ == "__main__":
    main()
