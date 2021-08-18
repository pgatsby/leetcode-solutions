# Peter Gatsby
# Problem: https://leetcode.com/explore/interview/card/google/67/sql-2/3046/

trees = [3,3,3,1,2,1,1,2,3,3,4]
# trees = [0,1,6,6,4,4,6]

def totalTrees(trees):
    max_trees = 0
    mostTrees = {}
    current_tree = 0
    for i in range(len(trees)):
        if trees[i] not in mostTrees: 
            mostTrees[trees[i]] = 1 
        else: 
            mostTrees[trees[i]] += 1
        while len(mostTrees) > 2: 
            mostTrees[trees[current_tree]] -= 1
            if mostTrees[trees[current_tree]] == 0:
                del mostTrees[trees[current_tree]]
            
            current_tree +=1
        
        max_trees = max(max_trees, i- current_tree +1)

    return max_trees


print(totalTrees(trees))