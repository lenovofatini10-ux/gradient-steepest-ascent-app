import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Gradient & Steepest Ascent Visualisation",
    layout="centered"
)

st.title("Gradient and Direction of Steepest Ascent")

st.markdown("""
This app visualises the **gradient of a function of two variables**
and explains why it gives the **direction of steepest ascent**.
""")

# --------------------------------------------------
# Function selection
# --------------------------------------------------
function_choice = st.selectbox(
    "Choose a function:",
    [
        "f(x, y) = x² + y²",
        "f(x, y) = x²y + y"
    ]
)

# --------------------------------------------------
# Sliders
# --------------------------------------------------
x0 = st.slider("x value", -3.0, 3.0, 1.0, 0.1)
y0 = st.slider("y value", -3.0, 3.0, 1.0, 0.1)

# --------------------------------------------------
# Grid
# --------------------------------------------------
x = np.linspace(-3, 3, 60)
y = np.linspace(-3, 3, 60)
X, Y = np.meshgrid(x, y)

# --------------------------------------------------
# Functions and gradients
# --------------------------------------------------
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

grad_mag = np.sqrt(grad_x**2 + grad_y**2)

# --------------------------------------------------
# 3D plot
# --------------------------------------------------
st.subheader("3D Surface Plot")

fig = go.Figure()

fig.add_surface(x=X, y=Y, z=Z, colorscale="viridis")
fig.add_scatter3d(
    x=[x0], y=[y0], z=[z0],
    mode="markers",
    marker=dict(size=6, color="red")
)

fig.update_layout(
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="f(x,y)"
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Gradient vector plot
# --------------------------------------------------
st.subheader("Gradient Vector in the xy-plane")

fig2, ax = plt.subplots()
ax.quiver(x0, y0, grad_x, grad_y, scale=1, scale_units="xy", angles="xy", color="red")
ax.scatter(x0, y0, color="black")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

st.pyplot(fig2)

# --------------------------------------------------
# Gradient values (SAFE LaTeX)
# --------------------------------------------------
st.markdown(f"**Gradient at ({x0:.2f}, {y0:.2f})**")
st.latex(r"\nabla f = (" + f"{grad_x:.2f}, {grad_y:.2f}" + ")")

st.markdown("**Magnitude of gradient**")
st.latex(r"|\nabla f| = " + f"{grad_mag:.2f}")

# --------------------------------------------------
# GENERAL explanation (works for BOTH functions)
# --------------------------------------------------
st.subheader("What does the gradient represent?")

st.markdown("""
The gradient of a function of two variables is a vector that describes how
the function changes with respect to both variables.
""")

st.latex(r"\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)")

st.markdown("""
- The first component measures the rate of change in the **x-direction**
- The second component measures the rate of change in the **y-direction**

Together, the gradient combines both rates of change into a **single vector**.
""")

st.subheader("Why does the gradient give the direction of steepest ascent?")

st.markdown("""
The gradient vector always points in the direction where the function increases
**most rapidly**.
""")

st.markdown("""
- Moving in the gradient direction produces the **maximum increase** in the function value  
- The magnitude of the gradient indicates **how steep** the surface is at that point
""")

# --------------------------------------------------
# SPECIAL interpretation ONLY for x² + y²
# --------------------------------------------------
if function_choice == "f(x, y) = x² + y²":

    st.subheader("Geometric Interpretation for $f(x,y)=x^2+y^2$")

    st.markdown("**1. Gradient points directly away from the origin**")
    st.latex(r"\nabla f = (2x, 2y)")

    st.markdown("""
The gradient vector is parallel to the position vector \((x,y)\).
Hence, it always points **radially outward from the origin**.
""")

    st.markdown("**2. Indicates the direction of steepest increase**")
    st.markdown("""
The function increases most rapidly when moving away from the origin,
which is exactly the direction of the gradient.
""")

    st.markdown("**3. The surface is a paraboloid**")
    st.markdown("""
The surface \(z = x^2 + y^2\) is an upward-opening **paraboloid** with a
minimum at the origin.
""")

# --------------------------------------------------
st.markdown("---")
st.markdown("📘 *Undergraduate multivariable calculus visualisation*")
