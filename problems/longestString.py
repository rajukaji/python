def longest_consec(strarr, k):
    # lst = [strarr[i] + strarr[i+1] for i in range(len(strarr)-k+1)]
    # return max(lst)
    
    #codewars
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))