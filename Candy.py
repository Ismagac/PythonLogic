def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    candies = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    return sum(candies)

def test_candy():
    assert candy([1, 0, 2]) == 5      
    assert candy([3, 2, 1]) == 6  
    assert candy([1]) == 1             
    assert candy([2, 2, 2]) == 3       
    assert candy([1, 2, 3, 4, 5]) == 15 
    assert candy([5, 4, 3, 2, 1]) == 15 

test_candy()