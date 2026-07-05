import plotly.express as px
import json

def generate_bar_chart(df):

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    text_columns = df.select_dtypes(include="object").columns.tolist()

    if not numeric_columns or not text_columns:
        return None

    x = text_columns[0]
    y = numeric_columns[0]

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=f"{y} by {x}"
    )

    fig.update_layout(template=None)

    # Convert Plotly object into normal Python dictionary
    chart = json.loads(fig.to_json())

    return chart