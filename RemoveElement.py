class Solutiongit :
    def removeElement(self,nums,val):
    # print(len(nums))
        temp=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[j]!=val):
                    temp.append(nums[i])
                break
        return temp




solution=Solution()
nums = [3,2,2,3,5,2,3,4]
val = 2
result=solution.removeElement(nums,val)
print("\nval=",val,"Removed from list",nums,"\n")
print("Now the list is",result,"\n")       
