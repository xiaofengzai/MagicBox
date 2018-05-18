def difference(list1,list2):
    return list(set(list1).difference(set(list2)))
  
def ascDifference(list1,list2):
    return sorted(list(set(list1).difference(set(list2))))
  
def descDifference(list1,list2):
    return sorted( list(set(list1).difference(set(list2))),reverse=True)
  
def union(list1,list2):
    return list(set(list1) |(set(list2)))
  
def ascUnion(list1,list2):
    return sorted(list(set(list1) |(set(list2))))
  
def descUnion(list1,list2):
    return sorted(list(set(list1) |(set(list2))),reverse=True)
  
def intersection(list1,list2):
    return list(set(list1) & (set(list2)))
  
def ascIntersection(list1,list2):
    return sorted(list(set(list1) & (set(list2))))
  
def descIntersection(list1,list2):
    return sorted(list(set(list1) & (set(list2))),reverse=True) 
  
  
  
