def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # time O(Nmlogm)
    sorted_strs = {}
    for string in strs:  # O(N)
        # Record letter frequence
        # Produce sorted string
        # Add string to the dict
        sorted_string = "".join(sorted(string))  # O(mlogm)
        if sorted_string in sorted_strs:
            sorted_strs[sorted_string].append(string)
        else:
            sorted_strs[sorted_string] = [string]
    return sorted_strs.values()

# try to do with O(Nm) runtime next time