nums=[]
nums1=[]
for i in range(1,5000):
        nums.append(i%5)
for i in range(5000,10001):
        nums1.append(i%5)
nums2=nums+nums1
if(set(nums).union(set(nums1))==set(nums2)):
    print("your lists are valid")
else:
    print("your lists are invalid")