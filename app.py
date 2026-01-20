import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="AI Tipping Point Atlas", page_icon="🦋", layout="wide")

# --- HIGH-FIDELITY CSS (The "Sci-Fi" Look) ---
st.markdown("""
<style>
    /* Main Background - Deep Space Gradient */
    .stApp {
        background: linear-gradient(to bottom, #000000, #0a0a12);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #222;
    }
    
    /* Custom Metric Cards (Glassmorphism) */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* Typography */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: -0.5px;
        color: white;
    }
    
    /* Remove Plotly White Borders */
    .js-plotly-plot .plotly .gl-container {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- MATH ENGINE: BIFURCATION & EWS ---
@st.cache_data
def get_bifurcation_data(min_r, max_r, steps=600, iterations=1000, last=100):
    """
    Generates the Feigenbaum Bifurcation Diagram.
    Cached for performance.
    """
    r_values = np.linspace(min_r, max_r, steps)
    x = 1e-5 * np.ones(steps)
    results = []

    # Burn-in period
    for i in range(iterations):
        x = r_values * x * (1 - x)
        if i >= (iterations - last):
            results.append(pd.DataFrame({'r': r_values, 'x': x}))
            
    return pd.concat(results)

def simulate_time_series(r, noise_level=0.01, steps=200):
    x = np.zeros(steps)
    x[0] = 0.5
    for t in range(1, steps):
        update = r * x[t-1] * (1 - x[t-1])
        # Ensure noise doesn't crash calculations
        noise = np.random.normal(0, max(0.0001, noise_level))
        x[t] = np.clip(update + noise, 0, 1)
    return x

# --- UI LAYOUT ---
def main():
    st.sidebar.title("🎛️ Chaos Control")
    st.sidebar.markdown("Adjust the system parameters below.")
    
    with st.sidebar.form("controls"):
        # Explicitly casting to float to prevent type errors
        r_focus = float(st.slider("Recursive Rate (r)", 2.5, 4.0, 3.8, 0.01, help="Controls the chaotic intensity."))
        noise = float(st.slider("Signal Noise", 0.0, 0.05, 0.01, help="Adds random perturbations."))
        run_update = st.form_submit_button("Update Analysis")
    
    # Header
    st.title("The AI Tipping Point Atlas")
    st.markdown("""
    <div style='background: rgba(0,204,150,0.1); padding: 10px; border-radius: 5px; border-left: 3px solid #00CC96; margin-bottom: 20px;'>
        <small style='color: #00CC96; font-weight: bold;'>SYSTEM STATUS: ONLINE</small><br>
        Mapping the mathematical transition from <b>Stability</b> to <b>Chaos</b> in recursive neural systems.
    </div>
    """, unsafe_allow_html=True)
    
    # --- ROW 1: THE BIFURCATION DIAGRAM ---
    st.subheader("1. Global Stability Map")
    
    # Computation
    df_bif = get_bifurcation_data(2.5, 4.0, steps=800)
    
    # Visual
    fig_bif = go.Figure()
    
    # The Chaos Tree
    fig_bif.add_trace(go.Scattergl(
        x=df_bif['r'], 
        y=df_bif['x'], 
        mode='markers',
        marker=dict(size=1, color='#00CC96', opacity=0.15),
        name='Attractor State',
        hoverinfo='skip'
    ))
    
    # The "Scanner" Line
    fig_bif.add_vline(x=r_focus, line_width=2, line_color="#FF4B4B", line_dash="solid", opacity=0.8)
    
    fig_bif.update_layout(
        template="plotly_dark",
        height=450,
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0,r=0,t=0,b=0),
        xaxis=dict(title="Recursive Growth Rate (r)", showgrid=False, zeroline=False),
        yaxis=dict(title="Equilibrium States", showgrid=False, zeroline=False),
        showlegend=False
    )
    st.plotly_chart(fig_bif, use_container_width=True)
    
    # --- ROW 2: CRITICAL SLOWING DOWN ---
    st.markdown("---")
    st.subheader(f"2. Signal Analysis (r = {r_focus})")
    
    col_sim, col_metrics = st.columns([3, 1])
    
    # Run Simulation
    ts_data = simulate_time_series(r_focus, noise)
    ts_series = pd.Series(ts_data)
    
    # Calculate Metrics with SAFETY CHECKS
    autocorr = ts_series.autocorr(lag=1)
    variance = ts_series.var()
    
    # Fix NaN (Not a Number) errors if system is perfectly stable
    if pd.isna(autocorr):
        autocorr = 0.0
    if pd.isna(variance):
        variance = 0.0
    
    with col_sim:
        fig_ts = go.Figure()
        fig_ts.add_trace(go.Scatter(
            y=ts_data, 
            mode='lines', 
            line=dict(color='#FF4B4B', width=2), 
            fill='tozeroy',
            fillcolor='rgba(255, 75, 75, 0.1)', 
            name='System Output'
        ))
        fig_ts.update_layout(
            title="Real-time Trajectory",
            title_font_size=12,
            template="plotly_dark", 
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=250,
            margin=dict(l=0,r=0,t=30,b=0),
            yaxis_range=[0, 1],
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
        )
        st.plotly_chart(fig_ts, use_container_width=True)
        
    with col_metrics:
        # Dynamic Coloring
        ac_val = f"{autocorr:.2f}"
        ac_color = "#00CC96" # Green
        if autocorr > 0.7: ac_color = "#FFA15A" # Orange
        if autocorr > 0.9: ac_color = "#FF4B4B" # Red
        
        # Calculate width for the bar, ensuring it's a valid number
        bar_width = min(abs(autocorr) * 100, 100)
        
        # HTML Cards
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:12px; opacity:0.7">AUTOCORRELATION</span>
            <h2 style="color:{ac_color}; margin:0">{ac_val}</h2>
            <div style="height:4px; width:100%; background:#333; margin-top:5px; border-radius:2px;">
                <div style="height:100%; width:{bar_width}%; background:{ac_color}; border-radius:2px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True) # Spacer
        
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:12px; opacity:0.7">SYSTEM VARIANCE</span>
            <h2 style="color:white; margin:0">{variance:.4f}</h2>
        </div>
        """, unsafe_allow_html=True)

    # --- ROW 3: FOOTER ---
    st.markdown("---")
    st.caption("A visualization of the Logistic Map ($x_{n+1} = r x_n (1 - x_n)$).")

if __name__ == "__main__":
    main()