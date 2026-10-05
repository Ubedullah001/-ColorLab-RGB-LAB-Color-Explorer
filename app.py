import streamlit as st
import colorsys

st.set_page_config(
    page_title="RGB & LAB Color App",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 RGB & LAB Color App")
st.write("Explore RGB primary colors and create colors by changing LAB values.")

# RGB Colors
st.header("Primary RGB Colors")

col1, col2, col3 = st.columns(3)

with col1:
    st.color_picker("Red", "#FF0000", disabled=True)

with col2:
    st.color_picker("Green", "#00FF00", disabled=True)

with col3:
    st.color_picker("Blue", "#0000FF", disabled=True)

# LAB Values
st.header("Create a Color with LAB Values")

L = st.slider("L (Lightness)", 0, 100, 50)
A = st.slider("A (Green ↔ Red)", -128, 127, 0)
B = st.slider("B (Blue ↔ Yellow)", -128, 127, 0)

# Simple LAB to RGB approximation
r = max(0, min(255, L * 2.55 + A * 0.8))
g = max(0, min(255, L * 2.55 - A * 0.4 - B * 0.2))
b = max(0, min(255, L * 2.55 + B * 0.8))

r = int(r)
g = int(g)
b = int(b)

hex_color = f"#{r:02X}{g:02X}{b:02X}"

st.subheader("Resulting Color")

st.color_picker("Generated Color", hex_color, disabled=True)

st.write(f"**RGB:** ({r}, {g}, {b})")
st.write(f"**HEX:** {hex_color}")

st.success("Change the LAB values to create different colors.")
