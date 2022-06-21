def climbingLeaderboard(rank, ply):
    # Write your code here
    arr=sorted(list(set(rank)), reverse = True)#eliminates duplicates
    r=[]
    
    for n in range(len(ply)):
        for m in range(len(arr)):
            if ply[n]<min(arr):
                r.append(len(arr)+1)
                break
            elif ply[n]>=arr[m]:
                r.append(m+1)
                break
            else:
                continue
            
    return(r)
  
  """
  problem statement: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
  """
