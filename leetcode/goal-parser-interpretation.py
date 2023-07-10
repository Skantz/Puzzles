class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        return "".join(s for s in command if s not in ["(", ")"])
