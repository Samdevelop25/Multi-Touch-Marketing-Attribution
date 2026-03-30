import pandas as pd
import plotly.graph_objects as go

def plot_replit_funnel(stages, counts):
    fig = go.Figure(go.Funnel(
        y = stages,
        x = counts,
        textinfo = "value+percent initial"))
    
    fig.update_layout(title_text="Replit User Conversion Funnel")
    fig.show()

# Example Data
stages = ["Website Visit", "Account Created", "Repl Created", "Paid Core Plan"]
counts = [10000, 4500, 2000, 350]
# plot_replit_funnel(stages, counts)
