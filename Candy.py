def candy(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    candies = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)

print(candy([1,0,2]))         # 5
print(candy([1,2,2]))         # 4
print(candy([2,4,2,6,1,7,8,9,2,1]))  # 19
