from config import CITY, POSTAL_CODE, PROPERTY_TYPE, MAX_PRICE

def main():
    print(f"Système de veille immobilière démarré")
    print(f"Recherche : {PROPERTY_TYPE} à {CITY} ({POSTAL_CODE})")
    print(f"Budget maximum : {MAX_PRICE} €")

if __name__ == "__main__":
    main()
