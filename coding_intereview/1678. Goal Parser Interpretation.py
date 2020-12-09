class Solution:
    def interpret(self, command: str) -> str:
        last_str = ""
        out = ''
        for i in range(len(command)):
            current_str = command[i]
            if current_str == ")":
                if last_str == "(":
                    out = out + "o"
            elif current_str == "(":
                pass
            else:
                out = out + current_str
            last_str = current_str
        return(out)
