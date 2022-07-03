import python.objectdefinition as objectdefinition

'''This method concatenate two list and avoid duplicate'''
def compare(firstlist,secondlist):
    joined_list = [*firstlist,*secondlist]
    return sorted(set(joined_list), key = lambda x: x[x.key()])