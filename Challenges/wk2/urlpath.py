def url(str):
    website = 'https://example.com'
    path = ''
    i = 0
    j = 0
    #slice whole string with substring 
    if (str[j:j + len(website)]) == website:
        #skip website and get path
        i = (j + len(website))
        #iterate through entire string
        while i < len(str):
            if i + 1 < len(str):
                path += str[i]
                i+=1
            else:
                #end of string
                path += str[i]
                print('path: ', path)
                return path
    print('path: ', path)
    return path

def fileExtension(path):
    dot = '.'
    fileExtension = ''
    i = 0
    j = 0
    for i in range(len(path)):
        if path[i] == dot:
            j = i
            while j + 1 < len(path):
                fileExtension += path[j]
                j += 1
            print('file extension: ', fileExtension)
        if path[i] != dot or i + 1 > len(path):
            return print('[empty string]')



path1 = url('https://example.com/')
path2 = url('https://example.com/foo')
path3 = url('https://example.com/bar.txt')
path4 = url('https://example.com/baz/foo/bar.git')
fileExtension(path1)
fileExtension(path2)
fileExtension(path3)
#fileExtension(path4)
