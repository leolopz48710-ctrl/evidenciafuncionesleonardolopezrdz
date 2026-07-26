def main():
    contador = 0
    while True:
        try:
            entrada = input("Palabra o número (espacio termina): ")
            if entrada == " ":
                break
            if entrada.isdigit():
                entrada = str(entrada)
            print(entrada.upper())
            contador += 1
        except Exception as e:
            print(f"Error:", e)
    print("Programa terminado")
    print("Cantidad de palabras procesadas:", contador)

main()