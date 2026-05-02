# ═══════════════════════════════════════════════════════════════════════════
#   DELIVERY CONFIGURATION  — Edit this file to change server location
# ═══════════════════════════════════════════════════════════════════════════
#
#  HOW TO CHANGE LOCATION BEFORE YOUR COLLEGE DEMO:
#  1. Open this file.
#  2. Update SERVER_LAT and SERVER_LNG to your college's GPS coordinates.
#     → Go to Google Maps → right-click your location → copy coordinates.
#  3. Save the file and restart the Flask server.  That's it!
#
# ═══════════════════════════════════════════════════════════════════════════

# ── Restaurant / Server Location ──────────────────────────────────────────
# Current: Bhaskar Mali Chawk, Bhiwandi, Maharashtra, India
SERVER_LAT = 19.081370206748694   # ← change to college latitude  e.g. 19.0760
SERVER_LNG = 72.88860538053606   # ← change to college longitude e.g. 72.8777

# ── Delivery Limits ───────────────────────────────────────────────────────
MAX_DELIVERY_KM = 100        # Orders beyond this distance are rejected

# ── Time Components (minutes) ─────────────────────────────────────────────
FIXED_PREP_TIME  = 20       # Kitchen preparation time
TRAVEL_PER_KM    = 3        # 3 min/km  →  ~20 km/h average city speed
HANDOFF_BUFFER   = 5        # Driver finding house / parking
