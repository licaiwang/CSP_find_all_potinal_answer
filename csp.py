from itertools import product

colors = ["Red", "Blue", "Green", "Yellow", ""]
states = ["SA", "WA", "NT", "Q", "NSW", "V", "T"]
neighbors = {}
neighbors["WA"] = ["NT", "SA"]
neighbors["NT"] = ["WA", "SA", "Q"]
neighbors["SA"] = ["WA", "NT", "Q", "NSW", "V"]
neighbors["Q"] = ["NT", "SA", "NSW"]
neighbors["NSW"] = ["Q", "SA", "V"]
neighbors["V"] = ["SA", "NSW"]
neighbors["T"] = []


def get_all_ans() -> list:
    # 目前的解
    all_slove = []
    slove = {}
    for color in product(colors, repeat=7):
        for i, c in enumerate(color):
            slove[states[i]] = c
        all_slove.append(slove)
        slove = {}
    # 4 的 7 方種解 (可重複)
    print(f"There is {len(all_slove)}  sloves in this question")
    return all_slove


def delete_invalid_ans(all_slove: list):
    # 刪掉不符合的解
    is_ans = True
    ans_fit_rule = []
    for ans in all_slove:
        for state in ans.keys():
            for neighbor in neighbors.get(state):
                if ans.get(neighbor) == ans.get(state):
                    is_ans = False
                    break
        if is_ans:
            print(ans)
            ans_fit_rule.append(ans)
        is_ans = True
    return ans_fit_rule


def main():
    print(f"所有可能解：{len(delete_invalid_ans(get_all_ans()))}")


main()
