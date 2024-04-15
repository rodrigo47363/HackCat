import os
import discord
from discord.ext import commands
import aiosqlite

# Configuración del bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')

# Constantes y variables globales
TOKEN = 'tu_token_de_discord'
DB_NAME = 'niveles.db'
IMG_FOLDER = 'imagenes'
ECONOMY_FOLDER = 'economia'

# Manejo de eventos
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

    # Conexión a la base de datos
    bot.db = await aiosqlite.connect(DB_NAME)
    await initialize_database(bot.db)

    # Actividad del bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="PornHub"))

# Comandos de bienvenida
@bot.event
async def on_member_join(member):
    # Asignar roles al nuevo miembro
    roles = [
        discord.utils.get(member.guild.roles, id=1012189850167943209),  # rolMiembros
        discord.utils.get(member.guild.roles, id=1017258189739270224),  # rolNiveles
        discord.utils.get(member.guild.roles, id=1017258625468743701),  # rolEco
        discord.utils.get(member.guild.roles, id=1017258787192717392)   # rolAuto
    ]
    await member.add_roles(*roles)

    # Enviar mensaje de bienvenida con imagen
    welcome_channel = member.guild.system_channel
    if welcome_channel:
        await welcome_channel.send(f'Bienvenido {member.mention}, espero que lo pases bien!')
        await send_welcome_image(welcome_channel, 'bienvenida.gif')

# Inicialización de la base de datos
async def initialize_database(db):
    async with db.execute('CREATE TABLE IF NOT EXISTS nivel (nivel INTEGER, xp INTEGER, usuario INTEGER, guild INTEGER)'):
        pass

# Envío de imagen de bienvenida
async def send_welcome_image(channel, image_name):
    image_path = os.path.join(IMG_FOLDER, image_name)
    if os.path.exists(image_path):
        file = discord.File(image_path)
        await channel.send(file=file)

# Comando de nivel
@bot.command(name='nivel')
async def nivel(ctx, member: discord.Member = None):
    member = member or ctx.author
    xp, nivel = await get_user_level(ctx.guild.id, member.id)
    await ctx.send(f'{member.display_name} está en el nivel {nivel} con {xp} puntos de experiencia.')

# Obtener nivel y experiencia de usuario
async def get_user_level(guild_id, user_id):
    async with bot.db.execute('SELECT xp, nivel FROM nivel WHERE usuario = ? AND guild = ?', (user_id, guild_id)) as cursor:
        row = await cursor.fetchone()
        return row[0] if row else 0, row[1] if row else 0

# Comando de ingreso de dinero
@bot.command(name='ingresar')
@commands.has_permissions(manage_roles=True)
async def ingresar(ctx, member: discord.Member, cantidad: int):
    await update_economy_balance(member.id, cantidad)
    await ctx.send(f'Se han ingresado {cantidad} monedas a la cuenta de {member.display_name}.')

# Actualizar balance de economía de usuario
async def update_economy_balance(user_id, amount):
    async with bot.db.execute('SELECT balance FROM economia WHERE usuario = ?', (user_id,)) as cursor:
        row = await cursor.fetchone()
        current_balance = row[0] if row else 0
    new_balance = current_balance + amount
    await bot.db.execute('INSERT INTO economia (usuario, balance) VALUES (?, ?) ON CONFLICT(usuario) DO UPDATE SET balance = ?', (user_id, new_balance, new_balance))
    await bot.db.commit()

# Manejo de errores
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando no encontrado. Usa >help para ver la lista de comandos disponibles.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('No tienes los permisos necesarios para ejecutar este comando.')

# Ejecutar el bot
bot.run(TOKEN)
