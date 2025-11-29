# left array By One Place
# array=[1,2,3,4,5]
# intial_pos=array[0]
# for i in range(0,len(array)-1):
#         array[i]=array[i+1]
# array[-1]=intial_pos
# print(array)



#Left array By K Places
# array=[1,2,3,4,5,6,7,8]
# k=int(input("Enter the No.Of K places we want to Replace : "))
# shiffting_value=int((len(array)/k)+1)
# temp=[]
# for i in range(0,shiffting_value):
#     temp.append(array[i])
# w=0
# for i in range(shiffting_value,len(array)):
#     array[w]=array[i]
#     w=w+1
# z=0
# for i in range(len(array)-shiffting_value,len(array)):
#     array[i]=temp[z]
#     z+=1
# print(array)

#right rotate by K Places

# array=[1,2,3,4,5,6,7,8]
# d=int(input("Enter the Number You want to Rotate: "))
# intial_array=[]
# if(d>len(array)):
#     value=int(d/len(array))
# else:
#     value=d
# final_str=""
# for i in range(0,value):
#     final_str=str(array[-1])+final_str
#     array.pop()
# for i in final_str:
#     integer=intial_array.append(int(i))
# print(intial_array+array)


# array = [1,2,3,4,5,6,7,8]
# d = int(input("Enter the Number You want to Rotate: "))

# d = d % len(array)  # To handle d > len(array)

# rotated = array[-d:] + array[:-d]

# print(rotated)

#move zeros to the right
# array=[1,0,2,3,0,0,4,5,1]
# length=len(array)
# for i in range(0,length):
#     if(array[i]==0):
#         array.remove(array[i])
#         array.append(0)
# print(array)


# array=[1,0,2,3,0,0,4,5,1]
# length=len(array)
# for i in range(0,len(array)):
#     if(array[i]==0):
#         for j in range(i,len(array)):
#             if(array[j]!=0):
#                 array[i]=array[j]
#                 array[j]=0
#                 break
# print(array)

# array=[1,2,3,4,8,10,12]
# target=int(input("Enter the Number that u want to Search: "))
# for i in range(0,len(array)):
#     if(array[i]==target):
#         print(i)
# if(target not in array):
#     print(-1)

 

#Uninon of Two Sorted Arrays
# arr1=[1,1,1,2,3,4,5]
# arr2=[1,1,1,7,8,9]
# arr3=set()
# for i in range(0,len(arr1)):
#     arr3.add(arr1[i])
# for j in range(0,len(arr2)):
#     arr3.add(arr1[i])
# print(list(arr3))

#Intersection of Two Array

# arr1=[1,2,3,3,4,5,6]
# arr2=[2,3,3,5,6,6,7]
# final_array=[]
# noted=0
# for i in range(0,len(arr1)):
#     for j in range(noted,len(arr2)):
#         if(arr1[i]==arr2[j]):
#             final_array.append(arr1[i])
#             noted=noted+1
#             break
# print(final_array)

# arr1=[1,2,3,3,4,5,6]
# arr2=[2,3,3,5,6,6,7]
# final_array=[]
# noted=0
# for i in range(0,len(arr2)):
#     if(arr1[noted]==arr2[i]):
#         final_array.append(arr1[noted])
#         noted+=1
# print(final_array)



# Finding The Missing Value
# arr=[1,2,4,5]
# for i in range(1,len(arr)+1):
#     flag=0
#     for j in range(0,len(arr)):
#         if(i==arr[j]):
#             flag+=1
#     if(flag==0):
#         print(i)
#         break

# arr=[12,14,18,20]
# diff=arr[-1]-arr[0]
# total_value=diff/len(arr)
# for i in range(0,len(arr)):
#     if(arr[i+1]-arr[i]==diff):
#         continue
#     else:
#         print(arr[i]+diff)
#         break


#Maximum Consecutive Ones
# arr=[1,2,3,1,1,1,3,2,1,1]
# count=0
# max=0
# for i in range(0,len(arr)):
#     if(arr[i]==1):
#         count+=1
#         if(max<count):
#             max=count
#     else:
#         count=0
# print(max)
    


#Find The Number That Appear Once
# arr=[1,1,2,3,3,4,4,5,5]
# ans=0
# for i in range(0,len(arr)-1,2):
#     if(arr[i]!=arr[i+1]):
#         ans=arr[i]
#         break
# print(ans)
        
# arr=[1,1,2,3,3,4,4,5,5]
# ans=0
# for i in range(0,len(arr)):
#     max=0
#     for j in range(0,len(arr)):
#         if(arr[i]==arr[j]):
#             max+=1
#     if(max==1):
#         print(arr[i])
#         break

#Longest Subarray with Sum K
# arr=[2,0,0,3]
# k=3
# longest_subarray=[]
# for i in range(0,len(arr)):
#     sum=0
#     subarray=[]
#     if(arr[i]<k):
#         sum=arr[i]
#         subarray.append(arr[i])
#         for j in range(i+1,len(arr)):
#             if(sum+arr[j]<=k ):
#                 subarray.append(arr[j])
#                 sum+=arr[j]
#             else:
#                 break
#         if(len(longest_subarray)<len(subarray) and sum==k):
#             longest_subarray=subarray
# print(longest_subarray)
#Optimal


# nums = [10, 5, 2, 7, 1, 9]
# k = 15
# n = len(nums)
# maxLen = 0
# left = 0
# right = 0
# sum = nums[0]
# while right < n:
#     while left <= right and sum > k:
#         sum -= nums[left]
#         left += 1
#     if sum == k:
#         maxLen = max(maxLen, right - left + 1)

#     right += 1
#     if right < n:
#         sum += nums[right]

# print(maxLen)  //Check Again And Again

#Two Sum
# arr=[2,6,5,8,11]
# target=10
# count=0
# for i in range(0,len(arr)):
#     for j in range(i,len(arr)):
#         if(arr[i]+arr[j]==target):
#             print(arr[i],arr[j])
#             count+=1
#             break
#     if(count>0):
#         break

#Two Pointer
# arr=[2,6,5,8,11]
# right=0
# left=len(arr)-1
# count=0
# target=50
# while(right<=left):
#     if(arr[right]+arr[left]==target):
#         print(arr[right],arr[left])
#         count+=1
#         break
#     elif(arr[right]+arr[left]>target):
#         left-=1
#     elif(arr[right]+arr[left]<target):
#         right+=1
# if(count==0):
#     print("The Numbers Are Not Found")

#Sort an array of 0's and 1's and 2's
arr=[0,1,2,0,1,2,1,0,0,0,1]
count_0=0
count_1=0
count_2=0
for i in range(0,len(arr)):
    if(arr[i]==0):
        count_0+=1
    elif(arr[i]==1):
        count_1+=1
    else:
        count_2+=1
for i in range(0,count_0):
    arr[i]=0
for j in range(count_0,len(arr)):
    arr[j]=1
for z in range(count_0+count_1,len(arr)):
    arr[z]=2
print(arr)