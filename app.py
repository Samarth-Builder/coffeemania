import streamlit as st

st.set_page_config(
    page_title="Sam's Coffee Bar",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# Coffee recipes
# Amounts are for ONE serving. The app scales them.
# --------------------------------------------------
RECIPES = {
    "Hot Latte": {
        "icon": "🥛",
        "tagline": "Smooth, milky and café-style",
        "coffee_sachets": 1,
        "water_ml": 30,
        "milk_ml": 180,
        "ice": 0,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Empty 1 ₹10 Nescafé sachet into a cup.",
            "Add 30 ml hot water and stir until fully dissolved.",
            "Warm 180 ml Country Delight milk. Do not boil it hard.",
            "Pour the milk slowly into the coffee. Add sugar to taste.",
        ],
        "tip": "Whisk the warm milk for 15–20 seconds for a smoother café-style finish.",
        "strength": "Mild–medium",
        "time": "5 min",
    },
    "Iced Latte": {
        "icon": "🧊",
        "tagline": "Creamy, chilled and easy",
        "coffee_sachets": 1,
        "water_ml": 30,
        "milk_ml": 160,
        "ice": 6,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 30 ml hot water.",
            "Add sugar while the coffee is warm, if desired.",
            "Fill a tall glass with ice and add 160 ml chilled Country Delight milk.",
            "Pour the coffee concentrate over the milk and stir.",
        ],
        "tip": "Use refrigerator-cold Country Delight milk for the cleanest iced-latte taste.",
        "strength": "Mild–medium",
        "time": "3 min",
    },
    "Hot Cappuccino": {
        "icon": "☁️",
        "tagline": "Bold coffee with a foamy top",
        "coffee_sachets": 1,
        "water_ml": 30,
        "milk_ml": 120,
        "ice": 0,
        "sugar": "1 tsp, optional",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 30 ml hot water.",
            "Warm 120 ml Country Delight milk.",
            "Froth or whisk the milk until a good layer of foam forms.",
            "Pour the milk into the coffee and spoon the foam over the top.",
        ],
        "tip": "The extra foam is what gives this a cappuccino-like feel.",
        "strength": "Medium",
        "time": "5 min",
    },
    "Iced Cappuccino": {
        "icon": "❄️",
        "tagline": "Cold, frothy and coffee-forward",
        "coffee_sachets": 1,
        "water_ml": 30,
        "milk_ml": 100,
        "ice": 7,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 30 ml hot water.",
            "Add sugar and stir while warm, if desired.",
            "Froth 100 ml chilled Country Delight milk for 20–30 seconds.",
            "Add ice, pour in the milk and coffee, then finish with the foam.",
        ],
        "tip": "A small handheld frother makes the foam much easier and more consistent.",
        "strength": "Medium",
        "time": "4 min",
    },
    "Espresso-style": {
        "icon": "⚡",
        "tagline": "Small, strong and concentrated",
        "coffee_sachets": 1,
        "water_ml": 35,
        "milk_ml": 0,
        "ice": 0,
        "sugar": "None or ½ tsp",
        "method": [
            "Empty 1 ₹10 Nescafé sachet into a small cup.",
            "Add only about 35 ml hot water.",
            "Stir thoroughly and serve immediately.",
        ],
        "tip": "This is an instant-coffee concentrate, not espresso extracted from an espresso machine.",
        "strength": "Strong",
        "time": "2 min",
    },
    "Americano": {
        "icon": "☕",
        "tagline": "Black coffee, longer and smoother",
        "coffee_sachets": 1,
        "water_ml": 180,
        "milk_ml": 0,
        "ice": 0,
        "sugar": "None or to taste",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in about 30 ml hot water.",
            "Add about 150 ml more hot water.",
            "Stir and taste. Add a little more water if you want it lighter.",
        ],
        "tip": "Start stronger and add water. It is easier to dilute coffee than to make it stronger.",
        "strength": "Medium–strong",
        "time": "2 min",
    },
    "Iced Americano": {
        "icon": "🧊",
        "tagline": "Cold, crisp and refreshing",
        "coffee_sachets": 1,
        "water_ml": 130,
        "milk_ml": 0,
        "ice": 9,
        "sugar": "None or to taste",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 30 ml hot water.",
            "Add 100 ml cold water and stir.",
            "Fill a tall glass with plenty of ice.",
            "Pour the coffee over the ice and serve immediately.",
        ],
        "tip": "Use lots of ice and very cold water for a sharper, more refreshing drink.",
        "strength": "Medium–strong",
        "time": "2 min",
    },
    "Dalgona Coffee": {
        "icon": "🍯",
        "tagline": "Whipped, fluffy and sweet",
        "coffee_sachets": 1,
        "water_ml": 15,
        "milk_ml": 150,
        "ice": 5,
        "sugar": "1 tbsp",
        "method": [
            "Mix 1 ₹10 Nescafé sachet, 1 tbsp sugar and 15 ml hot water in a bowl.",
            "Whisk vigorously for 2–4 minutes until thick and fluffy.",
            "Add ice to a glass and pour in 150 ml chilled Country Delight milk.",
            "Spoon the whipped coffee on top and stir before drinking.",
        ],
        "tip": "A hand mixer or electric frother makes the whipped coffee much faster.",
        "strength": "Medium–strong",
        "time": "5 min",
    },
    "South Indian Filter Coffee": {
        "icon": "🫖",
        "tagline": "Strong, aromatic and classic",
        "coffee_sachets": 0,
        "water_ml": 120,
        "milk_ml": 100,
        "ice": 0,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Use about 2 tsp South Indian filter coffee powder in a coffee filter.",
            "Add about 120 ml hot water to the upper chamber and let the decoction collect.",
            "Warm 100 ml Country Delight milk and add sugar to taste.",
            "Mix about 40–50 ml strong decoction with the hot milk and serve in a steel tumbler or cup.",
        ],
        "tip": "This one is best with proper South Indian filter coffee powder, not instant coffee.",
        "strength": "Strong",
        "time": "8–10 min",
    },
    "Indian Cold Coffee": {
        "icon": "🥤",
        "tagline": "Creamy, sweet and café-style",
        "coffee_sachets": 1,
        "water_ml": 30,
        "milk_ml": 180,
        "ice": 5,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 30 ml hot water.",
            "Add 180 ml chilled Country Delight milk, sugar and ice.",
            "Blend for 15–20 seconds until frothy.",
            "Pour into a tall glass. Add vanilla ice cream on top if you want it richer.",
        ],
        "tip": "For the classic Indian café texture, blend until a light foam forms on top.",
        "strength": "Mild–medium",
        "time": "4 min",
    },
    "Masala Coffee": {
        "icon": "🌿",
        "tagline": "Coffee with an Indian spice twist",
        "coffee_sachets": 1,
        "water_ml": 40,
        "milk_ml": 140,
        "ice": 0,
        "sugar": "1–2 tsp, optional",
        "method": [
            "Dissolve 1 ₹10 Nescafé sachet in 40 ml hot water.",
            "Warm 140 ml Country Delight milk with a tiny pinch of cinnamon and cardamom.",
            "Add sugar to taste and heat gently for 1–2 minutes.",
            "Pour the spiced milk into the coffee and stir well.",
        ],
        "tip": "Go very light on the spices. Coffee should stay the main flavour.",
        "strength": "Medium",
        "time": "5 min",
    },
    "Beaten Coffee": {
        "icon": "🤎",
        "tagline": "Indian-style hand-whipped coffee",
        "coffee_sachets": 1,
        "water_ml": 15,
        "milk_ml": 160,
        "ice": 0,
        "sugar": "1–2 tsp",
        "method": [
            "Mix 1 ₹10 Nescafé sachet with sugar and about 15 ml hot water.",
            "Beat vigorously with a spoon for 2–3 minutes until pale and creamy.",
            "Heat 160 ml Country Delight milk until hot but not boiling.",
            "Add the whipped coffee to a cup and slowly pour in the milk while stirring.",
        ],
        "tip": "This is the quick Indian home-style method often called whipped or beaten coffee.",
        "strength": "Medium–strong",
        "time": "5 min",
    },
}

