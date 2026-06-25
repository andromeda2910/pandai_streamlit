import streamlit as st

# ==========================================================================
# 1. KONFIGURASI HALAMAN (Wajib di baris pertama setelah import)
# ==========================================================================
st.set_page_config(
    page_title="PANDAI - Belajar Jadi Pandai",
    page_icon="🐼",
    layout="wide",
    initial_sidebar_state="collapsed"  # Memaksa sidebar menutup di awal
)

# ==========================================================================
# 2. PEMANGGILAN SEPARATION OF CONCERNS (Membaca CSS dari luar)
# ==========================================================================
with open("style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ==========================================================================
# 3. HERO SECTION & HEADER
# ==========================================================================
st.markdown('<p class="hero-title">PANDAI</p>', unsafe_allow_html=True)

# Tambahkan baris kepanjangan ini di bawah judul utama
st.markdown('<p class="hero-tagline">Platform AI Non-Internet Daerah Anak Indonesia</p>', unsafe_allow_html=True)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="hero-subtitle">
        <h2>Belajar Jadi Pandai 🧠</h2>
        <p>Dengan atau tanpa internet, PANDAI siap bantu anak Indonesia belajar!</p>
    </div>
""", unsafe_allow_html=True)


# ==========================================================================
# 4. MASKOT & BOX SAMBUTAN
# ==========================================================================
st.markdown("""
    <div class="welcome-box">
        <div style='display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap;'>
            <span style='font-size: 45px;'>🐼</span>
            <div style='text-align: left;'>
                <p style='font-weight: 700; color: #1f2937; margin: 0; font-size: 18px;'>Halo! Aku PANDAI!</p>
                <p style='color: #4b5563; margin: 0; font-size: 14px;'>Siap jadi teman setia kamu belajar bareng AI!</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ==========================================================================
# 5. TOMBOL NAVIGASI UTAMA (Mode Siswa & Mode Guru)
# ==========================================================================
col_nav1, col_nav2 = st.columns(2)

with col_nav1:
    btn_siswa = st.button(
        "📘 Ayo Belajar! (Mode Siswa)", 
        use_container_width=True, 
        key="to_siswa",
        type="primary" 
    )
    if btn_siswa:
        st.switch_page("pages/1_Siswa.py")  # Mengarah ke nama file berindeks secara utuh

with col_nav2:
    btn_guru = st.button(
        "👨‍🏫 Untuk Guru (Mode RPP & Kuis)", 
        use_container_width=True, 
        key="to_guru"
    )
    if btn_guru:
        st.switch_page("pages/2_Guru.py")   # Mengarah ke nama file berindeks secara utuh

st.markdown("<br><hr>", unsafe_allow_html=True)


# ==========================================================================
# 6. KEUNGGULAN ARSITEKTUR PANDAI
# ==========================================================================
st.markdown("### ✨ Keunggulan Arsitektur PANDAI")
st.markdown("<p style='color: #6b7280; font-size: 14px; margin-top:-10px;'>Kenapa sistem ini relevan untuk menyelesaikan masalah di daerah 3T?</p>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""
        <div class="feature-card">
            <div>
                <p style='font-size: 20px; margin: 0;'>📊</p>
                <h4>Simulasi Arsitektur Edge AI</h4>
                <p>Saat ini sistem berjalan menggunakan Gemini API untuk simulasi dan uji coba fitur. Tapi secara arsitektur, kodenya sudah dirancang modular agar ke depannya bisa langsung beralih 100% ke model lokal (tanpa internet) saat dipasang di server sekolah.</p>
            </div>
            <span class="badge-tag" style="background: #e0f2fe; color: #0369a1;">Kemandirian Infrastruktur</span>
        </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <div class="feature-card">
            <div>
                <p style='font-size: 20px; margin: 0;'>💬</p>
                <h4>Bahasa Ramah Anak</h4>
                <p>Cara AI menjawab sudah dikunci pakai instruksi khusus (prompting) supaya penyampaiannya selalu sederhana, ramah, dan memakai analogi yang mudah dipahami oleh anak-anak.</p>
            </div>
            <span class="badge-tag" style="background: #ecfdf5; color: #047857;">Kurikulum Terpadu</span>
        </div>
    """, unsafe_allow_html=True)

with col_f3:
    st.markdown("""
        <div class="feature-card">
            <div>
                <p style='font-size: 20px; margin: 0;'>🤖</p>
                <h4>Asisten Pintar Guru</h4>
                <p>Dirancang untuk membantu guru di sekolah terpencil dalam menyiapkan materi, rangkuman, atau bikin bank soal instan secara cepat, jadi waktu guru tidak habis untuk urusan administrasi yang kaku.</p>
            </div>
            <span class="badge-tag" style="background: #fef3c7; color: #b45309;">Solusi Krisis Guru</span>
        </div>
    """, unsafe_allow_html=True)


# ==========================================================================
# 7. METRIK & COMMITMENT (SDGs)
# ==========================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Metrik & Dampak Sosial")

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.info("**Aksesibilitas Ilmu**\n\nBelajar dengan mudah\n\n🟢 Bebas Akses")
with col_m2:
    st.success("**Efisiensi Waktu Guru**\n\nEfisiensi Kerja Guru\n\n🟢 Rencana Ajar Otomatis")
with col_m3:
    st.warning("**Target Siswa**\n\nMandiri & Aktif\n\n🟢 Pemeratakan Pendidikan")

# SDGs Box dengan Link Edukasi Tambahan
st.markdown("""
    <div class="sdgs-box">
        <p class="sdgs-title">🎯 Komitmen SDGs (Sustainable Development Goals)</p>
        <p class="sdgs-text">
            PANDAI diciptakan bukan sekadar sebagai aplikasi, melainkan sebuah solusi nyata untuk menjawab tantangan SDGs Poin 4 (Pendidikan Berkualitas) dan Poin 10 (Mengurangi Kesenjangan) di beranda terdepan Indonesia. Tujuan utama aplikasi ini adalah memastikan bahwa keterbatasan jumlah guru, minimnya buku paket, dan hilangnya sinyal internet tidak boleh menjadi alasan anak-anak di daerah pelosok tertinggal secara ilmu. Kami ingin meruntuhkan sekat pembatas itu, agar setiap siswa di sekolah terpencil memiliki hak, fasilitas, dan kesempatan belajar yang sama cerdasnya dengan anak-anak di kota besar.
        </p>
        <div style="margin-top: 15px; padding-top: 10px; border-top: 1px dashed #bbf7d0; font-size: 13px;">
            <span style="color: #166534; font-weight: 600;">🔗 Pelajari Selengkapnya:</span> 
            <a href="https://sdgs.bappenas.go.id/metadata-indikator-sdgs/" target="_blank" style="color: #2563eb; text-decoration: underline; font-weight: 500; margin-right: 15px;">Metadata Indikator SDGs Poin 4 (Pendidikan Berkualitas) & Poin 10 (Mengurangi Kesenjangan)</a>
            
    </div>
""", unsafe_allow_html=True)


# ==========================================================================
# 8. FOOTER
# ==========================================================================
st.markdown("""
    <div class="custom-footer">
        🐼 PANDAI - Platform AI Non-Internet Daerah Anak Indonesia • Final Project • © 2026
    </div>
""", unsafe_allow_html=True)