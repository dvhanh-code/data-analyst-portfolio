import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI & Data Science Job Market",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Syne:wght@600;700&display=swap');

/* ── global reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #f5f6fa;
    color: #1a1a2e;
}

/* ── gradient background ── */
.stApp {
    background: linear-gradient(135deg, #eef0fb 0%, #f0f4ff 35%, #faf5ff 65%, #f0f7ff 100%);
    background-attachment: fixed;
}

/* ── main area ── */
.main .block-container {
    padding: 2rem 2.5rem;
    max-width: 1440px;
    background: transparent;
}

/* ── sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f5f6ff 100%) !important;
    border-right: 1px solid #e2e4f0;
}
[data-testid="stSidebar"] section { padding: 1.5rem 1.2rem; }
[data-testid="stSidebar"] * { color: #3a3a5c !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #1a1a2e !important;
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* sidebar labels */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSlider label {
    color: #9999bb !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* file uploader */
[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background: transparent !important;
    border: 1px dashed #c8cadd !important;
    border-radius: 8px;
}

/* multiselect tags */
[data-testid="stSidebar"] .stMultiSelect span[data-baseweb="tag"] {
    background-color: rgba(99,102,241,0.08) !important;
    border: 1px solid rgba(99,102,241,0.2) !important;
    border-radius: 4px !important;
}
[data-testid="stSidebar"] .stMultiSelect span[data-baseweb="tag"] span {
    color: #4f46e5 !important;
    font-size: 0.75rem;
}

/* divider */
hr { border-color: #e2e4f0 !important; }

/* ── hero ── */
.hero {
    padding: 2.8rem 0 2rem;
    border-bottom: 1px solid rgba(99,102,241,0.12);
    margin-bottom: 2.4rem;
}
.hero-label {
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #9999bb;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: #1a1a2e;
    line-height: 1.15;
    margin: 0 0 0.5rem;
}
.hero-title span { color: #4f46e5; }
.hero-sub {
    font-size: 0.9rem;
    color: #9999bb;
    font-weight: 300;
}

/* ── KPI cards ── */
.kpi-wrap {
    background: rgba(255,255,255,0.7);
    border: 1px solid rgba(99,102,241,0.12);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    backdrop-filter: blur(12px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.kpi-wrap:hover {
    border-color: rgba(79,70,229,0.3);
    box-shadow: 0 4px 20px rgba(99,102,241,0.08);
}
.kpi-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #1a1a2e;
    line-height: 1;
}
.kpi-lbl {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #9999bb;
    margin-top: 0.35rem;
}

/* ── section label ── */
.sec-label {
    font-size: 0.68rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #9999bb;
    margin: 2rem 0 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #e2e4f0;
}

/* ── tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid #e2e4f0;
    gap: 0;
    padding: 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border: none;
    color: #9999bb;
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    padding: 0.7rem 1.4rem;
    border-bottom: 2px solid transparent;
    border-radius: 0;
}
.stTabs [aria-selected="true"] {
    color: #4f46e5 !important;
    border-bottom: 2px solid #4f46e5 !important;
    background: transparent !important;
}

/* ── expander ── */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.6) !important;
    border: 1px solid #e2e4f0 !important;
    border-radius: 8px;
    color: #6666aa !important;
    font-size: 0.8rem;
}

/* ── download button ── */
.stDownloadButton button {
    background: transparent !important;
    border: 1px solid #c8cadd !important;
    color: #6666aa !important;
    font-size: 0.78rem;
    border-radius: 6px;
    padding: 0.4rem 1rem;
}
.stDownloadButton button:hover {
    border-color: #4f46e5 !important;
    color: #4f46e5 !important;
}

/* ── footer ── */
.footer {
    text-align: center;
    color: #bbbbcc;
    font-size: 0.72rem;
    padding: 2.5rem 0 1rem;
    border-top: 1px solid #e2e4f0;
    margin-top: 4rem;
}
.footer a { color: #4f46e5; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── THEME ─────────────────────────────────────────────────────────────────────
BG   = "rgba(0,0,0,0)"
CARD = "#ffffff"
GRID = "#eef0f8"
LINE = "#e2e4f0"
COLORS = ["#4f46e5","#10b981","#f43f5e","#f59e0b","#0ea5e9","#8b5cf6","#06b6d4","#84cc16"]

PT = dict(
    paper_bgcolor=CARD, plot_bgcolor=CARD,
    font=dict(color="#4a4a6a", family="Inter", size=12),
    xaxis=dict(gridcolor=GRID, linecolor=LINE, tickcolor="#bbbbcc", zeroline=False),
    yaxis=dict(gridcolor=GRID, linecolor=LINE, tickcolor="#bbbbcc", zeroline=False),
    margin=dict(l=16, r=16, t=36, b=16),
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,0,0,0)",
                font=dict(color="#6666aa", size=11)),
)

def th(fig, title=""):
    fig.update_layout(**PT)
    if title:
        fig.update_layout(title=dict(text=title, font=dict(color="#c8c8d8", size=13,
                                                            family="Inter"), x=0, pad=dict(l=4)))
    return fig


# ── DATA LOADING ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    import os
    jobs_path   = "data/ai_jobs.csv"
    skills_path = "data/skills_demand.csv"

    if os.path.exists(jobs_path):
        df = pd.read_csv(jobs_path)
    else:
        st.error("data/ai_jobs.csv not found. Please add the dataset files to the data/ folder.")
        st.stop()

    # compute mid salary
    df["salary_usd"] = (df["salary_min_usd"] + df["salary_max_usd"]) / 2

    # normalise labels
    df["experience_level"] = df["experience_level"].str.strip()
    df["remote_type"]      = df["remote_type"].str.strip()
    df["company_size"]     = df["company_size"].str.strip()
    df["country"]          = df["country"].str.strip()

    # load skills if available
    skills_df = None
    if os.path.exists(skills_path):
        skills_df = pd.read_csv(skills_path)

    return df, skills_df

df_raw, skills_df = load_data()

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown("### Filters")

    year_range = st.slider("Year",
        int(df_raw["posted_year"].min()), int(df_raw["posted_year"].max()),
        (int(df_raw["posted_year"].min()), int(df_raw["posted_year"].max())))

    exp_sel    = st.multiselect("Experience",
                                sorted(df_raw["experience_level"].unique()),
                                default=sorted(df_raw["experience_level"].unique()))
    remote_sel = st.multiselect("Work Mode",
                                sorted(df_raw["remote_type"].unique()),
                                default=sorted(df_raw["remote_type"].unique()))
    size_sel   = st.multiselect("Company Size",
                                sorted(df_raw["company_size"].unique()),
                                default=sorted(df_raw["company_size"].unique()))
    top_n = st.slider("Top N Titles", 5, 15, 10)

    st.markdown("---")
    st.markdown("<span style='color:#9999bb;font-size:0.7rem;'>AI & DS Job Market 2020–2026</span>",
                unsafe_allow_html=True)

# ── FILTER ────────────────────────────────────────────────────────────────────
df = df_raw[
    df_raw["posted_year"].between(*year_range) &
    df_raw["experience_level"].isin(exp_sel) &
    df_raw["remote_type"].isin(remote_sel) &
    df_raw["company_size"].isin(size_sel)
].copy()

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">Data Visualization — Portfolio Project</div>
  <div class="hero-title">Global AI & Data Science<br><span>Job Market</span></div>
  <div class="hero-sub">Salary trends, role distribution, and hiring patterns &nbsp;·&nbsp; 2020 – 2026</div>
</div>
""", unsafe_allow_html=True)

# ── KPI ROW ───────────────────────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)
kpis = [
    (f"{len(df):,}",                             "Total Jobs"),
    (f"${df['salary_usd'].median()/1000:.0f}K",  "Median Salary"),
    (f"${df['salary_usd'].mean()/1000:.0f}K",    "Avg Salary"),
    (f"{df['job_title'].nunique()}",              "Unique Roles"),
    (f"{df['country'].nunique()}",                "Countries"),
]
for col, (v, l) in zip([k1,k2,k3,k4,k5], kpis):
    with col:
        st.markdown(f'<div class="kpi-wrap"><div class="kpi-val">{v}</div>'
                    f'<div class="kpi-lbl">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Salary Trends", "Job Roles", "Geography", "Deep Dive", "Skills"
])

# ══ TAB 1: SALARY TRENDS ══
with tab1:
    cl, cr = st.columns(2)

    with cl:
        st.markdown('<div class="sec-label">Median salary by year</div>', unsafe_allow_html=True)
        yearly = df.groupby("posted_year")["salary_usd"].median().reset_index()
        fig = px.bar(yearly, x="posted_year", y="salary_usd",
                     color_discrete_sequence=["#4f46e5"],
                     labels={"posted_year":"","salary_usd":"USD"},
                     text=yearly["salary_usd"].apply(lambda x: f"${x/1000:.0f}K"))
        fig.update_traces(textposition="outside", textfont=dict(color="#6666aa", size=11),
                          marker_opacity=0.85)
        fig.update_layout(uniformtext_minsize=9, uniformtext_mode="hide")
        th(fig); st.plotly_chart(fig, use_container_width=True)

    with cr:
        st.markdown('<div class="sec-label">Salary distribution by experience</div>', unsafe_allow_html=True)
        order = [o for o in ["Entry","Mid","Senior"] if o in df["experience_level"].unique()]
        fig2 = px.box(df, x="experience_level", y="salary_usd",
                      category_orders={"experience_level": order},
                      color="experience_level", color_discrete_sequence=COLORS,
                      labels={"experience_level":"","salary_usd":"USD"})
        fig2.update_layout(showlegend=False); th(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    cl2, cr2 = st.columns(2)
    with cl2:
        st.markdown('<div class="sec-label">Median salary by company size</div>', unsafe_allow_html=True)
        ss = df.groupby("company_size")["salary_usd"].median().reset_index().sort_values("salary_usd")
        fig3 = px.bar(ss, x="salary_usd", y="company_size", orientation="h",
                      color="company_size", color_discrete_sequence=COLORS,
                      labels={"salary_usd":"USD","company_size":""})
        fig3.update_layout(showlegend=False); th(fig3)
        st.plotly_chart(fig3, use_container_width=True)

    with cr2:
        st.markdown('<div class="sec-label">Salary trend by experience level</div>', unsafe_allow_html=True)
        ey = df.groupby(["posted_year","experience_level"])["salary_usd"].median().reset_index()
        fig4 = px.line(ey, x="posted_year", y="salary_usd", color="experience_level",
                       markers=True, color_discrete_sequence=COLORS,
                       labels={"posted_year":"","salary_usd":"USD","experience_level":""})
        fig4.update_traces(line_width=1.8, marker_size=5); th(fig4)
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown('<div class="sec-label">Salary distribution by work mode</div>', unsafe_allow_html=True)
    fig5 = px.violin(df, x="remote_type", y="salary_usd", color="remote_type",
                     box=True, points=False, color_discrete_sequence=COLORS,
                     labels={"remote_type":"","salary_usd":"USD"})
    fig5.update_layout(showlegend=False); th(fig5)
    st.plotly_chart(fig5, use_container_width=True)

# ══ TAB 2: JOB ROLES ══
with tab2:
    cl, cr = st.columns([3,2])

    with cl:
        st.markdown('<div class="sec-label">Top job titles by count</div>', unsafe_allow_html=True)
        tj = df["job_title"].value_counts().head(top_n).reset_index()
        tj.columns = ["job_title","count"]
        fig = px.bar(tj.sort_values("count"), x="count", y="job_title", orientation="h",
                     color="count", color_continuous_scale=["#e0e7ff","#4f46e5","#10b981"],
                     labels={"count":"","job_title":""})
        fig.update_layout(coloraxis_showscale=False); th(fig)
        st.plotly_chart(fig, use_container_width=True)

    with cr:
        st.markdown('<div class="sec-label">Experience level mix</div>', unsafe_allow_html=True)
        ec = df["experience_level"].value_counts().reset_index()
        ec.columns = ["level","count"]
        fig2 = px.pie(ec, names="level", values="count",
                      color_discrete_sequence=COLORS, hole=0.6)
        fig2.update_traces(textfont_color="#1a1a2e", textfont_size=11); th(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    cl2, cr2 = st.columns(2)
    with cl2:
        st.markdown('<div class="sec-label">Median salary by role</div>', unsafe_allow_html=True)
        top_nm = df["job_title"].value_counts().head(top_n).index
        sr = (df[df["job_title"].isin(top_nm)]
              .groupby("job_title")["salary_usd"].median().sort_values().reset_index())
        fig3 = px.bar(sr, x="salary_usd", y="job_title", orientation="h",
                      color="salary_usd", color_continuous_scale=["#e0e7ff","#4f46e5","#10b981"],
                      labels={"salary_usd":"USD","job_title":""})
        fig3.update_layout(coloraxis_showscale=False); th(fig3)
        st.plotly_chart(fig3, use_container_width=True)

    with cr2:
        st.markdown('<div class="sec-label">Jobs by industry</div>', unsafe_allow_html=True)
        indc = df["industry"].value_counts().reset_index()
        indc.columns = ["industry","count"]
        fig4 = px.bar(indc, x="industry", y="count", color="industry",
                      color_discrete_sequence=COLORS,
                      labels={"industry":"","count":""})
        fig4.update_layout(showlegend=False); th(fig4)
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown('<div class="sec-label">Job title x experience — salary heatmap</div>', unsafe_allow_html=True)
    t10 = df["job_title"].value_counts().head(10).index
    hm  = (df[df["job_title"].isin(t10)]
           .groupby(["job_title","experience_level"])["salary_usd"]
           .median().reset_index()
           .pivot(index="job_title", columns="experience_level", values="salary_usd"))
    fig5 = px.imshow(hm.fillna(0), color_continuous_scale=["#e0e7ff","#4f46e5","#10b981"],
                     labels={"color":"Salary"}, aspect="auto")
    fig5.update_traces(texttemplate="%{z:,.0f}", textfont_size=10, textfont_color="#1a1a2e")
    th(fig5); st.plotly_chart(fig5, use_container_width=True)

# ══ TAB 3: GEOGRAPHY ══
with tab3:
    cl, cr = st.columns(2)

    with cl:
        st.markdown('<div class="sec-label">Top countries by job count</div>', unsafe_allow_html=True)
        tc = df["country"].value_counts().head(15).reset_index()
        tc.columns = ["country","count"]
        fig = px.bar(tc.sort_values("count"), x="count", y="country", orientation="h",
                     color="count", color_continuous_scale=["#e0e7ff","#4f46e5"],
                     labels={"count":"","country":""})
        fig.update_layout(coloraxis_showscale=False); th(fig)
        st.plotly_chart(fig, use_container_width=True)

    with cr:
        st.markdown('<div class="sec-label">Average salary by country (top 15)</div>', unsafe_allow_html=True)
        t15 = df["country"].value_counts().head(15).index
        ca  = df[df["country"].isin(t15)].groupby("country")["salary_usd"].mean().sort_values().reset_index()
        ca.columns = ["country","avg"]
        fig2 = px.bar(ca, x="avg", y="country", orientation="h",
                      color="avg", color_continuous_scale=["#fce7f3","#f43f5e","#f59e0b"],
                      labels={"avg":"USD","country":""})
        fig2.update_layout(coloraxis_showscale=False); th(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown('<div class="sec-label">Remote work adoption by country</div>', unsafe_allow_html=True)
    top15 = df["country"].value_counts().head(12).index
    rmc = (df[df["country"].isin(top15)]
           .groupby(["country","remote_type"]).size().reset_index(name="count"))
    fig3 = px.bar(rmc, x="country", y="count", color="remote_type",
                  barmode="stack", color_discrete_sequence=COLORS,
                  labels={"country":"","count":"","remote_type":""})
    th(fig3); st.plotly_chart(fig3, use_container_width=True)

# ══ TAB 4: DEEP DIVE ══
with tab4:
    cl, cr = st.columns(2)

    with cl:
        st.markdown('<div class="sec-label">Salary vs year by experience (bubble)</div>', unsafe_allow_html=True)
        bb = (df.groupby(["posted_year","experience_level"])
              .agg(med=("salary_usd","median"), cnt=("salary_usd","count"))
              .reset_index())
        fig = px.scatter(bb, x="posted_year", y="med", size="cnt",
                         color="experience_level", color_discrete_sequence=COLORS, size_max=48,
                         labels={"posted_year":"","med":"Median Salary","experience_level":"","cnt":"Count"})
        th(fig); st.plotly_chart(fig, use_container_width=True)

    with cr:
        st.markdown('<div class="sec-label">Remote work share over time</div>', unsafe_allow_html=True)
        rt = df.groupby(["posted_year","remote_type"]).size().reset_index(name="count")
        rt["pct"] = rt["count"] / rt.groupby("posted_year")["count"].transform("sum") * 100
        fig2 = px.area(rt, x="posted_year", y="pct", color="remote_type",
                       color_discrete_sequence=COLORS,
                       labels={"posted_year":"","pct":"Share (%)","remote_type":""})
        th(fig2); st.plotly_chart(fig2, use_container_width=True)

    cl2, cr2 = st.columns(2)
    with cl2:
        st.markdown('<div class="sec-label">Median salary by industry</div>', unsafe_allow_html=True)
        ins = df.groupby("industry")["salary_usd"].median().sort_values().reset_index()
        fig3 = px.bar(ins, x="salary_usd", y="industry", orientation="h",
                      color="salary_usd", color_continuous_scale=["#e0e7ff","#4f46e5","#10b981"],
                      labels={"salary_usd":"USD","industry":""})
        fig3.update_layout(coloraxis_showscale=False); th(fig3)
        st.plotly_chart(fig3, use_container_width=True)

    with cr2:
        st.markdown('<div class="sec-label">Salary range — min vs max by role</div>', unsafe_allow_html=True)
        top_nm2 = df["job_title"].value_counts().head(8).index
        rng = (df[df["job_title"].isin(top_nm2)]
               .groupby("job_title")
               .agg(min_sal=("salary_min_usd","median"), max_sal=("salary_max_usd","median"))
               .reset_index().sort_values("min_sal"))
        fig4 = px.bar(rng, x="max_sal", y="job_title", orientation="h",
                      color_discrete_sequence=["#e0e7ff"],
                      labels={"max_sal":"USD","job_title":""})
        fig4.add_bar(x=rng["min_sal"], y=rng["job_title"], orientation="h",
                     marker_color="#4f46e5", name="Min Salary")
        fig4.update_layout(barmode="overlay", showlegend=True); th(fig4)
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown('<div class="sec-label">Overall salary distribution</div>', unsafe_allow_html=True)
    fig5 = px.histogram(df, x="salary_usd", nbins=60,
                        color_discrete_sequence=["#4f46e5"],
                        labels={"salary_usd":"USD"})
    fig5.update_traces(opacity=0.8)
    fig5.update_layout(bargap=0.04); th(fig5)
    st.plotly_chart(fig5, use_container_width=True)

# ══ TAB 5: SKILLS ══
with tab5:
    if skills_df is not None:
        from collections import Counter

        # merge skills with salary
        merged = skills_df.merge(df_raw[["job_id","salary_usd","experience_level","posted_year"]],
                                 on="job_id", how="left")

        cl, cr = st.columns(2)
        with cl:
            st.markdown('<div class="sec-label">Most in-demand skills</div>', unsafe_allow_html=True)
            skc = merged["skill"].value_counts().head(20).reset_index()
            skc.columns = ["skill","count"]
            fig = px.bar(skc.sort_values("count"), x="count", y="skill", orientation="h",
                         color="count", color_continuous_scale=["#e0e7ff","#4f46e5","#10b981"],
                         labels={"count":"","skill":""})
            fig.update_layout(coloraxis_showscale=False); th(fig)
            st.plotly_chart(fig, use_container_width=True)

        with cr:
            st.markdown('<div class="sec-label">Skill share — top 10</div>', unsafe_allow_html=True)
            fig2 = px.pie(skc.head(10), names="skill", values="count",
                          color_discrete_sequence=COLORS, hole=0.55)
            fig2.update_traces(textfont_color="#1a1a2e", textfont_size=11); th(fig2)
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown('<div class="sec-label">Median salary by skill (top 15)</div>', unsafe_allow_html=True)
        top_skills = skc["skill"].head(15).tolist()
        sk_sal = (merged[merged["skill"].isin(top_skills)]
                  .groupby("skill")["salary_usd"].median()
                  .sort_values().reset_index())
        fig3 = px.bar(sk_sal, x="salary_usd", y="skill", orientation="h",
                      color="salary_usd", color_continuous_scale=["#fce7f3","#f43f5e","#f59e0b"],
                      labels={"salary_usd":"USD","skill":""})
        fig3.update_layout(coloraxis_showscale=False); th(fig3)
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown('<div class="sec-label">Skills by category</div>', unsafe_allow_html=True)
        cat_c = merged["skill_category"].value_counts().reset_index()
        cat_c.columns = ["category","count"]
        fig4 = px.pie(cat_c, names="category", values="count",
                      color_discrete_sequence=COLORS, hole=0.45)
        fig4.update_traces(textfont_color="#1a1a2e", textfont_size=11); th(fig4)
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.caption("skills_demand.csv not found in data/ folder.")

# ── RAW DATA ──────────────────────────────────────────────────────────────────
with st.expander("Raw data"):
    st.dataframe(df.head(200), use_container_width=True)
    st.download_button("Download filtered CSV", df.to_csv(index=False),
                       "ai_jobs_filtered.csv", "text/csv")

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Built with Streamlit & Plotly &nbsp;&middot;&nbsp;
  <a href="https://www.kaggle.com/datasets/mann14/global-ai-and-data-science-job-market-20202026">
    Global AI & DS Job Market 2020–2026
  </a>
</div>
""", unsafe_allow_html=True)
