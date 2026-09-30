import streamlit as st
import json
import os
from datetime import datetime, date, time

# ============================================================
# ANIME NEXUS — PROFESSIONAL STREAMLIT EDITION
# ============================================================

DATA_FILE = "anime_nexus_data.json"

# ------------------------- PAGE ------------------------------
st.set_page_config(
    page_title="Anime Nexus — Ultimate Anime Manager",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------- THEME -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 5%, rgba(139,92,246,.13), transparent 25%),
        radial-gradient(circle at 10% 80%, rgba(34,211,238,.06), transparent 25%),
        #080812;
    color: #E2E8F0;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D0D1A 0%, #090914 100%);
    border-right: 1px solid rgba(139,92,246,.16);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.4rem;
}

.brand {
    padding: 8px 8px 24px 8px;
    border-bottom: 1px solid rgba(255,255,255,.06);
    margin-bottom: 18px;
}

.brand-icon {
    color: #EC4899;
    font-size: 34px;
    font-weight: 800;
    vertical-align: middle;
}

.brand-name {
    color: #F8FAFC;
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 1px;
}

.brand-sub {
    color: #22D3EE;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 5px;
    margin-left: 42px;
}

.section-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 8px 0 8px 4px;
}

.hero {
    background:
        linear-gradient(135deg, rgba(139,92,246,.22), rgba(236,72,153,.08)),
        #111120;
    border: 1px solid rgba(139,92,246,.22);
    border-radius: 22px;
    padding: 28px 30px;
    margin-bottom: 20px;
    box-shadow: 0 18px 50px rgba(0,0,0,.22);
}

.hero h1 {
    margin: 0;
    color: #F8FAFC;
    font-size: 34px;
    font-weight: 800;
}

.hero p {
    margin: 7px 0 0;
    color: #94A3B8;
}

.stat {
    background: linear-gradient(145deg, #171729, #111120);
    border: 1px solid rgba(255,255,255,.055);
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 10px 30px rgba(0,0,0,.16);
}

.stat-icon { font-size: 24px; }
.stat-value {
    color: #F8FAFC;
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}
.stat-title {
    color: #94A3B8;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.card {
    background: #171729;
    border: 1px solid rgba(255,255,255,.055);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,.12);
}

