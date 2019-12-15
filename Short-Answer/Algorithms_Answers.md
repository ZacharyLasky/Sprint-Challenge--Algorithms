#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N). I think this is O(N) because a = 0 would be 1, while (a < n * n * n) would be O(N), and a = a + n * n would be 1. 


b) O(N^2). I think this is O(N^2) because sum = 0 would be 1, for i in range(n) would be O(N), j = 1 would be 1, while j < n would be O(N), j *= 2 would be 1, and sum += 1 would be 1. 


c) O(N). I think this is O(N) because if bunnies == 0 would be 1, return 0 would be 1, return 2 + bunnyEars(bunnies-1) would be O(N) since there's 1 recursion happening. If there were 2 recursions happening I think it would be O(2N). 

## Exercise II

My solution would define a function called building. It would take 2 parameters called egg_floor and building_height. I'd define 2 variables called not_broken and broken, each having a runtime of 1. I'd have a while loop that says while egg_floor is greater than or equal to building_height, if egg_floor is less than building height, not_broken adds 1. While loop has runtime O(N), if statement has runtime of 1, and not_broken has runtime of 1. My else statement would say broken adds 1 and a recursive call would have building_height - 1. Else has runtime of 1, broken has runtime of 1, and recursive call has runtime of O(N). The runtime of this function is O(N^2). 
