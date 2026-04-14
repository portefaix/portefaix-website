#!/usr/bin/env python3
"""Portefaix Platform Architecture Diagram - Style 1: Flat Icon"""

lines = []

# ── Helpers ──────────────────────────────────────────────────────────
def R(x, y, w, h, fill='#ffffff', stroke='#d1d5db', sw=1.5, rx=8, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def T(x, y, txt, sz=12, fill='#111827', anchor='middle', weight='normal'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{sz}" font-weight="{weight}">{txt}</text>'

def C(x, y, label, fill='#ffffff', stroke='#d1d5db', w=106, h=24):
    return [
        R(x, y, w, h, fill=fill, stroke=stroke, sw=1.5, rx=8),
        T(x + w//2, y + h//2 + 4, label, sz=10, fill='#374151'),
    ]

def SL(x, y, txt, clr='#6b7280'):
    return T(x, y, txt, sz=9, fill=clr, anchor='start')

def emit(item):
    if isinstance(item, list):
        lines.extend(item)
    else:
        lines.append(item)

def hbar(x, y, w, color, rx=12):
    """Colored header bar: rounded top corners, flat bottom."""
    h = 26
    return (f'<path d="M {x+rx},{y} L {x+w-rx},{y} Q {x+w},{y} {x+w},{y+rx} '
            f'L {x+w},{y+h} L {x},{y+h} L {x},{y+rx} Q {x},{y} {x+rx},{y} Z" '
            f'fill="{color}"/>')

def layer_box(x, y, w, h, bg, stroke, hdr, label):
    out = []
    out.append(R(x, y, w, h, fill=bg, stroke=stroke, sw=2, rx=12))
    out.append(hbar(x, y, w, hdr, rx=12))
    out.append(f'<rect x="{x+8}" y="{y+6}" width="14" height="14" rx="3" fill="#ffffff" opacity="0.25"/>')
    out.append(T(x+30, y+17, label, sz=11, fill='#ffffff', anchor='start', weight='600'))
    return out

def arrow_down(x, y1, y2, color='#2563eb', marker='arr-blue', dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" '
            f'stroke-width="1.5" marker-end="url(#{marker})"{d}/>')

def vsep(x, y1, y2):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#e5e7eb" stroke-width="1"/>'

# ── SVG Open ─────────────────────────────────────────────────────────
emit('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1050" width="1200" height="1050">')
emit("<style>text { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }</style>")

# ── Defs ─────────────────────────────────────────────────────────────
emit('<defs>')
for mid, clr in [('arr-blue','#2563eb'),('arr-teal','#0d9488'),('arr-red','#ef4444'),
                 ('arr-purple','#9333ea'),('arr-green','#16a34a'),('arr-orange','#ea580c'),
                 ('arr-rose','#e11d48')]:
    emit(f'  <marker id="{mid}" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">')
    emit(f'    <polygon points="0 0, 10 3.5, 0 7" fill="{clr}"/>')
    emit(  '  </marker>')
emit('</defs>')

# ── Background ───────────────────────────────────────────────────────
emit('<rect width="1200" height="1050" fill="#f8fafc"/>')

# ── Header ───────────────────────────────────────────────────────────
emit(T(24, 40, 'Portefaix Platform', sz=26, fill='#111827', anchor='start', weight='600'))
emit(T(24, 60, 'Cloud-Native Kubernetes  ·  GitOps  ·  eBPF  ·  Multi-Cloud', sz=13, fill='#6b7280', anchor='start'))
emit('<line x1="20" y1="72" x2="1180" y2="72" stroke="#e5e7eb" stroke-width="1"/>')

# Header badges
for bx, bw, bf, bs, btxt, btc in [
    (840, 108, '#eff6ff', '#93c5fd', 'CNCF Stack', '#1d4ed8'),
    (956, 66,  '#fff7ed', '#fdba74', 'eBPF',       '#c2410c'),
    (1030,130, '#f0fdf4', '#86efac', 'Multi-Cloud', '#166534'),
]:
    emit(R(bx, 16, bw, 28, fill=bf, stroke=bs, sw=1.5, rx=6))
    emit(T(bx+bw//2, 34, btxt, sz=11, fill=btc, weight='600'))

# ── Layer palette: (bg, border, header, comp_fill, comp_stroke, sl_color) ──
G = ('#eff6ff', '#93c5fd', '#2563eb', '#dbeafe', '#3b82f6', '#1d4ed8')  # GitOps
N = ('#f0fdfa', '#5eead4', '#0d9488', '#ccfbf1', '#14b8a6', '#0f766e')  # Networking
S = ('#fef2f2', '#fca5a5', '#ef4444', '#fee2e2', '#f87171', '#b91c1c')  # Security
O = ('#faf5ff', '#c4b5fd', '#9333ea', '#ede9fe', '#a78bfa', '#7e22ce')  # Observability
D = ('#f0fdf4', '#86efac', '#16a34a', '#dcfce7', '#4ade80', '#166534')  # System & Data
P  = ('#fff7ed', '#fdba74', '#ea580c', '#fed7aa', '#fb923c', '#c2410c')  # Tools
CH = ('#fff1f2', '#fda4af', '#e11d48', '#ffe4e6', '#fb7185', '#9f1239')  # Chaos
EBPF = '#f97316'  # eBPF component border

# ═══════════════════════════════════════════════════════════════════════
# LAYER 0: GITOPS  (y=80, h=72)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 80, 1160, 72, G[0], G[1], G[2], 'GitOps Foundation'))
# 5 comps centered: w=110, gap=14 → total=578 → start=311
for lbl, x in [('ArgoCD',311),('Argo Workflows',429),('Argo Rollouts',547),
                ('Argo Events',665),('Kargo',783)]:
    emit(C(x, 117, lbl, fill=G[3], stroke=G[4], w=110))

# Arrows GitOps → Net (dashed = GitOps control)
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 154, 167, '#2563eb', 'arr-blue', '5,3'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 1: NETWORKING  (y=170, h=128)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 170, 1160, 128, N[0], N[1], N[2], 'Networking'))
# Row 1 (y=220): Ingress, Gateway, DNS
emit(SL(28,  216, 'Ingress · Gateway · DNS', N[5]))
for lbl, x, ebpf in [('Cilium',28,True),('K-Gateway',142,False),('Envoy GW',256,False),
                      ('Cert-Mgr',370,False),('Ext-DNS',484,False)]:
    emit(C(x, 220, lbl, fill=N[3], stroke=EBPF if ebpf else N[4]))
# Row 2 (y=268): Access, Messaging
emit(SL(28,  264, 'Zero-Trust Access · Messaging', N[5]))
for lbl, x in [('CF-Tunnel',28),('NATS',142)]:
    emit(C(x, 268, lbl, fill=N[3], stroke=N[4]))

# Arrows Net → Sec
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 300, 313, N[2], 'arr-teal'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 2: SECURITY  (y=316, h=128)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 316, 1160, 128, S[0], S[1], S[2], 'Security'))
# Row 1: Identity | Access Control  (removed: Kyverno, Kubewarden, Falco)
emit(SL(28,  362, 'Identity', S[5]))
emit(SL(276, 362, 'Access Control', S[5]))
for lbl, x, ebpf in [
    ('Authentik',28,False), ('Dex',142,False),
    ('Kube-Bench',276,False), ('Tetragon',390,True),
]:
    emit(C(x, 366, lbl, fill=S[3], stroke=EBPF if ebpf else S[4]))
emit(vsep(260, 362, 390))
# Row 2: Secrets | Scanning · Zero-Trust  (removed: Vault)
emit(SL(28,  410, 'Secrets', S[5]))
emit(SL(276, 410, 'Scanning · Zero-Trust', S[5]))
for lbl, x in [('Ext-Secrets',28),('Sealed Secrets',142),
                ('Trivy Operator',276),('SBOM Operator',390),('Paralus',504)]:
    emit(C(x, 414, lbl, fill=S[3], stroke=S[4]))
emit(vsep(260, 410, 438))

# Arrows Sec → Obs
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 446, 459, S[2], 'arr-red'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 3: OBSERVABILITY  (y=462, h=176)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 462, 1160, 176, O[0], O[1], O[2], 'Observability'))
# Row 1 (y=512): Metrics & Visualization
emit(SL(28, 508, 'Metrics · Visualization', O[5]))
for lbl, x in [('Prometheus',28),('Alertmanager',142),('Mimir',256),
                ('Grafana',370),('Grafana-Op',484),('SignOz',598)]:
    emit(C(x, 512, lbl, fill=O[3], stroke=O[4]))
