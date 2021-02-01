        t = '^#'+'#'.join(s)+'#$'
        c = r = 0                             
        for i in range(1,len(t)-1):
            j = 1 if t[i] == '#' else 2       
            while  t[i-j] == t[i+j]: j += 2
            if j > r: c, r = i, j
        return s[(c-r+1)//2:(c+r-1)//2]
