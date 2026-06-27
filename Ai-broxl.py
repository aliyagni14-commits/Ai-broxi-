import os
import urllib.parse
import re
from datetime import datetime

print("=== ASISTEN AI AKTIF (VERSI UPDATE MAXIMAL) ===")
print("Ketik 'keluar' untuk menghentikan program.\n")

while True:
    perintah = input("User: ").lower().strip()

    if perintah == "keluar":
        print("AI: Sampai jumpa, bro!")
        break

    # 🎮 BARU: FITUR GAME & HIBURAN
    elif perintah == "buka roblox":
        print("AI: Membuka Roblox... Selamat mabar!")
        os.system("am start -n com.roblox.client/com.roblox.client.ActivitySplash")

    elif perintah == "buka tiktok":
        print("AI: Membuka TikTok...")
        os.system("am start -n com.zhiliaoapp.musically/com.ss.android.ugc.aweme.splash.SplashActivity")

    elif perintah in ["buka spotify", "buka musik"]:
        print("AI: Membuka Spotify... Enjoy musiknya!")
        os.system("am start -n com.spotify.music/com.spotify.music.MainActivity")

    # 📱 FITUR UTAMA: MEMBUKA APLIKASI DI HP
    elif perintah == "buka whatsapp":
        print("AI: Membuka WhatsApp...")
        os.system("am start -n com.whatsapp/com.whatsapp.Main")

    elif perintah in ["buka youtube", "buka yt"]:
        print("AI: Membuka YouTube...")
        os.system("am start -n com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")

    elif perintah == "buka instagram":
        print("AI: Membuka Instagram...")
        os.system("am start -n com.instagram.android/com.instagram.android.activity.MainTabActivity")

    elif perintah == "buka facebook":
        print("AI: Membuka Facebook...")
        os.system("am start -n com.facebook.katana/com.facebook.katana.LoginActivity")

    elif perintah == "buka chatgpt":
        print("AI: Membuka ChatGPT...")
        os.system("am start -a android.intent.action.VIEW -d 'https://chatgpt.com'")

    # 🔍 BARU: CARI VIDEO DI YOUTUBE
    elif perintah.startswith("cari video "):
        video = perintah.replace("cari video ", "").strip()
        if video:
            query_encoded = urllib.parse.quote(video)
            print(f"AI: Mencari video '{video}' di YouTube...")
            os.system(f"am start -a android.intent.action.VIEW -d 'https://youtube.com{query_encoded}'")
        else:
            print("AI: Mau cari video apa di YouTube?")

    # 🔍 FITUR GOOGLE SEARCH (FIXED BUG)
    elif perintah.startswith("pengen cari "):
        cari = perintah.replace("pengen cari ", "").strip()
        if cari:
            query_encoded = urllib.parse.quote(cari)
            print(f"AI: Mencari '{cari}' di Google...")
            # Ditambahkan /search?q= agar link Google berfungsi dengan benar
            os.system(f"am start -a android.intent.action.VIEW -d 'https://google.com{query_encoded}'")
        else:
            print("AI: Mau cari apa? Sebutkan keyword-nya.")

    # ⏰ BARU: FITUR WAKTU & TANGGAL
    elif perintah in ["jam berapa", "pukul berapa", "waktu sekarang"]:
        sekarang = datetime.now().strftime("%H:%M:%S")
        print(f"AI: Sekarang jam {sekarang} WIB.")

    elif perintah in ["hari ini hari apa", "tanggal berapa"]:
        hari_ini = datetime.now().strftime("%A, %d %B %Y")
        print(f"AI: Hari ini adalah {hari_ini}.")

    # 📚 FITUR TANYA JAWAB TOKOH
    elif perintah in ["siapa albert einstein", "siapa einstein"]:
        print("AI: Albert Einstein adalah fisikawan terkenal yang mengembangkan Teori Relativitas.")

    elif perintah in ["siapa ronaldo", "siapa cristiano ronaldo"]:
        print("AI: Cristiano Ronaldo adalah salah satu pemain sepak bola terbaik asal Portugal.")

    elif perintah in ["siapa messi", "siapa lionel messi"]:
        print("AI: Lionel Messi adalah salah satu pemain sepak bola terbaik asal Argentina.")

    elif perintah == "berapa 1+1":
        print("AI: 2")

    # 🧮 FITUR KALKULATOR
    elif perintah.startswith("hitung "):
        try:
            soal = perintah.replace("hitung ", "").strip()
            soal = soal.replace("×", "*").replace("x", "*").replace("X", "*")
            soal = soal.replace("÷", "/").replace(":", "/")
            soal = soal.replace("^", "**")

            if not re.match(r'^[\d+\-*/\s.()]*$', soal):
                raise ValueError("Karakter tidak diizinkan")

            hasil = eval(soal)
            if isinstance(hasil, float) and hasil.is_integer():
                hasil = int(hasil)
            print("AI: Hasilnya =", hasil)
        except ZeroDivisionError:
            print("AI: Error! Tidak bisa membagi angka dengan nol.")
        except Exception:
            print("AI: Perhitungan tidak valid.")

    else:
        print("AI: Maaf, saya tidak mengerti perintah tersebut. Coba ketik 'buka roblox' atau 'jam berapa'.")