# Row 2 (y=560): Logging, Tracing, Profiling
emit(SL(28, 556, 'Logging · Tracing · Profiling', O[5]))
for lbl, x, ebpf in [('Loki',28,False),('Alloy',142,False),
                      ('Tempo',256,False),('Pyroscope',370,False),('Beyla',484,True)]:
    emit(C(x, 560, lbl, fill=O[3], stroke=EBPF if ebpf else O[4]))
# Row 3 (y=608): OTel & SLO
emit(SL(28, 604, 'OpenTelemetry · SLO', O[5]))
for lbl, x in [('OTel-Operator',28),('OTel-Collector',142),('Pyrra',256),('Sloth',370)]:
    emit(C(x, 608, lbl, fill=O[3], stroke=O[4]))

# Arrows Obs → Sys
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 640, 653, O[2], 'arr-purple'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 4: SYSTEM & DATA  (y=656, h=128)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 656, 1160, 128, D[0], D[1], D[2], 'System &amp; Data'))
# Row 1 (y=706): Databases & Search/Vector
emit(SL(28, 702, 'Databases · Search · Vector', D[5]))
for lbl, x in [('CloudNativePG',28),('Dragonfly',142),('MariaDB',256),
                ('ClickHouse',370),('Qdrant',484),('Meilisearch',598)]:
    emit(C(x, 706, lbl, fill=D[3], stroke=D[4]))
