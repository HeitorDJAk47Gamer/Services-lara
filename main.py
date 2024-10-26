import disnake, datetime, json, random, asyncio
from disnake.ext import commands, tasks


with open('config.json') as e:
  infos = json.load(e)
  token = infos['token']
  prefixo = infos['prefix']
  lara = infos['lara']
  heitor = infos['heitor']

bot = commands.Bot(command_prefix=prefixo, case_insensitive=True, intents=disnake.Intents.all())

@bot.event
async def on_ready():
  calc = bot.latency * 1000
  pong = round(calc)

  print(f'Nome: {bot.user}  ID: {bot.user.id}')
  print(f'Membros Globais: {len(bot.users)}')
  print(f'Ping {pong} ms')
  #await bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.listening, name=f''))

@bot.event
async def on_member_update(before, after):
  hora = datetime.datetime.utcnow().strftime(f'Data: %d/%m/%Y Hora: %H:%M:%S %p')
  lr = bot.get_user(lara)
  aviso = bot.get_channel(772915130995441744)
  if str(after.status) == 'offline' and after.id == lara:
    await aviso.purge(limit=10)
    x = disnake.Embed(title=f'🔰 {lr.display_name} Status', description=f'🔴 {lr.display_name} está  offline!')
    x.timestamp = datetime.datetime.utcnow()
    await aviso.send(embed=x)
    with open('logs.txt', 'a') as ls:
      ls.write(f'{lr} > offline > {hora}\n')
    ls.close()
  if str(before.status) == "offline" and after.id == lara:
    if str(after.status) == "online" and after.id == lara:
      await aviso.purge(limit=10)
      x = disnake.Embed(title=f'🔰 {lr.display_name} Status', description=f'🟢 {lr.display_name} está  online!')
      x.timestamp = datetime.datetime.utcnow()
      await aviso.send(embed=x)
      with open('logs.txt', 'a') as ls:
        ls.write(f'{lr} > online > {hora}\n')
      ls.close()

bot.run(token)
