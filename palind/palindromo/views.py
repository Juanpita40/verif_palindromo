from urllib.parse import unquote
from django.shortcuts import render

def verificar_palindromo(request, palabra):
    palabra_decodificada = unquote(palabra)
    palabra_sin_espacios = ''.join(palabra_decodificada.split()).lower()
    es_palindromo = palabra_sin_espacios == palabra_sin_espacios[::-1]

    mensaje = "ES PALÍNDROMO" if es_palindromo else "NO ES PALÍNDROMO"

    return render(request, 'palindromo/plantilla.html', {
        'palabra': palabra_decodificada,
        'mensaje': mensaje,
    })