# Row 2 (y=754): Scaling, Storage & Backup
emit(SL(28, 750, 'Scaling · Storage · Backup', D[5]))
for lbl, x in [('KEDA',28),('Karpenter',142),('VPA',256),
                ('Descheduler',370),('Longhorn',484),('Kured',598)]:
    emit(C(x, 754, lbl, fill=D[3], stroke=D[4]))

# Arrows Sys → Tools
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 786, 799, D[2], 'arr-green'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 5: PLATFORM TOOLS  (y=802, h=72)
# ═══════════════════════════════════════════════════════════════════════
# 5 comps (removed: Keep, Robusta, Litmus Chaos)
emit(layer_box(20, 802, 1160, 72, P[0], P[1], P[2], 'Platform Tools'))
for lbl, x in [('OpenCost',28),('Homepage',142),('Port (IDP)',256),('K8sGPT',370),('Ollama',484)]:
    emit(C(x, 839, lbl, fill=P[3], stroke=P[4]))

# Arrows Tools → Chaos
for ax in [440, 600, 760]:
    emit(arrow_down(ax, 876, 889, P[2], 'arr-orange'))

# ═══════════════════════════════════════════════════════════════════════
# LAYER 6: CHAOS ENGINEERING  (y=892, h=72)
# ═══════════════════════════════════════════════════════════════════════
emit(layer_box(20, 892, 1160, 72, CH[0], CH[1], CH[2], 'Chaos Engineering'))
# 2 comps centered: total=226 → start=487
for lbl, x in [('Litmus Chaos', 487), ('Chaos Mesh', 607)]:
    emit(C(x, 929, lbl, fill=CH[3], stroke=CH[4]))

# ═══════════════════════════════════════════════════════════════════════
# LEGEND  (y=980)
# ═══════════════════════════════════════════════════════════════════════
emit(R(20, 980, 580, 58, fill='#ffffff', stroke='#e5e7eb', sw=1, rx=8))
emit(T(32, 996, 'Legend', sz=10, fill='#374151', anchor='start', weight='600'))

leg_items = [
    (32,  1014, '#2563eb', 'arr-blue',   '5,3', 'GitOps sync'),
    (170, 1014, '#0d9488', 'arr-teal',   '',    'Network flow'),
    (300, 1014, '#9333ea', 'arr-purple', '',    'Telemetry flow'),
    (430, 1014, '#e11d48', 'arr-rose',   '',    'Chaos injection'),
]
for lx, ly, clr, mid, dash, lbl in leg_items:
    d = f' stroke-dasharray="{dash}"' if dash else ''
    emit(f'<line x1="{lx}" y1="{ly}" x2="{lx+28}" y2="{ly}" stroke="{clr}" stroke-width="1.5" marker-end="url(#{mid})"{d}/>')
    emit(T(lx+34, ly+4, lbl, sz=9, fill='#6b7280', anchor='start'))

# eBPF badge legend
emit(R(32, 1024, 106, 8, fill='#ffedd5', stroke=EBPF, sw=1.5, rx=4))
emit(T(140, 1032, '= eBPF kernel-instrumented component', sz=9, fill='#6b7280', anchor='start'))

# ── Info panel (bottom-right) ─────────────────────────────────────────
emit(R(720, 980, 460, 58, fill='#ffffff', stroke='#e5e7eb', sw=1, rx=8))
emit(T(950, 1002, 'Portefaix Platform', sz=15, fill='#111827', weight='600'))
emit(T(950, 1020, 'GitOps · eBPF · CNCF · Multi-Cloud', sz=11, fill='#6b7280'))
emit(T(950, 1036, 'v1.0  ·  2026  ·  Apache 2.0', sz=10, fill='#9ca3af'))

# ── SVG Close ─────────────────────────────────────────────────────────
emit('</svg>')

out = '/Users/nicolas.lamirault/Projects/Portefaix/portefaix-website/public/diagrams/portefaix-architecture-flat-v2.svg'
with open(out, 'w') as f:
    f.write('\n'.join(lines))
print(f'SVG written: {out}  ({len(lines)} lines)')
