# 6. Lambda for squaring
square = lambda x: x ** 2

if __name__ == "__main__":
    print("=== Lambda, Map & Filter ===")

    # 6. Lambda Square
    num = int(input("Enter an integer to square: "))
    print(f"Square of {num}:", square(num))

    # 7. map() Cubes
    raw_nums = input("\nEnter space-separated numbers to cube (e.g., 1 2 3 4): ")
    cubed_list = list(map(lambda x: int(x) ** 3, raw_nums.split()))
    print("Cubed values:", cubed_list)

    # 8. filter() Odds
    filter_nums = input("\nEnter space-separated numbers to filter odd ones: ")
    odds_list = list(filter(lambda x: int(x) % 2 != 0, map(int, filter_nums.split())))
    print("Odd numbers only:", odds_list)