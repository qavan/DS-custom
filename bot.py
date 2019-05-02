import discord, random, os,sys,cc
from discord.ext import commands
class bot(discord.Client):
    async def on_ready(self):
        print('Logged in as',self.user.name,self.user.id)
    async def on_message(self, m):
        if m.author.id == self.user.id:
            return
        if cc.cjcb(m.content) and m.author.id != self.user.id:
            await m.channel.send('Сам соси, '+str(m.author.mention))
        if cc.cerf(m.content) and m.author.id != self.user.id:
            await m.channel.send('Сам сука, '+str(m.author.mention))
        try:
            if m.content.startswith('!') and m.content!='!':
                if m.content==('!r'):
                    await m.channel.send('Restarting...',delete_after=cc.timeout)
                    os.execl(sys.executable, 'python3.6', __file__, *sys.argv[1:])
                elif m.content.startswith('!help') or m.content.startswith('!помощь'):
                    embed = discord.Embed(title="NoRecoilBot", description="List of commands are:",color=discord.Colour.dark_orange())
                    embed.add_field(name="!шар x y z | !ball [x;y;z]", value="Gives the random answer from given list", inline=False)
                    embed.add_field(name="!ролл x,y | !roll x,y", value="Gives the random int from A to B", inline=False)
                    embed.add_field(name="!помощь | !help", value="Gives this message", inline=False)
                    embed.add_field(name="### Admin commands ###", value="###Below is admin commands###", inline=False)
                    embed.add_field(name="!erase x | !erase all", value="Delete count of x or all messages from text channel", inline=False)
                    await m.channel.send(embed=embed)
                elif m.content.startswith('!erase'):
                    if m.channel.permissions_for(m.guild.me).manage_messages:
                        if m.channel.permissions_for(m.author).manage_messages:
                            if m.content.startswith('!erase all'):
                                async for message in m.channel.history():
                                    await message.delete()
                                await m.channel.send('Были удалены все сообщения',delete_after=cc.timeout)
                                # await m.channel.send('Команда отключена',delete_after=cc.timeout)
                            elif m.content.split(' ')[1].isdigit() and len(m.content.split(' '))==2:
                                ncount=int(m.content.split(' ')[1])+1
                                count=0
                                async for message in m.channel.history():
                                    await message.delete()
                                    count+=1
                                    if count==ncount:
                                        break
                                await m.channel.send('Было(и) удалено(ы) '+str(count-1)+' сообщений(я)',delete_after=cc.timeout)
                            else:
                                await m.delete()
                                await m.channel.send('Wrong use!',delete_after=cc.timeout)
                        else:
                            await m.delete()
                            await m.channel.send('Недостаточно прав!',delete_after=cc.timeout)
                    else:
                        await m.channel.send('I dont can manage messages in this channel!',delete_after=cc.timeout)
                elif m.content.startswith('!шар') or m.content.startswith('!ball'):
                    if len(m.content)==4:
                        if random.randint(0, 1) > 0:
                            await m.channel.send('Да')
                        else:
                            await m.channel.send('Нет')
                    elif cc.shar(m.content):
                        if cc.shar_list(m.content):
                            solve=m.content.split('[')[1].split(']')[0].split(';')
                            await m.channel.send(solve[random.randint(0,len(solve)-1)])
                        else:
                            await m.delete()
                            await m.channel.send('Wrong use:length of some variants =0!',delete_after=cc.timeout)
                    elif len(m.content.split(' '))>=3:#!s 1 2
                        solve=m.content.split(' ')
                        solve=solve[1:len(solve)]
                        await m.channel.send(str(solve[random.randint(0,len(solve)-1)]))
                    else:
                        await m.delete()
                        await m.channel.send('Wrong use!',delete_after=5)
                elif m.content.startswith('!ролл') or m.content.startswith('!roll'):
                    if (m.content.startswith('!ролл ') or m.content.startswith('!roll')) and m.content.find(',')  and len(m.content) >=8 and len(m.content.split(' ')[1].split(','))==2:
                        solve = m.content.split(' ')[1].split(',')
                        if solve[0].isdigit() and solve[1].isdigit():
                            await m.channel.send(random.randint(int(solve[0]),int(solve[1])))
                        else:
                            await m.delete()
                            await m.channel.send('Wrong use!', delete_after=cc.timeout)
                    else:
                        await m.delete()
                        await m.channel.send('Wrong use!', delete_after=cc.timeout)
                else:
                    await m.channel.send('\"!\" symbol in string start is allowed only for commands')
        except:
            await m.channel.send('Error excepted,restarting...')
            os.execl(sys.executable, 'python3.6', __file__, *sys.argv[1:])

bot = bot()
bot.run('NTcxMTA3NTQxODA3NzkyMTM4.XMJAyQ.l3gkY-zS_WSdO5r52DROgc5_vIA')