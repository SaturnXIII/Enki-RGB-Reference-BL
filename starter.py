import asyncio
from bleak import BleakClient

# Adresse MAC de l'appareil de destination
DEVICE_ADDRESS = "YOUR_DEVICE_ADDRESS"

# UUID de la caractéristique
CHARACTERISTIC_UUID = "0000a101-1115-1000-0001-617573746f6d"

# Nouvelle valeur à tester
VALUE = bytes.fromhex("YOUR_VALUE_HERE")

async def send_bluetooth_command():
    async with BleakClient(DEVICE_ADDRESS) as client:
        if not client.is_connected:
            print("Impossible de se connecter à l'appareil.")
            return

        print(f"Connecté à l'appareil: {DEVICE_ADDRESS}")

        # Envoyer la commande Write Request
        await client.write_gatt_char(CHARACTERISTIC_UUID, VALUE, response=True)
        print(f"Commande envoyée avec succès: UUID {CHARACTERISTIC_UUID}, Valeur {VALUE.hex()}")

# Exécuter le script
asyncio.run(send_bluetooth_command())