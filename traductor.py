
from translate import Translator 

translator = Translator(from_lang= 'spanish', to_lang= 'english')

txt = input('Que quieres traducir? ')

res = translator.translate(txt)

print(res)