.anime-card {
    background: linear-gradient(145deg, #171729, #111120);
    border: 1px solid rgba(255,255,255,.055);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 12px;
}

.avatar {
    width: 58px;
    height: 58px;
    border-radius: 16px;
    background: linear-gradient(135deg, #8B5CF6, #EC4899);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
    font-weight: 800;
    box-shadow: 0 8px 25px rgba(139,92,246,.22);
}

.anime-title {
    color: #F8FAFC;
    font-size: 18px;
    font-weight: 800;
}

.muted { color: #94A3B8; font-size: 12px; }
.cyan { color: #22D3EE; }
.green { color: #22C55E; }
.pink { color: #EC4899; }
.purple { color: #8B5CF6; }
.yellow { color: #FACC15; }

.mission {
    background: #171729;
    border: 1px solid rgba(34,211,238,.10);
    border-radius: 18px;
    padding: 20px;
    min-height: 260px;
}

.schedule-row {
    background: #171729;
    border: 1px solid rgba(255,255,255,.05);
    border-radius: 15px;
    padding: 16px 20px;
    margin-bottom: 9px;
}

.time {
    color: #22D3EE;
    font-size: 16px;
    font-weight: 800;
}

.badge {
    display: inline-block;
    padding: 4px 9px;
    border-radius: 999px;
    background: rgba(139,92,246,.14);
    color: #C4B5FD;
    font-size: 10px;
    font-weight: 700;
}

div[data-testid="stButton"] > button {
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,.08);
    background: #1D1D32;
    color: #E2E8F0;
    font-weight: 700;
    transition: .2s;
}

div[data-testid="stButton"] > button:hover {
    border-color: #8B5CF6;
    color: #FFFFFF;
    background: #241A45;
}

div[data-testid="stFormSubmitButton"] > button {
    border-radius: 10px;
    background: linear-gradient(90deg, #8B5CF6, #EC4899);
    color: white;
    border: 0;
    font-weight: 800;
}

div[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #8B5CF6, #22D3EE);
}

[data-testid="stMetric"] {
    background: #171729;
    border: 1px solid rgba(255,255,255,.05);
    padding: 14px;
    border-radius: 15px;
}

hr { border-color: rgba(255,255,255,.07); }

footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ------------------------- DATA ------------------------------

def default_data():
    today = datetime.now().strftime("%d-%m-%Y")
    return [
        {
            "anime": "Solo Leveling",
            "episode": 18,
            "total": 25,
            "status": "Watching",
            "genre": "Action",
            "priority": "High",
            "favorite": True,
            "date": today,
            "time": "20:00",
            "completed": False,
        },
        {
            "anime": "One Piece",
            "episode": 1150,
            "total": 1200,
            "status": "Watching",
            "genre": "Adventure",
            "priority": "High",
            "favorite": True,
            "date": today,
            "time": "21:00",
            "completed": False,
        },
        {
            "anime": "Demon Slayer",
            "episode": 12,
            "total": 12,
            "status": "Completed",
            "genre": "Action",
            "priority": "Medium",
            "favorite": False,
            "date": today,
            "time": "22:00",
            "completed": True,
        },
    ]


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except Exception:
            pass
    data = default_data()
    save_data(data)
    return data


def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as exc:
        st.error(f"Could not save data: {exc}")


if "anime_list" not in st.session_state:
    st.session_state.anime_list = load_data()

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


def persist():
    save_data(st.session_state.anime_list)


def go(page):
    st.session_state.page = page


# ------------------------- SIDEBAR ---------------------------

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <span class="brand-icon">✦</span>
        <span class="brand-name">ANIME</span>
        <div class="brand-sub">N E X U S</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">MAIN MENU</div>', unsafe_allow_html=True)

    pages = [
        ("⌂", "Dashboard"),
        ("▶", "Watchlist"),
        ("◷", "Schedule"),
        ("★", "Favorites"),
        ("✓", "Completed"),
    ]

    for icon, name in pages:
        if st.button(
            f"{icon}   {name}",
            key=f"nav_{name}",
            use_container_width=True,
            type="primary" if st.session_state.page == name else "secondary",
        ):
            go(name)
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center;">
        <div class="purple" style="font-weight:800;font-size:11px;">ANIME NEXUS</div>
        <div class="muted">Your anime. Your journey.</div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(f"Last saved: {datetime.now().strftime('%d %b %Y • %I:%M %p')}")


# ------------------------- HELPERS ---------------------------

def progress_for(anime):
    total = int(anime.get("total", 0) or 0)
    episode = int(anime.get("episode", 0) or 0)
    if total <= 0:
        return 0
    return min(max(episode / total, 0), 1)


def delete_anime(index):
    name = st.session_state.anime_list[index]["anime"]
    st.session_state.anime_list.pop(index)
    persist()
    st.toast(f"Removed {name}", icon="🗑️")


def increase_episode(index):
    anime = st.session_state.anime_list[index]
    if anime["episode"] < anime["total"]:
        anime["episode"] += 1
        if anime["episode"] >= anime["total"]:
            anime["completed"] = True
            anime["status"] = "Completed"
        persist()
        st.toast(f"{anime['anime']} → Episode {anime['episode']}", icon="▶️")
    else:
        st.toast("Already at the final episode.", icon="✓")


def mark_completed(index):
    anime = st.session_state.anime_list[index]
    anime["completed"] = True
    anime["status"] = "Completed"
    if anime["total"] > 0:
        anime["episode"] = anime["total"]
    persist()
    st.toast(f"{anime['anime']} completed!", icon="🏆")


def toggle_favorite(index):
    anime = st.session_state.anime_list[index]
    anime["favorite"] = not anime["favorite"]
    persist()


# ------------------------- HEADER ----------------------------

page = st.session_state.page
now = datetime.now()

st.markdown(f"""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
    <div>
        <div style="font-size:30px;font-weight:800;color:#F8FAFC;">{page}</div>
        <div class="muted">Anime Nexus • Ultimate Anime Manager</div>
    </div>
    <div style="color:#22D3EE;font-weight:700;font-size:12px;text-align:right;">
        {now.strftime("%A")}<br>
        {now.strftime("%d %B %Y • %I:%M:%S %p")}
    </div>
</div>
""", unsafe_allow_html=True)


# ========================= DASHBOARD ========================

if page == "Dashboard":
    data = st.session_state.anime_list
    total = len(data)
    watching = sum(1 for a in data if a["status"] == "Watching")
    completed = sum(1 for a in data if a["completed"])
    favorites = sum(1 for a in data if a["favorite"])

    st.markdown("""
    <div class="hero">
        <h1>✦ Welcome to Anime Nexus</h1>
        <p>Track your anime journey, schedule your episodes, and never lose your progress.</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    stats = [
        ("◈", total, "TOTAL ANIME", "purple"),
        ("▶", watching, "CURRENTLY WATCHING", "cyan"),
        ("✓", completed, "COMPLETED", "green"),
        ("★", favorites, "FAVORITES", "pink"),
    ]

    for col, (icon, value, title, color) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat">
                <div class="{color} stat-icon">{icon}</div>
                <div class="stat-value">{value}</div>
                <div class="stat-title">{title}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("""
        <div class="card">
            <div style="font-size:18px;font-weight:800;color:#F8FAFC;">CONTINUE WATCHING</div>
            <div class="muted">Pick up where your anime journey stopped.</div>
        </div>
        """, unsafe_allow_html=True)

        watching_items = [
            a for a in data
            if a["status"] == "Watching" and not a["completed"]
        ]

        if not watching_items:
            st.info("No anime currently being watched.")
        else:
            for anime in watching_items[:5]:
                pct = progress_for(anime)
                st.markdown(f"""
                <div class="anime-card">
                    <div style="display:flex;gap:15px;align-items:center;">
                        <div class="avatar">{anime['anime'][:1].upper()}</div>
                        <div style="flex:1;">
                            <div class="anime-title">{anime['anime']}</div>
                            <div class="muted">Episode {anime['episode']} / {anime['total']} • {anime['genre']}</div>
                        </div>
                        <div class="cyan" style="font-weight:800;">{int(pct*100)}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(pct)

    with right:
        st.markdown("""
        <div class="card">
            <div style="font-size:18px;font-weight:800;color:#F8FAFC;">TODAY'S MISSION</div>
            <div class="muted">Your anime schedule for today.</div>
        </div>
        """, unsafe_allow_html=True)

        today_str = now.strftime("%d-%m-%Y")
        today_items = [a for a in data if a.get("date") == today_str]
        today_items.sort(key=lambda x: x.get("time", "99:99"))

        if not today_items:
            st.info("✦ No anime scheduled today.")
        else:
            for anime in today_items[:5]:
                st.markdown(f"""
                <div class="schedule-row">
                    <div style="display:flex;align-items:center;gap:18px;">
                        <div class="time">{anime['time']}</div>
                        <div>
                            <div class="anime-title" style="font-size:15px;">{anime['anime']}</div>
                            <div class="muted">Episode {anime['episode']} • {anime['genre']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.write("")
    st.caption("Tip: Use the Watchlist page to add anime and update episodes.")


# ========================= WATCHLIST ========================

elif page == "Watchlist":
    st.markdown("""
    <div class="hero">
        <h1>📺 Anime Watchlist</h1>
        <p>Manage every anime you're watching or planning to watch.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("＋ ADD NEW ANIME", expanded=False):
        with st.form("add_anime_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                anime_name = st.text_input("Anime Name", placeholder="e.g. Attack on Titan")
                current_episode = st.number_input("Current Episode", min_value=0, value=1, step=1)
                total_episodes = st.number_input("Total Episodes", min_value=1, value=12, step=1)
                genre = st.text_input("Genre", value="Action")
            with c2:
                selected_date = st.date_input("Reminder Date", value=date.today())
                reminder_time = st.time_input("Reminder Time", value=time(20, 0))
                priority = st.selectbox("Priority", ["Low", "Medium", "High"])
                favorite = st.checkbox("Add to Favorites")

            submitted = st.form_submit_button("＋ ADD TO WATCHLIST", use_container_width=True)

            if submitted:
                if not anime_name.strip():
                    st.error("Please enter an anime name.")
                else:
                    ep = int(current_episode)
                    total = int(total_episodes)
                    item = {
                        "anime": anime_name.strip(),
                        "episode": min(ep, total),
                        "total": total,
                        "status": "Completed" if ep >= total else "Watching",
                        "genre": genre.strip() or "Unknown",
                        "priority": priority,
                        "favorite": favorite,
                        "date": selected_date.strftime("%d-%m-%Y"),
                        "time": reminder_time.strftime("%H:%M"),
                        "completed": ep >= total,
                    }
                    st.session_state.anime_list.append(item)
                    persist()
                    st.success(f"{anime_name.strip()} added to your watchlist!")
                    st.rerun()

    query = st.text_input("🔎 Search anime", placeholder="Search by anime name...")
    status_filter = st.selectbox("Filter", ["All", "Watching", "Completed", "Favorites"])

    filtered = []
    for index, anime in enumerate(st.session_state.anime_list):
        if query.strip().lower() not in anime["anime"].lower():
            continue
        if status_filter == "Watching" and anime["status"] != "Watching":
            continue
        if status_filter == "Completed" and not anime["completed"]:
            continue
        if status_filter == "Favorites" and not anime["favorite"]:
            continue
        filtered.append((index, anime))

    st.caption(f"{len(filtered)} anime shown")

    if not filtered:
        st.info("No anime matches your search/filter.")
    else:
        for index, anime in filtered:
            pct = progress_for(anime)

            st.markdown('<div class="anime-card">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns([0.7, 3.8, 1.8])

            with c1:
                st.markdown(
                    f'<div class="avatar">{anime["anime"][:1].upper()}</div>',
                    unsafe_allow_html=True,
                )

            with c2:
                fav = " ★" if anime["favorite"] else ""
                st.markdown(
                    f'<div class="anime-title">{anime["anime"]}{fav}</div>'
                    f'<div class="muted">{anime["genre"]} • {anime["status"]} • '
                    f'{anime["priority"]} priority</div>'
                    f'<div class="cyan" style="font-weight:700;margin-top:7px;">'
                    f'Episode {anime["episode"]} / {anime["total"]} • {int(pct*100)}%</div>',
                    unsafe_allow_html=True,
                )
                st.progress(pct)

            with c3:
                b1, b2 = st.columns(2)
                with b1:
                    if st.button("+ EP", key=f"ep_{index}", use_container_width=True):
                        increase_episode(index)
                        st.rerun()
                    if st.button("✓ Complete", key=f"complete_{index}", use_container_width=True):
                        mark_completed(index)
                        st.rerun()
                with b2:
                    if st.button(
                        "★" if anime["favorite"] else "☆",
                        key=f"fav_{index}",
                        use_container_width=True,
                    ):
                        toggle_favorite(index)
                        st.rerun()
                    if st.button("✕ Delete", key=f"del_{index}", use_container_width=True):
                        delete_anime(index)
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)


# ========================= SCHEDULE =========================

elif page == "Schedule":
    data = sorted(
        st.session_state.anime_list,
        key=lambda x: (x.get("date", ""), x.get("time", "99:99")),
    )

    st.markdown("""
    <div class="hero">
        <h1>◷ Anime Schedule</h1>
        <p>Keep your watch sessions organized by date and time.</p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.date_input("View schedule for", value=date.today())
    selected_str = selected.strftime("%d-%m-%Y")

    scheduled = [a for a in data if a.get("date") == selected_str]

    if not scheduled:
        st.info("No anime scheduled for this date.")
    else:
        for anime in scheduled:
            completed_badge = "✓ Completed" if anime["completed"] else "▶ Watching"
            st.markdown(f"""
            <div class="schedule-row">
                <div style="display:flex;align-items:center;gap:20px;">
                    <div class="time">{anime['time']}</div>
                    <div style="flex:1;">
                        <div class="anime-title">{anime['anime']}</div>
                        <div class="muted">Episode {anime['episode']} • {anime['genre']}</div>
                    </div>
                    <div class="badge">{completed_badge}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔔 Reminder Status")
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M")

    due = [
        a for a in st.session_state.anime_list
        if a.get("date") == current_date
        and a.get("time") == current_time
        and not a.get("completed")
    ]

    if due:
        for anime in due:
            st.warning(
                f"🔔 **Time to continue {anime['anime']}!** "
                f"Episode {anime['episode']} is scheduled now."
            )
    else:
        st.success("No reminder is due at this exact minute.")

    st.caption(
        "Streamlit reminders appear when the app is running/refreshed. "
        "They are web-app notifications, not Windows desktop popups."
    )


# ========================= FAVORITES ========================

elif page == "Favorites":
    favorites = [
        (i, a) for i, a in enumerate(st.session_state.anime_list)
        if a["favorite"]
    ]

    st.markdown("""
    <div class="hero">
        <h1>★ Favorite Anime</h1>
        <p>Your personal collection of anime you never want to lose.</p>
    </div>
    """, unsafe_allow_html=True)

    if not favorites:
        st.info("★ No favorite anime yet. Add one from the Watchlist.")
    else:
        for index, anime in favorites:
            pct = progress_for(anime)
            st.markdown(f"""
            <div class="anime-card">
                <div style="display:flex;align-items:center;gap:18px;">
                    <div style="font-size:30px;color:#FACC15;">★</div>
                    <div style="flex:1;">
                        <div class="anime-title">{anime['anime']}</div>
                        <div class="muted">{anime['genre']} • {anime['status']}</div>
                        <div class="cyan" style="margin-top:6px;font-weight:700;">
                            Episode {anime['episode']} / {anime['total']} • {int(pct*100)}%
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(pct)
            if st.button("☆ Remove Favorite", key=f"remove_fav_{index}"):
                toggle_favorite(index)
                st.rerun()


# ========================= COMPLETED ========================

elif page == "Completed":
    completed = [
        a for a in st.session_state.anime_list
        if a["completed"]
    ]

    st.markdown("""
    <div class="hero">
        <h1>✓ Completed Anime</h1>
        <p>Your finished anime journey, all in one place.</p>
    </div>
    """, unsafe_allow_html=True)

    if not completed:
        st.info("✓ No completed anime yet.")
    else:
        for anime in completed:
            st.markdown(f"""
            <div class="anime-card">
                <div style="display:flex;align-items:center;gap:18px;">
                    <div style="font-size:30px;color:#22C55E;">✓</div>
                    <div style="flex:1;">
                        <div class="anime-title">{anime['anime']}</div>
                        <div class="muted">
                            {anime['total']} episodes • {anime['genre']} •
                            Priority: {anime['priority']}
                        </div>
                    </div>
                    <div class="green" style="font-weight:800;">COMPLETED</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ------------------------- FOOTER ----------------------------

st.markdown("""
<div style="text-align:center;padding:30px 0 10px;color:#475569;font-size:10px;">
    ANIME NEXUS • Built with Python + Streamlit
</div>
""", unsafe_allow_html=True)
