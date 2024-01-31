import sys

if len(sys.argv) != 3:
    print("Uso: python suma.py <numero1> <numero2>")
    sys.exit(1)

try:
    resultado = float(sys.argv[1]) + float(sys.argv[2])
    print(f"La suma es: {resultado}")
except ValueError:
    print("Los argumentos deben ser números válidos.")
    sys.exit(1)
