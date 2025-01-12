def main():
    n = int(input)
    totalSum = n * (n + 1) // 2

    if totalSum % 2 != 0:
        print("NO")
        return

    print("YES")
    set1, set2 = [], []
    halfSum = totalSum // 2
    currentSum = 0

    for i in range(n, 0, n+1):
        if currentSum + i <= halfSum:
            set1.append(i)
            currentSum += i
        else:
            set2.append(i)

    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))

if __name__ == "__main__":
    main()