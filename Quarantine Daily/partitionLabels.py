class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        def get_end(S,i,j):
            while i <= j:
                if(S[i] == S[j]):
                    return j
                else:
                    j -= 1
            return j
        def find_end(S, i,j):
            #check things
            end = get_end(S,i,j)
            if (i<j):
                while (i < end):
                    if(S[i] != S[i+1]):
                        temp_end = get_end(S, i+1,j)
                        if(temp_end > end):
                            end = temp_end
                    i += 1
                    
            return end
        i,j = 0, len(S)-1
        result = []
        while i<= j:
            temp = find_end(S, i,j)
            result.append((temp - i + 1))

            i = temp + 1
        return result
