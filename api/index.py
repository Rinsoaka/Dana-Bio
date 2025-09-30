# This file serves as the Serverless Function entry point for Vercel.
from flask import Flask, render_template_string

# --- Application Data ---
SKILLS = [
    {"icon": "🐍", "name": "Python", "level": 50},
    {"icon": "🟩", "name": "JavaScript", "level": 70},
    {"icon": "🛡️", "name": "HTML/CSS", "level": 85},
    {"icon": "✈️", "name": "Telegram Bots", "level": 80},
    {"icon": "🌐", "name": "Web Dev", "level": 75},
    {"icon": "🔎", "name": "Config & Checks", "level": 65},
    {"icon": "🕷️", "name": "Web Pentesting (legal)", "level": 60},
    {"icon": "☁️", "name": "Cloud Breach & Hardening", "level": 62},
    {"icon": "🔌", "name": "Hardware Hacking (legal)", "level": 55},
    {"icon": "🗄️", "name": "SQL Testing", "level": 58},
    {"icon": "📱", "name": "Android Security", "level": 52},
    {"icon": "🧪", "name": "Exploit Research (defensive)", "level": 50, "accent": "danger"},
]

SOCIALS = [
    {"icon": "💬", "name": "Telegram", "url": "https://t.me/dana_17z"},
    {"icon": "📘", "name": "Facebook", "url": "https://www.facebook.com/share/1Zm64EXzAf/"},
    {"icon": "🐙", "name": "GitHub", "url": "https://github.com/dana-lps"},
]

# TEMPLATE is the complete HTML/CSS structure embedded here.
# NOTE: Using a raw string (r''') to safely handle the backslashes in the template.
TEMPLATE = r'''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>DASOP // Skills Bio 2023–2025</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #071013;
      --neon: #3dff86;
      --neon-dim: #1bf06a;
      --text: #d7ffe6;
      --muted: #6cd49a;
      --danger: #ff4d6d;
    }
    * { box-sizing: border-box }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: "JetBrains Mono", ui-monospace, monospace;
      color: var(--text);
      background: #000;
    }
    .wrap { max-width: 1120px; margin: 40px auto; padding: 0 20px; }
    .title {
      font-weight: 800; font-size: clamp(24px, 4vw, 42px);
      color: var(--neon);
      text-shadow: 0 0 5px var(--neon),0 0 10px var(--neon),0 0 20px var(--neon),0 0 40px var(--neon-dim);
    }
    .title small { display:block; color: var(--muted); font-size:.55em; letter-spacing:2px; text-shadow: 0 0 8px var(--neon); }
    .bar { height: 3px; width: 100%; background: var(--neon); box-shadow:0 0 10px var(--neon),0 0 20px var(--neon); margin: 18px 0 8px; }
    .matrix {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 18px;
      margin-top: 22px;
    }
    .card {
      border: 2px solid var(--neon);
      border-radius: 16px;
      background: rgba(0,0,0,0.3);
      padding: 18px 16px 14px;
      box-shadow: 0 0 10px var(--neon), inset 0 0 15px rgba(61,255,134,.4);
      transition: transform .2s ease, box-shadow .2s ease;
    }
    .card:hover {
      transform: translateY(-6px) scale(1.02);
      box-shadow: 0 0 20px var(--neon), 0 0 40px var(--neon-dim), inset 0 0 25px rgba(61,255,134,.6);
    }
    .card.danger { border-color: var(--danger); box-shadow: 0 0 10px var(--danger); }
    .card.danger:hover { box-shadow: 0 0 20px var(--danger), 0 0 40px #ff9fb1; }
    .card .icon { font-size: 28px; filter: drop-shadow(0 0 6px var(--neon)); }
    .card.danger .icon { filter: drop-shadow(0 0 6px var(--danger)); }
    .card .name { margin-top: 10px; font-weight: 700; letter-spacing: .5px; text-shadow: 0 0 8px var(--neon); }
    .meter { margin-top: 14px; height: 8px; border-radius: 999px; background: rgba(255,255,255,.1); overflow: hidden; }
    .meter > i { display:block; height:100%; width:var(--w); background: var(--neon); box-shadow:0 0 5px var(--neon),0 0 10px var(--neon),0 0 20px var(--neon); }
    .card.danger .meter > i { background: var(--danger); box-shadow:0 0 5px var(--danger),0 0 15px var(--danger); }
    .header {
      display:flex; align-items:center; justify-content:space-between; gap:12px;
      border:1px dashed var(--neon); border-radius:14px; padding:12px 14px;
      background: rgba(61,255,134,.08); box-shadow: 0 0 10px var(--neon);
    }
    .prompt { color: var(--muted); text-shadow: 0 0 6px var(--neon); }
    .tag { color:#000; background: var(--neon); padding:4px 10px; border-radius:999px; font-weight:800; }
    footer { margin-top: 30px; color: #9adcb6; font-size: 12px; letter-spacing: .8px; text-align:center; text-shadow: 0 0 8px var(--neon); }
    .socials { margin-top:40px; text-align:center; }
    .socials h2 { color: var(--neon); text-shadow:0 0 10px var(--neon); margin-bottom:20px; }
    .social-links { display:flex; flex-wrap:wrap; justify-content:center; gap:16px; }
    .social-links a {
      display:inline-flex; align-items:center; gap:8px;
      padding:10px 16px; border-radius:12px;
      color:#000; background: var(--neon); font-weight:700; text-decoration:none;
      box-shadow:0 0 10px var(--neon), 0 0 20px var(--neon);
      transition: transform .2s ease, box-shadow .2s ease;
    }
    .social-links a:hover {
      transform:scale(1.08);
      box-shadow:0 0 20px var(--neon), 0 0 40px var(--neon-dim);
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="title">DASOP // SKILLS BIO <small>2023—2025</small></div>
    <div class="bar"></div>

    <div class="header">
      <div class="prompt">_ SKILL&nbsp;MATRIX</div>
      <div class="tag">ACTIVE</div>
    </div>

    <div class="matrix">
      {% for s in skills %}
        <div class="card {% if s.accent == 'danger' %}danger{% endif %}">
          <div class="icon">{{ s.icon }}</div>
          <div class="name">{{ s.name|upper }}</div>
          <div class="meter"><i style="--w: {{ s.level }}%"></i></div>
        </div>
      {% endfor %}
    </div>

    <div class="socials">
      <h2>CONNECT WITH ME</h2>
      <div class="social-links">
        {% for soc in socials %}
          <a href="{{ soc.url }}" target="_blank">
            <span>{{ soc.icon }}</span> {{ soc.name }}
          </a>
        {% endfor %}
      </div>
    </div>

    <footer>Built for a personal portfolio. Ethical use only ⚡</footer>
  </div>
</body>
</html>
'''

# The standard Flask app instance
app = Flask(__name__)

# The route function is defined as usual
@app.route
("/")
def home():
    # Pass the data to the embedded template string
    return render_template_string(TEMPLATE, skills=SKILLS, socials=SOCIALS)

# IMPORTANT: We remove the 'if __name__ == "__main__":' block
# Vercel will import the 'app' variable directly to run the Serverless Function.