# --------------------------------------------------
# Helpers
# --------------------------------------------------
import random


import re


def scale_step(text: str, n: int) -> str:
    """Scale every quantity (sachets, ml, tbsp, tsp) in a method step by the number of cups."""
    if n == 1:
        return text

    def mul(num: str) -> str:
        return "–".join(str(int(x) * n) for x in num.split("–"))

    text = re.sub(
        r"(\d+)( ₹10 Nescafé sachet)",
        lambda m: f"{int(m.group(1)) * n}{m.group(2)}s",
        text,
    )
    text = re.sub(r"(\d+(?:–\d+)?)( ?(?:ml|tbsp|tsp)\b)", lambda m: mul(m.group(1)) + m.group(2), text)
    return text.replace("into a cup.", "into a jug or cup.").replace("into a small cup.", "into a small jug or cup.")


def h(s: str) -> str:
    """Flatten HTML so Streamlit's markdown never treats it as a code block."""
    return "".join(line.strip() for line in s.splitlines())


MOODS = {
    "All": list(RECIPES),
    "Hot": [n for n, r in RECIPES.items() if r["ice"] == 0],
    "Cold": [n for n, r in RECIPES.items() if r["ice"] > 0],
    "Strong": [n for n, r in RECIPES.items() if "trong" in r["strength"]],
    "Creamy": [n for n, r in RECIPES.items() if r["milk_ml"] >= 140],
    "Quick": [
        n for n, r in RECIPES.items() if int(r["time"].split()[0].split("–")[0]) <= 3
    ],
}


