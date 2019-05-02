import discord, random, os,sys
from discord.ext import commands
class bot(discord.Client):
    async def on_ready(self):
        print('Logged in as',self.user.name,self.user.id)
    async def on_message(self, m):
        print(m)
        try:
            if m.author.id != self.user.id and m.content.startswith('!help'):
                await m.channel.send("""Команды:
                !help - помощь
                !шар - случайный ответ в виде Да/Нет или из списка вида [1;2]
                !ролл X,Y - случайное число от X до Y
                \n
                Команды админа текстового канала:
                !erase all/x - удаление всех/x последних сообщений в текстовом канале
                """)
            elif m.author.id == self.user.id:
                return
            # sosi
            if (m.content.find('соси')!=-1 or m.content.find('саси')!=-1 or m.content.find('sosi')!=-1 or m.content.find('sasi')!=-1 or m.content.find('suck')!=-1 or m.content.find('сак ')!=-1) and m.author.id != self.user.id:
                print(m.author.id)
                await m.channel.send('Сам соси, '+str(m.author.mention))
            if (m.content.find('сука')!=-1 or m.content.find('suka')!=-1 or m.content.find('cyka')!=-1 or m.content.find('cerf')!=-1 or m.content.find('bitch')!=-1 or m.content.find('бич')!=-1) and m.author.id != self.user.id:
                print(m.author.id)
                await m.channel.send('Сам сука, '+str(m.author.mention))
            ### erase
            elif m.content.startswith('!erase'):
                if m.channel.permissions_for(m.author).manage_messages:
                    if m.content.startswith('!erase all'):
                        await m.delete()
                        await m.channel.send('Команда отключена',delete_after=5.0)
                    elif m.content.split(' ')[1].isdigit() and len(m.content.split(' '))==2:
                        ncount=int(m.content.split(' ')[1])+1
                        count=0
                        async for message in m.channel.history():
                            await message.delete()
                            count+=1
                            if count==ncount:
                                break
                        await m.channel.send('Было удалено '+str(count-1)+' сообщений',delete_after=5.0)
                    else:
                        await m.channel.send('Неправильное использование команды!',delete_after=5.0)
                else:
                    await m.delete()
                    await m.channel.send('Недостаточно прав!',delete_after=5.0)
            ### шар
            if m.content.startswith('!шар'):
                if len(m.content)==4:
                    if random.randint(0, 1) > 0:
                        await m.channel.send('Да')
                    else:
                        await m.channel.send('Нет')
                elif m.content.startswith('!шар ') and m.content.find('[')!=-1 and m.content.find(']')!=-1 and m.content.find(';')!=-1 and len(m.content)!='!шар [;]':
                    solve=m.content.split('[')[1].split(']')[0].split(';')
                    await m.channel.send(solve[random.randint(0,len(solve)-1)])
                else:
                    await m.delete()
                    await m.channel.send('Неправильное использование команды!',delete_after=5)
            ### ролл
            if m.content.startswith('!ролл'):
                if m.content.startswith('!ролл ') and m.content.find(',') and len(m.content) >=8 and len(m.content.split(' ')[1].split(','))==2:
                    solve = m.content.split(' ')[1].split(',')
                    if solve[0].isdigit() and solve[1].isdigit():
                        await m.channel.send(random.randint(int(solve[0]),int(solve[1])))
                    else:
                        await m.delete()
                        await m.channel.send('Неправильное использование команды!', delete_after=5)
                else:
                    await m.delete()
                    await m.channel.send('Неправильное использование команды!', delete_after=5)
        except:
            await m.channel.send('Ошибка бота!Сообщите администратора об условиях возникновения ошибки!Инициализирован перезапуск!')
            os.execl(sys.executable, 'python3.6', __file__, *sys.argv[1:])

bot = bot()
bot.run('NTcxMTA3NTQxODA3NzkyMTM4.XMJAyQ.l3gkY-zS_WSdO5r52DROgc5_vIA')