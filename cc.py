timeout = 3.0
bigtimeout = 30.0
def cjcb(s):
    if s.find('соси')!=-1 or s.find('саси')!=-1 or s.find('sosi')!=-1 or s.find('sasi')!=-1 or s.find('suck')!=-1 or s.find('сак ')!=-1:
        return True
    return False
def cerf(s):
    if s.find('сука')!=-1 or s.find('suka')!=-1 or s.find('cyka')!=-1 or s.find('cerf')!=-1 or s.find('bitch')!=-1 or s.find('бич')!=-1:
        return  True
    return False
def shar(s):
    if (s.startswith('!шар [')  or s.startswith('!ball [')) and s.find('[') != -1 and s.find('[') == s.rfind('[') and s.find(']') != -1 and s.find(']')==s.rfind(']') and s.find(';') != -1 and len(s) >= 11:
        return True
    return False
def shar_list(s):
    for elem in s.split('[')[1].split(']')[0].split(';'):
        if elem=='':
            return False
    return True