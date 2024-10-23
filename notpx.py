import requests
import time
import random


print(Fore.YELLOW + "========================================")
print(Fore.CYAN + "AUTHOR : ANAM BACTIAR")
print(Fore.MAGENTA + "THANKS TO : ANAM BACTIAR!")
print(Fore.BLUE + "GITHUB: https://github.com/bactiar291")
print(Fore.GREEN + "BUY COFFEE FOR ME : 0x648dce97a403468dfc02c793c2b441193fccf77b ")
print(Fore.YELLOW + "========================================\n")



class NotPixelBot:
    def __init__(self, session_data):
        self.session_data = session_data
        self.base_url = "https://notpx.app/api/v1"
        
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'initData {self.session_data}',
        }
        
        self.display_initial_info()

    def display_initial_info(self):
        self.colored_print(f"✨ Initialized with headers: {self.headers}")
        self.colored_print("🎨 Bot is starting... Let's paint some pixels! 🖌️")

    def claim_mining(self):
        """Klaim mining setiap jam."""
        response = requests.get(f"{self.base_url}/mining/claim", headers=self.headers)
        if response.status_code == 200:
            self.colored_print("⛏️ Mining claimed successfully! 💎")
            return response.json()
        else:
            self.colored_print(f"❌ Error claiming mining: {response.status_code} - {response.text}")
            return None

    def get_pixels_data(self):
        """Mengambil data piksel dari server."""
        response = requests.get(f"{self.base_url}/pixels", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.colored_print(f"❌ Error fetching pixel data: {response.status_code} - {response.text}")
            return []

    def auto_paint_pixel(self):
        """Mewarnai pixel secara otomatis dengan warna acak."""
        pixels_data = self.get_pixels_data()

        if not pixels_data:
            self.colored_print("❌ No pixel data available. Skipping painting.")
            return

       
        pixels_to_paint = [pixel for pixel in pixels_data if pixel['color'] != '#000000']

        if not pixels_to_paint:
            self.colored_print("✅ All pixels are already painted!")
            return

       
        target_pixel = random.choice(pixels_to_paint)

       
        selected_color = f'#{random.randint(0, 0xFFFFFF):06x}'  
        data = {
            "pixelId": target_pixel['id'],
            "newColor": selected_color  
        }

        self.colored_print(f"🎨 Painting pixel with data: {data}")

        response = requests.post(f"{self.base_url}/repaint/start", headers=self.headers, json=data)
        if response.status_code == 200:
            self.colored_print(f"✅ Pixel painted successfully! ID: {target_pixel['id']}, Color: {data['newColor']}")
            return response.json()
        else:
            self.colored_print(f"❌ Error painting pixel: {response.status_code} - {response.text}")
            return None

    def colored_print(self, message):
        """Mencetak pesan dengan warna acak untuk setiap kata."""
        colors = [
            "\033[91m",  # Merah
            "\033[92m",  # Hijau
            "\033[93m",  # Kuning
            "\033[94m",  # Biru
            "\033[95m",  # Ungu
            "\033[96m",  # Cyan
        ]
        reset_color = "\033[0m"

        words = message.split()
        colored_message = ' '.join(f"{random.choice(colors)}{word}{reset_color}" for word in words)
        print(colored_message)

    def run(self):
        """Menjalankan bot secara terus-menerus."""
        while True:
           
            self.claim_mining()
            self.colored_print("⏳ Waiting for an hour before the next mining claim... ⛏️")
            time.sleep(5)  # Simulasi, gunakan 3600 untuk satu jam

            
            self.auto_paint_pixel()
            self.colored_print("⏳ Waiting for a random interval before the next painting... 🎨")
            time.sleep(random.randint(5, 6))  # Tunggu secara acak antara 5 sampai 6 detik

            
            self.colored_print("⏳ All tasks completed. Taking a break for 6 hours... 💤")
            time.sleep(21600)  # Jeda 6 jam (21600 detik)

if __name__ == "__main__":
   
    session_data = input("💻 Masukkan query_user Anda: ")

    bot = NotPixelBot(session_data)
    bot.run()
