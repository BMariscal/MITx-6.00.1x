#Problem 9

# Write a function to flatten a list. The list contains other lists, strings,
#  or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened 
#  into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#     ''' 
#     aList: a list 
#     Returns a copy of aList, which is a flattened version of aList 
#     '''
  






def flatten(aList):    
    
    flat_list = []
    for i in aList:
        if type(i) == type([]):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list






print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))