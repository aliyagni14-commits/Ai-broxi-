import os
import urllib.parse
import re

print("=== ASISTEN AI AKTIF (VERSI BUKA APLIKASI) ===")
print("Ketik 'keluar' untuk menghentikan program.\n")

while True:
    perintah = input("User: ").lower().strip()

    if perintah == "keluar":
        print("AI: Sampai jumpa!")
        break

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
        # Karena ChatGPT versi aplikasi sering berbeda, ini dibuka lewat browser bawaan HP
        print("AI: Membuka ChatGPT...")
        os.system("am start -a android.intent.action.VIEW -d 'https://chatgpt.com'")

    # 🔍 FITUR GOOGLE SEARCH
    elif perintah.startswith("pengen cari "):
        cari = perintah.replace("pengen cari ", "").strip()
        if cari:
            query_encoded = urllib.parse.quote(cari)
            print(f"AI: Mencari '{cari}' di Google...")
            os.system(f"am start -a android.intent.action.VIEW -d 'https://google.com{query_encoded}'")
        else:
            print("AI: Mau cari apa? Sebutkan keyword-nya.")

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
        print("AI: Maaf, saya tidak mengerti perintah tersebut.")
