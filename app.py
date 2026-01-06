import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Gradient Visualisation", layout="centered")

st.title("Gradient and Steepest Ascent Visualisation")

st.markdown("""
This interactive app helps you understand **gradients of functions of two variables**
and why the gradient gives the **direction of steepest ascent**.
""")

# -----------------------------
# Function selection
# -----------------------------
function_choice = st.selectbox(
    "Choose a function:",
    ("f(x, y) = x² + y²", "f(x, y) = x²y + y")
)

# -----------------------------
# Sliders for x and y
# -----------------------------
x0 = st.slider("x value", -3.0, 3.0, 1.0, 0.1)
y0 = st.slider("y value", -3.0, 3.0, 1.0, 0.1)

# -----------------------------
# Define functions and gradients
# -----------------------------
x = np.linspace(-3, 3, 60)
y = np.linspace(-3, 3, 60)
X, Y = np.meshgrid(x, y)

if function_choice == "f(x, y) = x² + y²":
    Z = X**2 + Y**2
    z0 = x0**2 + y0**2

    grad_x = 2 * x0
    grad_y = 2 * y0

else:
    Z = X**2 * Y + Y
    z0 = x0**2 * y0 + y0

    grad_x = 2 * x0 * y0
    grad_y = x0**2 + 1

gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# -----------------------------
# 3D surface plot
# -----------------------------
st.subheader("3D Surface Plot")

surface = go.Surface(x=X, y=Y, z=Z, colorscale="viridis")
point = go.Scatter3d(
    x=[x0], y=[y0], z=[z0],
    mode="markers",
    marker=dict(size=6, color="red"),
    name="Selected Point"
)

fig = go.Figure(data=[surface, point])
fig.update_layout(
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="f(x, y)"
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Gradient vector (2D plot)
# -----------------------------
st.subheader("Gradient Vector at the Selected Point")

fig2, ax = plt.subplots()
ax.quiver(
    x0, y0, grad_x, grad_y,
    angles='xy', scale_units='xy', scale=1, color='red'
)
ax.scatter(x0, y0, color='black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Gradient Vector in the xy-plane")
ax.grid(True)

st.pyplot(fig2)

# -----------------------------
# Display gradient values
# -----------------------------
st.markdown(f"""
**Gradient at ({x0:.2f}, {y0:.2f})**  
\[
\\nabla f = ({grad_x:.2f}, {grad_y:.2f})
\]

**Magnitude of gradient:**  
\[
|\\nabla f| = {gradient_magnitude:.2f}
\]
""")

# -----------------------------
# Explanations for students
# -----------------------------
st.subheader("What does the gradient represent?")

st.markdown("""
The **gradient** of a function \( f(x, y) \) is a vector:

\[
\\nabla f = \\left( \\frac{\\partial f}{\\partial x}, \\frac{\\partial f}{\\partial y} \\right)
\]

It tells us:
- How fast the function increases in the **x-direction**
- How fast the function increases in the **y-direction**

So, the gradient combines both rates of change into **one vector**.
""")

st.subheader("Why does the gradient give the direction of steepest ascent?")

st.markdown("""
The gradient vector always points in the direction where the function
**increases most rapidly**.

- Moving **in the direction of the gradient** increases the function value as fast as possible.
- The **magnitude** of the gradient tells us *how steep* the surface is at that point.

This is why the gradient is called the **direction of steepest ascent**.
""")

st.markdown("---")
st.markdown("📘 *Designed for undergraduate multivariable calculus students*")
