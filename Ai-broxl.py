import streamlit as st
import urllib.parse

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Asisten AI Mobile", page_icon="📱", layout="centered")

st.title("📱 ASISTEN AI (VERSI STREAMLIT)")
st.write("Gunakan fitur di bawah untuk membuka aplikasi atau melakukan pencarian.")

# 2. Input dari User
perintah = st.text_input("Ketik perintah kamu di sini (contoh: 'buka roblox' atau 'cari baju baru'):")
perintah = perintah.lower().strip()

# 3. Logika Proses Perintah (Menggunakan Struktur yang Aman)
if perintah:
    # --- Kelompok Buka Aplikasi (Deep Link) ---
    if "roblox" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka Roblox!")
        st.link_button("🎮 Buka Aplikasi Roblox", "roblox://")

    elif "whatsapp" in perintah or "wa" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka WhatsApp!")
        st.link_button("💬 Buka WhatsApp", "whatsapp://")

    elif "youtube" in perintah or "yt" in perintah and not perintah.startswith("cari video "):
        st.success("Silakan klik tombol di bawah untuk membuka YouTube!")
        st.link_button("📺 Buka YouTube", "https://youtube.com")

    elif "instagram" in perintah or "ig" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka Instagram!")
        st.link_button("📸 Buka Instagram", "instagram://")

    elif "facebook" in perintah or "fb" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka Facebook!")
        st.link_button("🔵 Buka Facebook", "fb://")

    elif "spotify" in perintah or "musik" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka Spotify!")
        st.link_button("🎵 Buka Spotify", "spotify://")

    # --- Kelompok Fitur Pencarian ---
    elif perintah.startswith("cari video "):
        video = perintah.replace("cari video ", "").strip()
        if video:
            query_encoded = urllib.parse.quote(video)
            url_yt = f"https://youtube.com/results?search_query={query_encoded}"
            st.success(f"Hasil pencarian untuk video: '{video}'")
            st.link_button(f"📺 Tonton '{video}' di YouTube", url_yt)
        else:
            st.warning("Mau cari video apa, bro?")

    elif perintah.startswith("pengen cari ") or perintah.startswith("cari "):
        cari = perintah.replace("pengen cari ", "").replace("cari ", "").strip()
        if cari:
            query_encoded = urllib.parse.quote(cari)
            url_google = f"https://google.com{query_encoded}"
            st.success(f"Tombol pencarian Google untuk: '{cari}'")
            st.link_button(f"🔍 Cari '{cari}' di Google", url_google)
        else:
            st.warning("Mau cari apa di Google?")

    # --- Kelompok Hitung-hitungan ---
    elif perintah.startswith("hitung "):
        soal = perintah.replace("hitung ", "").strip()
        soal = soal.replace("×", "*").replace("x", "*").replace("X", "*").replace(":", "/")
        try:
            hasil = eval(soal, {"__builtins__": None}, {})
            st.metric(label=f"Hasil dari {soal}", value=hasil)
        except Exception:
            st.error("Perhitungan tidak valid, bro. Contoh: hitung 5*5")

    # --- Kelompok Tanya Jawab Tokoh ---
    elif "einstein" in perintah:
        st.info("💡 Albert Einstein adalah fisikawan terkenal yang mengembangkan Teori Relativitas.")
    elif "ronaldo" in perintah:
        st.info("⚽ Cristiano Ronaldo adalah salah satu pemain sepak bola terbaik asal Portugal.")
    elif "messi" in perintah:
        st.info("⚽ Lionel Messi adalah salah satu pemain sepak bola terbaik asal Argentina.")

    # --- Jika Perintah Tidak Dikenal ---
    else:
        st.warning("AI tidak mengerti perintah itu. Coba ketik 'buka roblox' atau 'cari sepatu baru'.")

    elif "spotify" in perintah or "musik" in perintah:
        st.success("Silakan klik tombol di bawah untuk membuka Spotify!")
        st.link_button("🎵 Buka Spotify", "spotify://")

    # 🔍 FITUR SEARCH VIDEO YOUTUBE
    elif perintah.startswith("cari video "):
        video = perintah.replace("cari video ", "").strip()
        if video:
            query_encoded = urllib.parse.quote(video)
            url_yt = f"https://youtube.com/results?search_query={query_encoded}"
            st.success(f"Hasil pencarian untuk video: '{video}'")
            st.link_button(f"📺 Tonton '{video}' di YouTube", url_yt)

    # 🔍 FITUR GOOGLE SEARCH
    elif perintah.startswith("pengen cari ") or perintah.startswith("cari "):
        # Mengambil keyword pencarian
        cari = perintah.replace("pengen cari ", "").replace("cari ", "").strip()
        if cari:
            query_encoded = urllib.parse.quote(cari)
            url_google = f"https://google.com{query_encoded}"
            st.success(f"Tombol pencarian Google untuk: '{cari}'")
            st.link_button(f"🔍 Cari '{cari}' di Google", url_google)

    # 🧮 FITUR HITUNG / KALKULATOR CEPAT
    elif perintah.startswith("hitung "):
        soal = perintah.replace("hitung ", "").strip()
        soal = soal.replace("×", "*").replace("x", "*").replace("X", "*").replace(":", "/")
        try:
            # Evaluasi matematika sederhana yang aman di Streamlit
            hasil = eval(soal, {"__builtins__": None}, {})
            st.metric(label=f"Hasil dari {soal}", value=hasil)
        except Exception:
            st.error("Perhitungan tidak valid, bro. Coba angka biasa (misal: hitung 5*5)")

    # 📚 TANYA JAWAB TOKOH
    elif "einstein" in perintah:
        st.info("💡 Albert Einstein adalah fisikawan terkenal yang mengembangkan Teori Relativitas.")
    elif "ronaldo" in perintah:
        st.info("⚽ Cristiano Ronaldo adalah salah satu pemain sepak bola terbaik asal Portugal.")
    elif "messi" in perintah:
        st.info("⚽ Lionel Messi adalah salah satu pemain sepak bola terbaik asal Argentina.")

    else:
        st.warning("AI tidak mengerti perintah itu. Coba ketik 'buka roblox' atau 'cari sepedah baru'.")

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
