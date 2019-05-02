timeout = 3.0
helpcommtxt = """Команды:
                !help - помощь
                !шар - случайный ответ в виде Да/Нет или из списка вида [1;2]
                !ролл X,Y - случайное число от X до Y
                \n
                Команды админа текстового канала:
                !erase all/x - удаление всех/x последних сообщений в текстовом канале
                """
def cjcb(s):
    if s.find('соси')!=-1 or s.find('саси')!=-1 or s.find('sosi')!=-1 or s.find('sasi')!=-1 or s.find('suck')!=-1 or s.find('сак ')!=-1:
        return True
    return False
def cerf(s):
    if s.find('сука')!=-1 or s.find('suka')!=-1 or s.find('cyka')!=-1 or s.find('cerf')!=-1 or s.find('bitch')!=-1 or s.find('бич')!=-1:
        return  True
    return False
def shar(s):
    if s.startswith('!шар ') and s.find('[') != -1 and s.find(']') != -1 and s.find(';') != -1 and len(s) != '!шар [;]':
        return True
    return False
def shar_list(s):
    for elem in s.split('[')[1].split(']')[0].split(';'):
        if elem=='':
            return False
    return True