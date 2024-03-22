import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'¡Hola, soy un bot que te da recomendaciónes sobre como ayudar el medio ambiente, {bot.user}!')

@bot.command()
async def ayuda(ctx):
    await ctx.send(f'intenta usar $tips')

@bot.command()
async def tips(ctx):
    elements = "qwertyuiop"
    random.choice(elements)
    dictionary = {
    "q": "Deposita los residuos en el contenedor correspondiente: Esta acción facilita que los residuos se incorporen antes a la cadena de reciclaje. Localiza la zona de contenedores más cercana a tu vivienda para hacer más fácil el proceso. Una vez separados, debes dejar los envases de plástico, latas y bricks en el contenedor amarillo; los papeles y cartones en el contenedor azul; y el vidrio en el contenedor verde. Para los residuos orgánicos, el contenedor marrón es el correcto, y para aquellos materiales con mezcla de residuos orgánicos como pueden ser pañales, algodones, etc., los contenedores grises son los adecuados.",
    "w": "Aprende qué hacer con los residuos especiales: Los residuos especiales como aparatos electrónicos o muebles se depositan en los puntos limpios. Las pilas y el aceite de cocina tienen sus contenedores específicos. Lo mismo ocurre con los medicamentos, que no puedes tirar a la basura por su toxicidad y que debes dejar en uno de los puntos SIGRE situados en algunas farmacias.",
    "e": "Recicla el aceite de cocina: Uno de los problemas habituales al reciclar en casa es qué hacer con el aceite usado. Este residuo debe depositarse en un contenedor especial y nunca tirarse por el inodoro o por la pila de la cocina. Un consejo para reciclar este aceite es almacenarlos en botes de vidrio que, una vez llenos, llevaremos a un punto de recogida.",
    "r": "Limpia los envases de comida antes de tirarlos al contenedor: Otro consejo básico es limpiar los envases de comida como latas o botes antes de llevarlos al contenedor. En el caso de las botellas de aceite o los envases de productos cosméticos y de limpieza no deben enjuagarse antes de su reciclaje para evitar vertidos químicos o tóxicos en el agua.",
    "t": "Reduce el tamaño de botellas y bricks: Reciclar supone acumular envases temporalmente. Un truco para optimizar nuestros espacios de almacenaje es «aplastar» los bricks y las botellas de plástico, o meter las latas de metal unas dentro de otras, según su tamaño, para reducir el riesgo de cortes.",
    "y": "Involucra a toda tu familia y entorno en tu plan de reciclaje: Para que el reciclaje en casa sea efectivo todos los miembros de la familia, incluso los más pequeños, deben ser partícipes activos. Un consejo para concienciarse al máximo es exportar estos hábitos de reciclaje a otros ámbitos de tu vida como por ejemplo el trabajo.",
    "u": "Reciclar y reutilizar van de la mano: No se trata únicamente de clasificar los residuos del hogar y llevarlos a su contenedor, sino también de adoptar hábitos para reutilizar materiales y fomentar el consumo responsable. Un ejemplo es llevar nuestras propias bolsas de tela o rejilla para hacer la compra. Otro, usar los botes de cristal de conservas para guardar pasta, especias, cereales o legumbres. Reciclar y reutilizar van de la mano  No se trata únicamente de clasificar los residuos del hogar y llevarlos a su contenedor, sino también de adoptar hábitos para reutilizar materiales y fomentar el consumo responsable. Un ejemplo es llevar nuestras propias bolsas de tela o rejilla para hacer la compra. Otro, usar los botes de cristal de conservas para guardar pasta, especias, cereales o legumbres.",
    "i": "Lee las etiquetas y envases: La información sobre reciclaje disponible en etiquetas y envases es muy útil en los plásticos, que tienen un código especial que indica el material o mezcla de materiales utilizados en su fabricación. En algunos casos, la etiqueta también nos indica en qué contenedor debemos depositar un envase.",
    "o": "Separa los residuos en recipientes independientes: El primer paso para reciclar en casa es disponer de recipientes independientes para cada tipo de residuo. Esta acción es sencilla y facilita mucho la clasificación, aunque requiere espacio, un solo cubo con separadores es suficiente."
            }
    word = random.choice(elements)
    await ctx.send(dictionary[word])

bot.run()
