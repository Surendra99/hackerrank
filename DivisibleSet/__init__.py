from StdSuites.AppleScript_Suite import list_2c__record_or_text
from _ast import Num
class DivisibleSetCalculator:
    def divisibleSetCalculator(self,key,numSet):
        rem_dict = {}
        resultSet = set()
        if len(numSet) <=1:
            return len(numSet)
        for num in numSet:
            rem=num%key
            num_list = rem_dict.get(rem,[])
            num_list.append(num)
            rem_dict[rem] = num_list
        for num in rem_dict.keys():
            if num == key-num or num == 0:
                resultSet |=set([rem_dict[num][0]])
                continue
            list_num = rem_dict[num]
            list_numc =  rem_dict.get(key-num,[])
            if len(list_num) <= len(list_numc):
                resultSet|=set(list_numc)
            else:
                resultSet|=set(list_num)
        return resultSet