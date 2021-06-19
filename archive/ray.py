import plotly.express as px
import numpy as np

fig = px.line_3d(x= np.linspace(1,10), y=np.linspace(1,10), z=np.linspace(1,10), title="a ray")
fig.update_layout(
    width=400, height=400,
    margin=dict(t=80, r=0, l=40, b=40)
)
fig.show()
