
class List(list):
    def __init__(self, arr=[]):
        self.arr = arr
        super().__init__(self.arr)

    def __getitem__(self, ind_key, curr_arr=None):
        if curr_arr is None:
            curr_arr = self.arr
        if  isinstance(ind_key, int):
            return curr_arr[ind_key]
        if len(ind_key) == 1: 
            return curr_arr[ind_key[0]]
        if  isinstance(ind_key, tuple): 
            return self.__getitem__(ind_key[1:],curr_arr[ind_key[0]])


mylist = List([
[[1,2,3,33],[4,5,6,66]],
[[7,8,9,99],[10,11,12,122]],
[[13,14,15,155],[16,17,18,188]],
])
print(mylist[0,1,3]) 
print(mylist[2,0,0])
print(mylist[2,0,1]) 
print(mylist[0]) 
    