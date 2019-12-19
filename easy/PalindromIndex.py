class PalindromIndex:
    def find_index(self,string):
        for index in range(0,len(string)/2):
            rev = len(string)-1-index
            if string[index] != string[rev]:
                new_str = string[:rev] + string[rev+1:]
                if len(new_str)%2!=0:
                    new_str = new_str[:len(new_str)/2] + new_str[(len(new_str)/2)+1:]
                firstpart, secondpart = new_str[:len(new_str)/2], new_str[len(new_str)/2:][::-1]
                if firstpart == secondpart:
                    return rev
                else:
                    return index
        return -1