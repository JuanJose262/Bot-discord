import discord
import random
from discord.ext import commands

# Activar permisos para leer mensajes
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

FRASES = [
    "Paso a paso también se avanza.",
    "Que funcione primero, que quede bonito después.",
    "Un bug resuelto es un aprendizaje ganado.",
    "Hoy es buen día para terminar lo que empezaste.",
]


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# Comando !hola
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Soy tu bot de Discord y estoy funcionando.")


# Comando !ayuda
@bot.command()
async def ayuda(ctx):
    mensaje = (
        "**Comandos disponibles:**\n"
        "`!hola` - Te saludo\n"
        "`!ayuda` - Muestro esta lista\n"
        "`!dado` - Tiro un dado del 1 al 6\n"
        "`!moneda` - Lanzo una moneda (Cara o Cruz)\n"
        "`!repetir <mensaje>` - Repito lo que me digas"
        "`!info` - Muestra info del servidor\n"
        "`!frase` - Te doy una frase motivadora\n"
        "`!elegir a, b, c` - Elijo una opción al azar\n"
        "`!contar <texto>` - Cuenta palabras y letras"
    )
    await ctx.send(mensaje)


@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f" Salió el número **{numero}**.")


@bot.command()
async def moneda(ctx):
    resultado = random.choice(["Cara", "Cruz"])
    await ctx.send(f" Cayó **{resultado}**.")


@bot.command()
async def repetir(ctx, *, texto: str = None):
    if not texto:
        await ctx.send("Escribe algo después de `!repetir`, por ejemplo: `!repetir hola mundo`")
        return
    await ctx.send(texto)


@bot.command()
async def info(ctx):
    if ctx.guild is None:
        await ctx.send("Este comando funciona mejor dentro de un servidor.")
        return
    await ctx.send(
        f" **Servidor:** {ctx.guild.name}\n"
        f" **Miembros:** {ctx.guild.member_count}"
    )


@bot.command()
async def frase(ctx):
    await ctx.send(f"💬 *\"{random.choice(FRASES)}\"*")


@bot.command()
async def elegir(ctx, *, opciones: str = None):
    if not opciones:
        await ctx.send("Escribe opciones separadas por coma. Ejemplo: `!elegir pizza, tacos, hamburguesa`")
        return
    lista = [op.strip() for op in opciones.split(",") if op.strip()]
    if len(lista) < 2:
        await ctx.send("Pon al menos **dos** opciones separadas por coma.")
        return
    await ctx.send(f"🎯 Elijo: **{random.choice(lista)}**")


@bot.command()
async def contar(ctx, *, texto: str = None):
    if not texto:
        await ctx.send("Escribe un texto después de `!contar`, por ejemplo: `!contar hola como estas`")
        return
    palabras = len(texto.split())
    caracteres = len(texto)
    await ctx.send(f"🔢 **Palabras:** {palabras} | **Caracteres:** {caracteres}")


# Manejo de comandos que no existen
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ese comando no existe. Escribe `!ayuda` para ver los disponibles.")


bot.run("TU_TOKEN_DE_DISCORD_AQUI")
