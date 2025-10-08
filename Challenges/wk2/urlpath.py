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
                return print('path: ', path)
    print('path: ', path)

url('https://example.com/')
url('https://example.com/foo')
url('https://example.com/bar.txt')
url('https://example.com/baz/foo/bar.git')