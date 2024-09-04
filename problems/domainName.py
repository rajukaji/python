def domain_name(url):
    for i in url.split('.'):
        if i == 'www' or i == 'http://www' or i == 'https://www':
            continue
        
        if not 'www' in i and '://' in i:
            for j in i.split('://'):
                if 'http' in j:
                    continue
                
                return j
        
        return i
    

    # return url.split("//")[-1].split("www.")[-1].split(".")[0]
    # from code wars,,,

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

print(domain_name('http://github.com/carbonfive/raygun'))
print(domain_name('http://www.zombie-bites.com'))
print(domain_name('https://www.cnet.com'))
print(domain_name('www.xakep.ru'))
print(domain_name('icann.org'))

