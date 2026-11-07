class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
    
        people=list(zip(heights,names))
        people.sort(reverse=True)
        print(people)
        res=[]
        for i in range(0,len(people)):
            res.append(people[i][1])
        return res