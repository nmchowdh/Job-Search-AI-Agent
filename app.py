import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Job Search AI Agent",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Demo records only. Replace this list with results from your search_jobs() tool
# when you connect the project to a real job-listings API.
JOBS = [
    {"title": "Junior Python Developer", "company": "Northstar Labs", "location": "Remote", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 92, "posted": "2026-10-02", "source": "Demo data"},
    {"title": "AI Engineer Intern", "company": "BrightPath AI", "location": "USA", "type": "Internship", "field": "AI / ML", "level": "Internship", "match": 89, "posted": "2026-10-04", "source": "Demo data"},
    {"title": "Data Analyst", "company": "Cactus Analytics", "location": "Phoenix", "type": "Full-time", "field": "Data", "level": "Entry level", "match": 86, "posted": "2026-10-01", "source": "Demo data"},
    {"title": "Python Automation Assistant", "company": "Orbit Systems", "location": "Remote", "type": "Contract", "field": "Software", "level": "Entry level", "match": 84, "posted": "2026-10-05", "source": "Demo data"},
    {"title": "Machine Learning Intern", "company": "SignalForge", "location": "USA", "type": "Internship", "field": "AI / ML", "level": "Internship", "match": 83, "posted": "2026-10-06", "source": "Demo data"},
    {"title": "Junior QA Engineer", "company": "Copper Cloud", "location": "Phoenix", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 78, "posted": "2026-09-29", "source": "Demo data"},
    {"title": "Reporting Analyst", "company": "Mesa Metrics", "location": "Remote", "type": "Full-time", "field": "Data", "level": "Entry level", "match": 81, "posted": "2026-10-03", "source": "Demo data"},
    {"title": "AI Research Assistant", "company": "Blue Mesa AI", "location": "USA", "type": "Internship", "field": "AI / ML", "level": "Internship", "match": 77, "posted": "2026-09-28", "source": "Demo data"},
    {"title": "Backend Developer I", "company": "Juniper Apps", "location": "Remote", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 88, "posted": "2026-10-07", "source": "Demo data"},
    {"title": "Business Data Assistant", "company": "Desert Ledger", "location": "Phoenix", "type": "Part-time", "field": "Data", "level": "Entry level", "match": 74, "posted": "2026-09-25", "source": "Demo data"},
    {"title": "AI Product Intern", "company": "Lumen Works", "location": "Remote", "type": "Internship", "field": "AI / ML", "level": "Internship", "match": 80, "posted": "2026-10-08", "source": "Demo data"},
    {"title": "Python Developer Intern", "company": "Redstone Tech", "location": "USA", "type": "Internship", "field": "Software", "level": "Internship", "match": 85, "posted": "2026-10-06", "source": "Demo data"},
    {"title": "Data Quality Associate", "company": "Sunline Data", "location": "Remote", "type": "Contract", "field": "Data", "level": "Entry level", "match": 72, "posted": "2026-09-22", "source": "Demo data"},
    {"title": "AI Support Engineer", "company": "Kiteframe", "location": "Phoenix", "type": "Full-time", "field": "AI / ML", "level": "Entry level", "match": 76, "posted": "2026-10-02", "source": "Demo data"},
    {"title": "Software Engineer Trainee", "company": "Pioneer Digital", "location": "USA", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 79, "posted": "2026-09-30", "source": "Demo data"},
    {"title": "Junior BI Analyst", "company": "Prism North", "location": "Remote", "type": "Full-time", "field": "Data", "level": "Entry level", "match": 87, "posted": "2026-10-09", "source": "Demo data"},
    {"title": "Generative AI Intern", "company": "Morrow AI", "location": "USA", "type": "Internship", "field": "AI / ML", "level": "Internship", "match": 91, "posted": "2026-10-10", "source": "Demo data"},
    {"title": "Application Support Analyst", "company": "Canyon Software", "location": "Phoenix", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 70, "posted": "2026-09-20", "source": "Demo data"},
    {"title": "Data Operations Intern", "company": "Clearview Data", "location": "Remote", "type": "Internship", "field": "Data", "level": "Internship", "match": 75, "posted": "2026-10-01", "source": "Demo data"},
    {"title": "AI Workflow Assistant", "company": "Evergreen Logic", "location": "Remote", "type": "Contract", "field": "AI / ML", "level": "Entry level", "match": 82, "posted": "2026-10-05", "source": "Demo data"},
    {"title": "Python QA Intern", "company": "Copperleaf Apps", "location": "USA", "type": "Internship", "field": "Software", "level": "Internship", "match": 73, "posted": "2026-09-26", "source": "Demo data"},
    {"title": "Operations Data Analyst", "company": "Saguaro Insights", "location": "Phoenix", "type": "Full-time", "field": "Data", "level": "Entry level", "match": 90, "posted": "2026-10-08", "source": "Demo data"},
    {"title": "ML Data Labeling Associate", "company": "Atlas Signals", "location": "Remote", "type": "Part-time", "field": "AI / ML", "level": "Entry level", "match": 68, "posted": "2026-09-18", "source": "Demo data"},
    {"title": "Junior API Developer", "company": "Westwind Tech", "location": "Remote", "type": "Full-time", "field": "Software", "level": "Entry level", "match": 93, "posted": "2026-10-10", "source": "Demo data"},
]

df = pd.DataFrame(JOBS)
df["posted"] = pd.to_datetime(df["posted"])

