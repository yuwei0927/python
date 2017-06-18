s ="""<a target ="new" title ="Python 06 vim" href="http://www.tudou.com/programs/view/myLEA7IrHx4/">Python 06 vim</a>"""

url = s[s.find ("href") + 6 : s. find ("\">")]

print(url)
