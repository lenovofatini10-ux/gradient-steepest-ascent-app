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
This interactive app visualises the **gradient of a function of two variables**
and explains why it gives the **direction of steepest ascent**.
""")

# --------------------------------------------------
# Function selection
# --------------------------------------------------
function_choice = st.selectbox(
    "Choose a function:",
    (
        "f(x, y) = x² + y²",
        "f(x, y) = x²y + y"
    )
)

# --------------------------------------------------
# Sliders for x and y
# --------------------------------------------------
x0 = st.slider("x value", -3.0, 3.0, 1.0, 0.1)
y0 = st.slider("y value", -3.0, 3.0, 1.0, 0.1)

# --------------------------------------------------
# Define grid
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

gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# --------------------------------------------------
# 3D surface plot
# --------------------------------------------------
st.subheader("3D Surface Plot of the Function")

surface = go.Surface(
    x=X,
    y=Y,
    z=Z,
    colorscale="viridis"
)

point = go.Scatter3d(
    x=[x0],
    y=[y0],
    z=[z0],
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

# --------------------------------------------------
# Gradient vector plot (2D)
# --------------------------------------------------
st.subheader("Gradient Vector at the Selected Point")

fig2, ax = plt.subplots()

ax.quiver(
    x0, y0,
    grad_x, grad_y,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="red"
)

ax.scatter(x0, y0, color="black")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Gradient Vector in the xy-plane")
ax.grid(True)

st.pyplot(fig2)

# --------------------------------------------------
# Gradient values (LaTeX FIXED)
# --------------------------------------------------
st.markdown(f"**Gradient at ({x0:.2f}, {y0:.2f})**")
st.latex(r"\nabla f = (" + f"{grad_x:.2f}, {grad_y:.2f}" + ")")

st.markdown("**Magnitude of the gradient:**")
st.latex(r"|\nabla f| = " + f"{gradient_magnitude:.2f}")

# --------------------------------------------------
# Explanations for students
# --------------------------------------------------
st.subheader("What does the gradient represent?")

st.markdown("""
The **gradient** of a function of two variables is a vector that describes
how the function changes with respect to both variables.
""")

st.latex(
    r"\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)"
)

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
- Moving in the direction of the gradient produces the **maximum increase** in the function value
- The magnitude of the gradient indicates **how steep** the surface is at that point
""")

# --------------------------------------------------
# Special interpretation for f(x, y) = x² + y²
# --------------------------------------------------
if function_choice == "f(x, y) = x² + y²":

    st.subheader("Geometric Interpretation for $f(x, y) = x^2 + y^2$")

    st.markdown("**1. The gradient points directly away from the origin**")

    st.latex(r"\nabla f = (2x, 2y)")

    st.markdown("""
At any point \((x, y)\), the gradient vector is a scalar multiple of the position vector
\((x, y)\). Therefore, the gradient always points **radially outward from the origin**.
""")

    st.markdown("**2. The gradient indicates the direction of steepest increase**")

    st.markdown("""
Because the surface rises equally in all directions away from the origin,
the gradient gives the direction in which the function value increases
**most rapidly**.
""")

    st.markdown("**3. The surface is a paraboloid**")

    st.markdown("""
The graph of \( f(x, y) = x^2 + y^2 \) is an **upward-opening paraboloid**.
It has a minimum at the origin, and the height of the surface increases
symmetrically as we move away from \((0,0)\).
""")

    st.markdown("""
This explains why the gradient always points away from the origin and why
its magnitude increases with distance from the origin.
""")

st.markdown("---")
st.markdown("📘 *Suitable for undergraduate multivariable calculus students*")