st.title("🔎 Job Search AI Agent")
st.subheader("Find promising entry-level roles. Compare matches. Focus your next application.")
st.caption("Interactive dashboard • Sample listings are fictional demo data, not live vacancies.")

with st.sidebar:
    st.header("Filter jobs")
    search_text = st.text_input("Search title or company", placeholder="e.g. Python")
    chosen_fields = st.multiselect("Career area", sorted(df["field"].unique()), default=sorted(df["field"].unique()))
    chosen_locations = st.multiselect("Location", sorted(df["location"].unique()), default=sorted(df["location"].unique()))
    chosen_types = st.multiselect("Job type", sorted(df["type"].unique()), default=sorted(df["type"].unique()))
    min_match = st.slider("Minimum AI match score", 0, 100, 65, 5)
    st.caption("The match score is illustrative demo data, not a validated prediction.")

filtered = df[
    df["field"].isin(chosen_fields)
    & df["location"].isin(chosen_locations)
    & df["type"].isin(chosen_types)
    & (df["match"] >= min_match)
]
if search_text.strip():
    term = search_text.strip().lower()
    filtered = filtered[
        filtered["title"].str.lower().str.contains(term, na=False)
        | filtered["company"].str.lower().str.contains(term, na=False)
    ]

total = len(filtered)
avg_match = round(filtered["match"].mean()) if total else 0
remote_count = int((filtered["location"] == "Remote").sum()) if total else 0
entry_count = int((filtered["level"] == "Entry level").sum()) if total else 0

m1, m2, m3, m4 = st.columns(4)
m1.metric("Matching listings", total)
m2.metric("Average match score", f"{avg_match}%" if total else "—")
m3.metric("Remote roles", remote_count)
m4.metric("Entry-level roles", entry_count)

st.divider()
left, right = st.columns(2)

with left:
    st.markdown("### 1. Listings by career area")
    if total:
        area_counts = filtered["field"].value_counts().rename_axis("Career area").reset_index(name="Listings")
        fig = px.bar(area_counts, x="Career area", y="Listings", color="Career area",
                     hover_data={"Listings": True}, title=None)
        fig.update_layout(showlegend=False, margin=dict(l=8, r=8, t=12, b=8))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No jobs match these filters.")
    st.caption("Takeaway: This shows which career areas have the most listings in the current filtered sample.")

with right:
    st.markdown("### 2. AI match-score distribution")
    if total:
        fig = px.histogram(filtered, x="match", nbins=8, labels={"match": "Match score (%)"},
                           hover_data=["title", "field"], title=None)
        fig.update_layout(margin=dict(l=8, r=8, t=12, b=8))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No jobs match these filters.")
    st.caption("Takeaway: Hover over score ranges to explore how closely the sample listings match the selected threshold.")

left, right = st.columns(2)
with left:
    st.markdown("### 3. Location mix")
    if total:
        loc_counts = filtered["location"].value_counts().rename_axis("Location").reset_index(name="Listings")
        fig = px.pie(loc_counts, names="Location", values="Listings", hole=0.45,
                     hover_data={"Listings": True}, title=None)
        fig.update_layout(margin=dict(l=8, r=8, t=12, b=8), legend_title_text="Location")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No jobs match these filters.")
    st.caption("Takeaway: Compare remote, Phoenix, and broader USA listings in the filtered sample.")

with right:
    st.markdown("### 4. Match score by job type")
    if total:
        fig = px.box(filtered, x="type", y="match", color="type",
                     points="all", hover_data=["title", "company", "location"],
                     labels={"type": "Job type", "match": "Match score (%)"}, title=None)
        fig.update_layout(showlegend=False, margin=dict(l=8, r=8, t=12, b=8))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No jobs match these filters.")
    st.caption("Takeaway: Compare the spread of illustrative match scores across job types; hover for individual listings.")

st.divider()
st.markdown("### Matching jobs")
if total:
    display = filtered.copy()
    display["posted"] = display["posted"].dt.strftime("%b %d, %Y")
    st.dataframe(
        display[["title", "company", "location", "type", "field", "level", "match", "posted"]]
        .rename(columns={"match": "AI match (%)", "field": "Career area", "level": "Experience level", "posted": "Demo posted date"}),
        use_container_width=True,
        hide_index=True,
    )
    st.download_button(
        "Download filtered jobs as CSV",
        data=display.to_csv(index=False).encode("utf-8"),
        file_name="filtered_demo_jobs.csv",
        mime="text/csv",
    )
else:
    st.warning("No listings match the current filters. Try lowering the minimum match score or broadening your selections.")

with st.expander("Data notes: sample size and exclusions"):
    st.markdown(
        f"""
- **Sample size:** This dashboard contains **{len(df)} fictional demo listings** in total. Treat any pattern as illustrative only; for stable real-world comparisons, aim for at least **30 relevant listings overall** and preferably **10 or more per group**. These are practical guidelines, not guarantees of statistical validity.
- **Not explored:** salary/pay, benefits, employer legitimacy, application outcomes, hiring rates, duplicate listings, job-description skill extraction, posting freshness beyond the demo date, and actual labor-market trends.
- **Important limitation:** the match scores, companies, listings, and dates are mock values. No live job API is connected, and this dashboard does not submit applications.
"""
    )

st.caption("Next integration point: replace the JOBS demo list with the list returned by your existing search_jobs(query) function.")