def surprise_me():
    mood = st.session_state.get("mood") or "All"
    st.session_state["coffee_choice"] = random.choice(MOODS[mood])


def reset_steps():
    for k in [k for k in st.session_state if str(k).startswith("step_")]:
        st.session_state[k] = False


# --------------------------------------------------
# Styling
# --------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap');

html, body, .stApp { font-family: 'Inter', sans-serif; }
.stApp { background: #f4eee6; color: #2a1b14; }
footer { visibility: hidden; }

/* Top bar: Fork + GitHub icon (and Deploy) */
[data-testid="stToolbar"],
[data-testid="stToolbarActions"],
[data-testid="stHeader"],
[data-testid="stDecoration"] { display: none !important; }

/* Bottom corner: creator avatar + Streamlit badge */
[class*="viewerBadge"],
[class*="_profileContainer_"],
[class*="_profilePreview_"],
[class*="_container_gzau3"],
[data-testid="appCreatorAvatar"],
a[href*="streamlit.io/cloud"],
a[href*="share.streamlit.io"] { display: none !important; }
.block-container { max-width: 1060px; padding-top: 1.4rem; padding-bottom: 3rem; }

/* Hero: flat, editorial */
.hero { background:#1f130d; padding:44px 48px 36px; border-radius:4px; margin-bottom:10px; }
.hero-eyebrow { color:#c9a57a; font-size:.7rem; font-weight:600; letter-spacing:.28em; text-transform:uppercase; }
.brand { font-family:'DM Serif Display',Georgia,serif; color:#f7ecda; font-size:clamp(2.8rem,7vw,5.2rem); line-height:1; margin:14px 0 22px; letter-spacing:-.01em; }
.hero-rule { height:1px; background:#4a3324; margin-bottom:16px; }
.hero-meta { display:flex; flex-wrap:wrap; gap:6px 28px; color:#bfa68c; font-size:.74rem; font-weight:500; letter-spacing:.14em; text-transform:uppercase; }

.section-title { display:flex; align-items:baseline; gap:14px; margin:34px 0 10px; }
.section-title span { font-size:.7rem; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:#8a6a52; }
.section-title i { flex:1; height:1px; background:#d9c8b5; }

[data-testid="stWidgetLabel"] p { color:#3a251a !important; font-weight:600; font-size:.8rem; letter-spacing:.12em; text-transform:uppercase; }

/* Mood filter: plain text tabs with underline */
.st-key-mood button { background:transparent !important; border:none !important; border-bottom:2px solid transparent !important; border-radius:0 !important; padding:4px 2px !important; margin-right:14px; color:#8a6a52 !important; font-weight:600 !important; letter-spacing:.06em; text-transform:uppercase; font-size:.78rem !important; }
.st-key-mood button:hover { color:#2a1b14 !important; }
.st-key-mood button[data-testid="stBaseButton-pillsActive"] { color:#2a1b14 !important; border-bottom-color:#6f432a !important; }

/* Drink picker: square outlined buttons, filled when active */
.st-key-coffee_choice button { background:transparent !important; color:#2a1b14 !important; border:1px solid #cdb9a4 !important; border-radius:3px !important; font-weight:500 !important; padding:8px 16px !important; transition:all .12s ease; }
.st-key-coffee_choice button:hover { border-color:#2a1b14 !important; }
.st-key-coffee_choice button[data-testid="stBaseButton-pillsActive"] { background:#1f130d !important; color:#f7ecda !important; border-color:#1f130d !important; }
.st-key-coffee_choice button[data-testid="stBaseButton-pillsActive"] p { color:#f7ecda !important; }

.stButton button { background:transparent; color:#2a1b14; border:1px solid #2a1b14; border-radius:3px; font-weight:600; font-size:.76rem; letter-spacing:.14em; text-transform:uppercase; }
.stButton button:hover { background:#1f130d; color:#f7ecda; border-color:#1f130d; }

/* Recipe card */
.recipe-card { display:grid; grid-template-columns:1.1fr 1fr; gap:48px; background:#fffaf3; border:1px solid #e0d0bf; border-radius:4px; padding:36px 40px; }
.recipe-no { font-size:.7rem; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:#8a6a52; }
.recipe-name { font-family:'DM Serif Display',Georgia,serif; font-size:clamp(2.2rem,4.4vw,3.2rem); line-height:1.02; color:#1f130d; margin:10px 0 8px; }
.recipe-tagline { color:#705443; font-size:1rem; }
.stats { display:grid; grid-template-columns:repeat(3,1fr); margin-top:28px; border-top:1px solid #e0d0bf; }
.stats div { padding:14px 0 0; }
.stats div + div { padding-left:16px; border-left:1px solid #e0d0bf; }
.stats small { display:block; font-size:.64rem; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:#8a6a52; }
.stats b { display:block; margin-top:4px; font-family:'DM Serif Display',Georgia,serif; font-weight:400; font-size:1.3rem; color:#1f130d; }
.mini-heading { font-size:.7rem; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:#8a6a52; padding-bottom:10px; border-bottom:1px solid #2a1b14; }
.ing { display:flex; justify-content:space-between; gap:18px; padding:13px 0; border-bottom:1px solid #eadbca; color:#2a1b14; }
.ing span { color:#8a6a52; font-size:.72rem; font-weight:600; letter-spacing:.16em; text-transform:uppercase; padding-top:3px; }
.ing b { font-weight:500; text-align:right; }
.ing.empty b { color:#b3a090; }

[data-testid="stVerticalBlockBorderWrapper"] { background:#fffaf3; border-color:#e0d0bf !important; border-radius:4px !important; }
[data-testid="stCheckbox"] p { color:#2a1b14 !important; line-height:1.55; text-transform:none; letter-spacing:0; font-size:1rem; font-weight:400; }
[data-testid="stProgress"] div[role="progressbar"] > div { background:#6f432a !important; }

.note { border-left:2px solid #6f432a; padding:2px 0 2px 20px; }
.note small { display:block; font-size:.66rem; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:#8a6a52; margin-bottom:10px; }
.note p { font-family:'DM Serif Display',Georgia,serif; font-size:1.3rem; line-height:1.4; color:#2a1b14; margin:0; }
.footer { text-align:center; color:#8a6a52; font-size:.7rem; letter-spacing:.16em; text-transform:uppercase; margin-top:40px; }

@media (max-width:760px) {
  .hero { padding:30px 22px 24px; }
  .recipe-card { grid-template-columns:1fr; padding:24px 20px; gap:26px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    h(
        """
<div class="hero">
<div class="hero-eyebrow">Home coffee bar · Indian edition</div>
<div class="brand">Sam's Coffee Bar</div>
<div class="hero-rule"></div>
<div class="hero-meta"><span>Nescafé ₹10 sachets</span><span>Country Delight milk</span><span>No machine needed</span></div>
</div>
"""
    ),
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Picker
# --------------------------------------------------
st.markdown('<div class="section-title"><span>The menu</span><i></i></div>', unsafe_allow_html=True)

mood = st.pills(
    "Filter",
    list(MOODS),
    default="All",
    selection_mode="single",
    key="mood",
    label_visibility="collapsed",
) or "All"
options = MOODS[mood]

# Keep the selected coffee valid when the filter changes
if st.session_state.get("coffee_choice") not in options:
    st.session_state["coffee_choice"] = options[0]

selected = st.pills(
    "Coffee menu",
    options,
    selection_mode="single",
    key="coffee_choice",
    label_visibility="collapsed",
) or options[0]
recipe = RECIPES[selected]

c1, c2 = st.columns([3, 1], vertical_alignment="bottom")
with c1:
    servings = st.slider("How many cups?", 1, 6, 1, help="Scales every ingredient for you.")
with c2:
    st.button("Random pick", on_click=surprise_me, use_container_width=True)

# --------------------------------------------------
# Scaled recipe card (single HTML block so the layout is reliable)
# --------------------------------------------------
sachets = recipe["coffee_sachets"] * servings
water = recipe["water_ml"] * servings
milk = recipe["milk_ml"] * servings
ice = recipe["ice"] * servings

if sachets:
    coffee_text = f"{sachets} × ₹10 Nescafé sachet{'s' if sachets != 1 else ''}"
else:
    coffee_text = f"~{2 * servings} tsp South Indian filter powder"

rows = [
    ("Coffee", coffee_text, True),
    ("Water", f"{water} ml", True),
    ("Milk", f"{milk} ml Country Delight" if milk else "None", bool(milk)),
    ("Ice", f"About {ice} cubes" if ice else "None", bool(ice)),
    ("Sweetness", recipe["sugar"], True),
]
ing_html = "".join(
    f'<div class="ing{"" if on else " empty"}"><span>{label}</span><b>{value}</b></div>'
    for label, value, on in rows
)

st.markdown('<div class="section-title"><span>Your brew</span><i></i></div>', unsafe_allow_html=True)
st.markdown(
    h(
        f"""
<div class="recipe-card">
<div>
<div class="recipe-no">No. {list(RECIPES).index(selected) + 1:02d}</div>
<div class="recipe-name">{selected}</div>
<div class="recipe-tagline">{recipe['tagline']}</div>
<div class="stats">
<div><small>Strength</small><b>{recipe['strength']}</b></div>
<div><small>Ready in</small><b>{recipe['time']}</b></div>
<div><small>Cups</small><b>{servings}</b></div>
</div>
</div>
<div>
<div class="mini-heading">Ingredients</div>
{ing_html}
</div>
</div>
"""
    ),
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Method as an interactive checklist
# --------------------------------------------------
st.markdown('<div class="section-title"><span>Method</span><i></i></div>', unsafe_allow_html=True)

left, right = st.columns([1.6, 1], gap="large")

with left:
    with st.container(border=True):
        done = 0
        for i, step in enumerate(recipe["method"], start=1):
            if st.checkbox(f"**{i}.** {scale_step(step, servings)}", key=f"step_{selected}_{i}"):
                done += 1
        total = len(recipe["method"])
        st.progress(done / total, text=f"{done} of {total} steps done")
        if done == total:
            st.success("Your coffee is ready.", icon=":material/check_circle:")
        st.button("Reset steps", on_click=reset_steps, key="reset_btn")

with right:
    st.markdown(
        h(
            f"""
<div class="note"><small>Bar note</small><p>{recipe['tip']}</p></div>
"""
        ),
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer">Start with the recipe · then adjust sweetness, strength and milk to taste</div>',
    unsafe_allow_html=True,
)