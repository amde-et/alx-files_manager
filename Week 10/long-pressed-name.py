class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[-1] != typed[-1] or len(set(name)) > len(set(typed)):
            return False
        name_pointer = 0
        typed_pointer = 0
        while name_pointer <= len(name) - 1:
            if (typed_pointer == len(typed) - 1 and name_pointer != len(name) - 1) or name[name_pointer] != typed[typed_pointer]:
                return False
            if name_pointer != len(name) - 1 and name[name_pointer] != name[name_pointer + 1]:
                while typed_pointer <= len(typed) - 1 and name[name_pointer] == typed[typed_pointer]:
                    typed_pointer += 1
                name_pointer += 1
            elif name_pointer == len(name) - 1:
                if ''.join(set(typed[typed_pointer:])) == name[name_pointer]:
                    return True
                else:
                    return False
            else:
                typed_pointer += 1
                name_pointer += 1