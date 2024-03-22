  
def common_elements(set_1, set_2):
       """
       A function that returns a set of
       common elements in two sets
       """
       return (set_1 & set_2)

#Example Usage :    
            
#common_elements = __import__.common_elements


set_1 = {12,2,5,6,8}
set_2 = {12,4,2,1,4}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
