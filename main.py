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

lara = 123456789012345678  # Substitua pelo ID real do usuário

@bot.event
async def on_member_update(before, after):
    # Defina o horário formatado
    hora = datetime.datetime.utcnow().strftime(f'Data: %d/%m/%Y Hora: %H:%M:%S %p')

    # Pegue o usuário e o canal de aviso
    lr = bot.get_user(lara)
    aviso = bot.get_channel(772915130995441744)  # Canal onde as mensagens serão enviadas

    # Verifique se é o usuário correto e se houve alteração para offline
    if after.id == lara:
        if str(after.status) == 'offline' and str(before.status) != 'offline':
            await aviso.purge(limit=10)
            embed = disnake.Embed(
                title=f'🔰 {lr.display_name} Status',
                description=f'🔴 {lr.display_name} está offline!'
            )
            embed.timestamp = datetime.datetime.utcnow()
            await aviso.send(embed=embed)
            with open('logs.txt', 'a') as ls:
                ls.write(f'{lr} > offline > {hora}\n')

        # Verifique se houve alteração para online
        elif str(after.status) == 'online' and str(before.status) == 'offline':
            await aviso.purge(limit=10)
            embed = disnake.Embed(
                title=f'🔰 {lr.display_name} Status',
                description=f'🟢 {lr.display_name} está online!'
            )
            embed.timestamp = datetime.datetime.utcnow()
            await aviso.send(embed=embed)
            with open('logs.txt', 'a') as ls:
                ls.write(f'{lr} > online > {hora}\n')

bot.run(token)
