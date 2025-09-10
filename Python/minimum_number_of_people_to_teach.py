"""
[September 10th 2025]
Problem: 1733

On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.


"""
from typing import Optional, List 

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:     
        """
        Naive backtracking method, did not work with large arrays

       
        def problems(languages, friendships):
            problems = []
            for friendship in friendships:
                problem = True
                for language in languages[friendship[0]-1]:
                    if language in languages[friendship[1]-1]:
                        problem = False
                        break
                        
                if problem == True:
                    problems.append(friendship)
            return problems
        
        def solve(ans, languages): 
            newProblems = problems(languages, friendships)
            print(newProblems)
            if len(newProblems) == 0:
                return ans

            temp = 999999
            ans += 1

            for problem in newProblems:
                for i in languages[problem[1]-1]: # Problem means there is no language in common at all!
                    languages[problem[0]-1].append(i)
                    
                    newTemp = solve(ans, languages)
                    if newTemp < temp:
                        temp = newTemp
                    languages[problem[0]-1].pop()
                # for i in languages [problem[0]-1]:
                #     languages[problem[1]-1].append(i)
                #     newTemp = solve(ans, languages)
                #     if newTemp < temp:
                #         temp = newTemp
                #     languages[problem[1]-1].pop()

            return temp
        return solve(0, languages)
        """

        """
        Greedy method: which works as explained on leetcode
        """
        problems = set()
        lang_count = [0 for _ in range (n)]

        for friendship in friendships:
            problem = True
            for language in languages[friendship[0]-1]:
                if language in languages[friendship[1]-1]:
                    problem = False
                    break
            if problem == True:
                print(friendship)
                problems.update(friendship)
        
        for entry in problems:
            for i in languages[entry-1]:
                lang_count[i-1] += 1
        
        print(lang_count, )
        return len(problems) - max(lang_count)
