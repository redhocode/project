import time
import streamlit as st

# === SET FULL WIDTH ===
st.set_page_config(layout="wide")

# Data lirik dan timing
lirik = [
    ("Berilah sebuah pertanda bila", 28.0),
    ("Bila kau menyimpan rasa yg sama", 35.0),
    ("Tunjukkanlah Anindya", 40.0),
    ("Berikan aku secercah harapan Anindya", 45.0),
]

# CSS background dan confetti
css_style = """
<style>
@keyframes wave {
  0% {background-position: 0 0;}
  100% {background-position: 1000px 0;}
}
body {
  background: linear-gradient(90deg, #f0f8ff, #b0e0e6, #f0f8ff);
  background-size: 1000px 100%;
  animation: wave 30s linear infinite;
  overflow-x: hidden;
}
h1 {
  color: #034f84;
  text-align: center;
  margin-bottom: 50px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 3rem;
}
.lyrics-text {
  font-size: 2.2rem;
  font-weight: 600;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 20px 0;
  color: #222222;
}
.confetti-container {
  pointer-events: none;
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  overflow: visible;
  z-index: 9999;
}
.confetti {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  opacity: 0.8;
  animation-name: confetti-fall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}
@keyframes confetti-fall {
  0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
  100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
""" + "".join([
    f".confetti:nth-child({i+1}) {{ left: {5 + i*10}vw; animation-duration: {4 + i*0.5}s; animation-delay: {0.5*i}s; background: #{hex(0x100000 + i*123456)[2:]}; }}\n"
    for i in range(10)
]) + """
</style>
<div class="confetti-container">
  """ + "\n".join([f"<div class='confetti'></div>" for _ in range(10)]) + """
</div>
"""

# Render CSS & animasi
st.markdown(css_style, unsafe_allow_html=True)
st.title("🎵 Surat Eletronikku 🎵")

# Fungsi delay ketikan
def get_typing_delay(line_length, interval):
    delay = interval / max(line_length, 1)
    return max(0.04, min(0.15, delay))

# Tombol trigger
if st.button("Klik Sini!"):
    # Buat 2 kolom: kiri (lirik), kanan (video)
    col1, col2 = st.columns([2, 1])

    with col2:
        # Embed YouTube video (mobile-friendly)
        st.markdown(
            """
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
                <iframe src="https://www.youtube.com/embed/YB_k5TeOK7I"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen
                        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                </iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col1:
        lyrics_container = st.empty()
        start_time = time.time()

        for i, (line, start_sec) in enumerate(lirik):
            while True:
                elapsed = time.time() - start_time
                if elapsed >= start_sec:
                    break
                time.sleep(0.05)

            next_start_sec = lirik[i + 1][1] if i < len(lirik) - 1 else start_sec + 4
            interval = next_start_sec - start_sec
            typing_delay = get_typing_delay(len(line), interval)

            teks_tertulis = ""
            for c in line:
                teks_tertulis += c
                lyrics_container.markdown(f"<div class='lyrics-text'>{teks_tertulis}</div>", unsafe_allow_html=True)
                time.sleep(typing_delay)

        # st.success("Selesai!")

else:
    st.info("Klik tombol **Klik Sini!** untuk mulai. lalu Player YouTube akan muncul di kanan.")
