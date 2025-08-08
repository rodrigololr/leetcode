class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "string_vazia"
    
        if not strs:
            return ""
        return "°°°°°°°°".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "string_vazia":
            return [""]
        return s.split("°°°°°°°°")
