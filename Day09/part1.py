
def main():
    with open('./input.txt') as file:
        total = 0

        for line in file:
            line = line.strip()

            rows = []
            nums = [int(x) for x in line.split()]
            rows.append(nums)

            allZeros = len([x for x in nums if x != 0]) == 0

            while not allZeros:
                row = []
                current_row = rows[-1]
                allZeros = True

                for i in range(1, len(current_row)):
                    prev_num = current_row[i-1]
                    current_num = current_row[i]
                    diff = current_num - prev_num
                    row.append(diff)
                    if diff != 0:
                        allZeros = False

                rows.append(row)

            for i in range(len(rows) - 2, -1, -1):
                current_row = rows[i]
                prev_row = rows[i+1]
                current_num = current_row[-1] + prev_row[-1]
                current_row.append(current_num)

            total += rows[0][-1]

    print(total)


if __name__ == '__main__':
    main()
