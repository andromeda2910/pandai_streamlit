import streamlit as st
from google import genai
import os
import json
import base64
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =================================================
# 1. KONFIGURASI HALAMAN
# =================================================
st.set_page_config(
    page_title="PANDAI - Belajar",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# =================================================
# 2. HEADER & HOME BUTTON
# =================================================

# Home button at top
col_home1, col_home2, col_home3 = st.columns([1, 2, 1])
with col_home2:
    if st.button("🏠 Kembali ke Beranda", use_container_width=True, key="siswa_home"):
        st.switch_page("app.py")

st.markdown('<p class="hero-title"><span class="hero-icon">📖</span> Belajar</p>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# SD-only notice
st.markdown("""
    <div style='background: #FEF3C7; padding: 15px; border-radius: 12px; border-left: 4px solid #F59E0B; margin: 20px 0;'>
        <p style='color: #92400E; font-weight: 600; margin: 0;'>📚 Perhatian: Saat ini materi tersedia untuk jenjang SD (Kelas 1-6). Jenjang lain menyusul.</p>
    </div>
""", unsafe_allow_html=True)

# =================================================
# 4. SELECTOR KELAS & MAPEL
# =================================================
st.markdown("## 🎯 Pilih Materi Belajar")

col1, col2 = st.columns([1, 1])

with col1:
    kelas = st.selectbox(
        "📚 Kelas",
        ["Kelas 1 SD", "Kelas 2 SD", "Kelas 3 SD", "Kelas 4 SD", "Kelas 5 SD", "Kelas 6 SD"],
        index=3
    )

with col2:
    mapel = st.selectbox(
        "📖 Mata Pelajaran",
        ["Matematika", "IPA", "Bahasa Indonesia", "IPS", "PKn"],
        index=0
    )

st.divider()

# =================================================
# 5. MATERI DISPLAY
# =================================================
st.markdown(f"## 📚 Materi {mapel} - {kelas}")

# Load materi dari JSON file
try:
    with open("materi.json", "r", encoding="utf-8") as f:
        materi_data = json.load(f)
except FileNotFoundError:
    st.error("❌ File materi.json tidak ditemukan!")
    materi_data = {}
except json.JSONDecodeError:
    st.error("❌ File materi.json tidak valid!")
    materi_data = {}

# Get materi info
materi_info = materi_data.get(mapel, {}).get(kelas, {})
if not materi_info:
    materi_info = {"deskripsi": "Materi belum tersedia.", "file_pdf": ""}

deskripsi = materi_info.get("deskripsi", "Materi belum tersedia.")
file_pdf = materi_info.get("file_pdf", "")

st.markdown(f"""
    <div class='mascot-card' style='margin: 20px 0;'>
        <h4 style='color: #1F2937; margin-top: 0;'>📖 {deskripsi}</h4>
        <p style='color: #6B7280; font-size: 14px; margin-top: 10px;'>
            Baca materi berikut, lalu tanyakan ke PANDAI jika ada yang tidak dimengerti!
        </p>
    </div>
""", unsafe_allow_html=True)

# Display PDF jika ada (FIXED: Dengan Navigasi Kontrol Halaman)
if file_pdf and os.path.exists(file_pdf):
    st.markdown("### 📄 Materi Lengkap (PDF)")
    
    from streamlit_pdf_viewer import pdf_viewer
    
    # Inisialisasi nomor halaman di session state jika belum terdaftar
    if "pdf_page" not in st.session_state:
        st.session_state.pdf_page = 1

    # Grid kolom untuk tombol navigasi kontrol halaman
    col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
    
    with col_nav1:
        if st.button("⬅️ Sebelumnya", use_container_width=True, key="prev_page_btn"):
            if st.session_state.pdf_page > 1:
                st.session_state.pdf_page -= 1
                st.rerun()
                
    with col_nav2:
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 18px; margin-top: 5px;'>Halaman {st.session_state.pdf_page}</p>", unsafe_allow_html=True)
        
    with col_nav3:
        if st.button("Selanjutnya ➡️", use_container_width=True, key="next_page_btn"):
            st.session_state.pdf_page += 1
            st.rerun()

    # Tampilkan komponen pdf_viewer dikunci pada halaman aktif
    pdf_viewer(file_pdf, height=600, pages_to_render=[st.session_state.pdf_page])
    
    # Input tambahan untuk melompati halaman secara manual
    col_jump1, col_jump2 = st.columns([1, 3])
    with col_jump1:
        jump_page = st.number_input("Loncat ke Halaman:", min_value=1, value=st.session_state.pdf_page, step=1, key="jump_page_input")
        if jump_page != st.session_state.pdf_page:
            st.session_state.pdf_page = jump_page
            st.rerun()
        
    with open(file_pdf, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    
    # Download button sebagai fallback
    st.download_button(
        label="📥 Download Materi PDF",
        data=pdf_bytes,
        file_name=os.path.basename(file_pdf),
        mime="application/pdf",
        use_container_width=True
    )
elif file_pdf:
    st.warning(f"⚠️ File PDF tidak ditemukan: {file_pdf}")
else:
    st.markdown("""
        <div style='background: #FEF3C7; padding: 15px; border-radius: 12px; border-left: 4px solid #F59E0B; margin: 20px 0;'>
            <p style='color: #92400E; font-weight: 600; margin: 0;'>📚 Materi Belum Tersedia</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# =================================================
# 6. CHAT AI UNTUK TANYA JAWAB
# =================================================
st.markdown("## 🤖 Tanya PANDAI")
st.caption("💡 Tanyakan apa saja seputar materi yang sedang kamu pelajari!")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    try:
        # Inisialisasi Klien Protokol Baru
        client = genai.Client(api_key=api_key)
        
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        # Menggunakan Form agar input jauh lebih stabil di Streamlit
        with st.form(key="chat_form", clear_on_submit=True):
            question = st.text_input(
                "Tulis pertanyaanmu di sini...",
                placeholder=f"Contoh: Jelaskan lebih lanjut tentang {mapel} untuk {kelas}"
            )
            submit_button = st.form_submit_button("🚀 Kirim Pertanyaan", use_container_width=True, type="primary")
        
        if submit_button and question:
            # Check cooldown
            if "last_chat_request" in st.session_state:
                time_since_last = time.time() - st.session_state.last_chat_request
                if time_since_last < 10:  # 10 second cooldown for chat
                    remaining = int(10 - time_since_last)
                    st.error(f"❌ Mohon tunggu {remaining} detik sebelum bertanya lagi (untuk menghindari limit kuota)")
                    st.info("💡 Tips: Tunggu sebentar agar sistem AI tidak terlalu sibuk")
                    st.stop()
            
            with st.spinner("🧠 PANDAI sedang berpikir..."):
                try:
                    # Update last request time
                    st.session_state.last_chat_request = time.time()
                    
                    st.session_state.chat_history.append({"role": "user", "content": question})
                    
                    context = (
                        f"Siswa {kelas} sedang belajar {mapel}. Materi: {deskripsi}. "
                        f"Jawab pertanyaan ini dengan bahasa sangat sederhana, analogi menyenangkan, "
                        f"ramah, dan mudah dipahami anak kelas 1-6 SD: {question}"
                    )
                    
                    # Pemanggilan menggunakan Protokol Baru
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=context
                    )
                    
                    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                    st.rerun()
                except Exception as e:
                    error_msg = str(e)
                    if "quota" in error_msg.lower() or "429" in error_msg:
                        st.error("❌ Sistem sedang sibuk. Tunggu sebentar lalu coba lagi")
                        st.info("💡 Tips : Mohon ditunggu")
                    else:
                        st.error(f"❌ Gagal memproses: {e}")
        
        # Display chat history (Native Streamlit chat layout)
        if st.session_state.chat_history:
            st.markdown("### 💬 Riwayat Percakapan")
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    with st.chat_message("user"):
                        st.write(msg["content"])
                else:
                    with st.chat_message("assistant", avatar="🐼"):
                        st.write(msg["content"])
            
            st.write("") # Spacer
            if st.button("🗑️ Hapus Riwayat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
                
    except Exception as e:
        st.error(f"❌ Error konfigurasi AI: {e}")
else:
    st.warning("⚠️ GEMINI_API_KEY tidak ditemukan di .env file.")

# =================================================
# 7. FOOTER
# =================================================
st.markdown("""
    <div style='text-align: center; color: #9CA3AF; font-size: 13px; padding-top: 25px; border-top: 1px solid #E5E7EB; margin-top: 40px;'>
        🐼 PANDAI - Mode Siswa • © 2026
    </div>
""", unsafe_allow_html=True)