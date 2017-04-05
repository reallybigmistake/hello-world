def moreLines(text, num=15):
    lines = text.splitlines()
    while lines:
        show = lines[:num]
        lines = lines[num:]
        for line in show:
            print(line)
        if input('More?') not in ('y', 'Y', ''):
            break
if __name__ == '__main__':
    import sys
    moreLines(sys.__doc__)
    
