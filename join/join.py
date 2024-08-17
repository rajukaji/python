def accum(st):
    return '-'.join([ ( st[i].upper() + (st[i].lower() * (i)) ) for i in range( len(st) ) ])

print(accum('abcdefghi'))

'''Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"'''