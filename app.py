from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Journey.pdf"
cv_file = current_dir / "assets" / "obaid_yousuf_cv.pdf"
profile_pic = current_dir / "assets" / "profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ubaid Yousaf Khan"
PAGE_ICON = ":computer:"
NAME = "Ubaid Yousaf Khan"
Designation = "Chairman Young Think Tank"
DESCRIPTION = """
IR Scholar, Journalist, Political Analyst, Researcher
"""
EMAIL = "Ubaidkhan78688@gmail.com"
PHONE = "+92 335 5536445"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/c/UbaidYousafKhan",
    "Facebook": "https://www.facebook.com/UYK.Official/",
    "Twitter": "https://twitter.com/ubaidykhan",
    "Instagram": "https://www.instagram.com/uyk.official/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.markdown(f"**{Designation}**")
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 My Journey",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label=" 📄 My Complete CV",
        data=cv_file.read_bytes(),
        file_name=cv_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", PHONE)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Education ---
st.write('\n')
st.header("Education")
st.write('\n')
st.write("📚 **BS(hons) in International Relations**")
st.write("📚 **M.Phil in International Relations**")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- ✔️ Journalist
- ✔️ Excellent Research Skills
- ✔️ Strong Communication Skills
- ✔️ 3 Years of Experience in Teaching
- ✔️ Strong Conceptual Understanding of International Relations
"""
)


# --- Work Experiance ---
st.write('\n')

st.subheader("Work Experience")
st.write(
"""
- → Running Organization named Karwan from last 3 years
- → 2 Years of Experience in TV shows
- → 1+ Year of Experience in Organizing Events
- → 5+ Years of Experience in Social Work

"""
)

# --- HARD SKILLS ---
st.write('\n')
col1, col2 = st.columns(2, gap="small")
with col1:
    st.subheader("Hard Skills")
    st.write(
    """
    - → Reporting
    - → Copy Writing
    - → Interviewing
    - → Public Relations
    - → Observations
    - → Communication
    - → Investigative Journalism

"""
)


# --- Soft SKILLS ---
with col2:
    st.subheader("Soft Skills")
    st.write(
    """
    - → Team Work
    - → Leadership Skills
    - → Decision Making
    - → Problem Solving
    - → Time Management
    - → Creativity
    - → Adaptability

"""
)





































