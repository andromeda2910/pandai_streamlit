# 🐼 PANDAI (Asisten Pendidikan Berbasis AI)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://share.streamlit.io/)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B)](https://streamlit.io/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Gemini%202.5%20Flash-00BCD4)](https://ai.google.dev/)

**PANDAI** adalah aplikasi berbasis web interaktif yang dirancang khusus untuk membantu digitalisasi ekosistem pendidikan di Indonesia. Memanfaatkan kecerdasan buatan dari **Gemini 2.5 Flash**, aplikasi ini menyediakan alat bantu taktis dan produktif bagi **Siswa** maupun **Guru** jenjang Sekolah Dasar (SD Kelas 1-6).

---

## 🌟 Fitur Utama (Mode Guru)

Di dalam menu Guru (`2_Guru.py`), terdapat fitur canggih yang bekerja secara instan tanpa basa-basi untuk kebutuhan administrasi sekolah:
1. **📝 Perencanaan Pembelajaran (RPP) Otomatis**
   * Menyusun Rencana Pelaksanaan Pembelajaran (RPP) formal sesuai standar Kurikulum Nasional secara instan berdasarkan Mata Pelajaran, Kelas, Topik, dan Durasi.
   * Dilengkapi fitur ekspor dokumen langsung ke format **Microsoft Word (.docx)** yang rapi dan siap cetak.
2. **🎯 Generator Kuis & LKPD Interaktif**
   * Membuat Lembar Kerja Peserta Didik (LKPD) berupa soal pilihan ganda (A, B, C, D) yang disesuaikan dengan tingkat kesulitan (Mudah, Sedang, Sulit).
   * Menghasilkan file cetak otomatis berformat **PDF LKPD** lengkap dengan lembar identitas siswa dan kunci jawaban terintegrasi.
3. **📚 Riwayat Pembuatan Dokumentasi**
   * Menyimpan riwayat dokumen RPP dan Kuis yang berhasil dibuat selama sesi berjalan menggunakan managemen *Session State* Streamlit.

---

## 📂 Struktur Proyek

Aplikasi ini dibangun menggunakan arsitektur *Multipage* bawaan Streamlit yang efisien:

```text
pandai_streamlit/
│
├── .streamlit/
│   └── config.toml         # Konfigurasi tema dan visual Streamlit
├── materi_pdf/             # Penyimpanan modul atau materi ajar pendukung
├── pages/                  # Direktori halaman multipage
│   ├── 1_Siswa.py          # Ruang belajar interaktif untuk Siswa
│   └── 2_Guru.py           # Pusat alat bantu administrasi Guru (RPP & Kuis)
├── app.py                  # Beranda Utama / Pintu Masuk Aplikasi PANDAI
├── style.css               # Kustomisasi UI Modern & Estetik
├── requirements.txt        # Daftar dependency / library pihak ketiga
└── README.md               # Dokumentasi proyek (File ini)