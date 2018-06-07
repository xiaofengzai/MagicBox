def difference(list1,list2):
    """ get different element in two list """
    return list(set(list1).difference(set(list2)))
  
def ascDifference(list1,list2):
    """ get different element in two list order asc"""
    return sorted(list(set(list1).difference(set(list2))))
  
def descDifference(list1,list2):
    """ get different element in two list order desc"""
    return sorted( list(set(list1).difference(set(list2))),reverse=True)
  
def union(list1,list2):
    """ get all element in two list remove the Repeated"""
    return list(set(list1) |(set(list2)))
  
def ascUnion(list1,list2):
    """ get all element in two list remove the Repeated order asc"""
    return sorted(list(set(list1) |(set(list2))))
  
def descUnion(list1,list2):
    """ get all element in two list remove the Repeated order desc"""
    return sorted(list(set(list1) |(set(list2))),reverse=True)
  
def intersection(list1,list2):
    """ get same element in two list """
    return list(set(list1) & (set(list2)))
  
def ascIntersection(list1,list2):
    """ get same element in two list  order asc"""
    return sorted(list(set(list1) & (set(list2))))
  
def descIntersection(list1,list2):
    """ get same element in two list  order desc"""
    return sorted(list(set(list1) & (set(list2))),reverse=True) 
  
  
  
