"""
   Exercise - 7: Find the Runner-Up Score
   Given the participants score sheet for your University Sports Day, 
   you are required to find the runner-up score. You are given n scores. 
   Store them in a list and find the score of the runner-up.
    
   Sample Input 0
   5
   2 3 6 6 5
   
   Sample Output 0
   5
    
    Cassio Cioni Carmo - 04/01/2023
"""

if __name__ == '__main__':
    n = int(input("Insert how many score:"))
    score_list = list(map(int, input("Insert score list:").split()))
    
    score_list_sorted = sorted(score_list, reverse = True)
   
    score_max = score_list_sorted[0]
    
    for i in range(len(score_list_sorted)):
        if score_max > score_list_sorted[i]:
            runner_up = score_list_sorted[i]
            break
        
    print(runner_up)
