import streamlit as st
import streamlit.components.v1 as components
import os

# -----------------------------------------------------------------------------
# Sayfa Konfigürasyonu
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="HEDİYEYİ KAP HEDEFİX",
    page_icon="🏆",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Tam Ekran ve Header/Footer Gizleme CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        /* Streamlit Header ve Footer'ı tamamen gizle */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* Ana sayfanın kaydırma çubuğunu gizle */
        body {
            overflow: hidden;
            margin: 0;
            padding: 0;
        }
        
        /* Streamlit'in iç konteyner boşluklarını sıfırla */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* iframe'i ekranın tamamına sabitle */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
            z-index: 999999;
        }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HTML Dosyasını Okuma ve Gösterme
# -----------------------------------------------------------------------------
html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

if os.path.exists(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_code = f.read()

        # scrolling=False yaptık çünkü CSS ile fixed full screen verdik.
        # index.html kendi içerisinde scroll bar barındırmalıdır.
        components.html(html_code, height=2000) # Yüksek değer, CSS ile ezilecek.

    except Exception as e:
        st.error(f"Hata: {e}")
else:
    st.error("index.html bulunamadı! Lütfen dosyanın app.py ile aynı klasörde olduğundan emin olun.")
