#!/usr/bin/env python3
"""Portefaix Platform Architecture Diagram - Blueprint Style"""

lines = []

def R(x, y, w, h, fill='none', stroke='#00b4d8', sw=1, rx=2, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def T(x, y, txt, sz=11, fill='#caf0f8', anchor='middle', weight='normal'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{sz}" font-weight="{weight}">{txt}</text>'

def C(x, y, label, stroke='#00b4d8', w=100, h=22):
    return [
        R(x, y, w, h, fill='#0d1f3c', stroke=stroke),
        T(x + w//2, y + h//2 + 4, label, sz=10),
    ]

def SL(x, y, txt):
    return T(x, y, txt, sz=9, fill='#48cae4', anchor='start')

def emit(item):
    if isinstance(item, list):
        lines.extend(item)
    else:
        lines.append(item)

def arr(x1, y1, x2, y2, color, marker, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5" marker-end="url(#{marker})"{d}/>'

# SVG Open
emit('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 920" width="1200" height="920">')
emit("<style>text { font-family: 'Courier New', 'Lucida Console', monospace; }</style>")

# Defs
emit('<defs>')
emit('  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">')
emit('    <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#112240" stroke-width="0.5"/>')
emit('  </pattern>')
for mid, clr in [('arr-blue','#3b82f6'),('arr-cyan','#00b4d8'),('arr-orange','#f77f00'),('arr-green','#06d6a0'),('arr-purple','#7c3aed')]:
    emit(f'  <marker id="{mid}" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">')
    emit(f'    <polygon points="0 0, 8 3, 0 6" fill="{clr}"/>')
    emit(  '  </marker>')
emit('</defs>')

# Background
emit('<rect width="1200" height="920" fill="#0a1628"/>')
emit('<rect width="1200" height="920" fill="url(#grid)" opacity="0.6"/>')

# Header
emit(T(25, 34, 'PORTEFAIX PLATFORM', sz=22, fill='#ffffff', anchor='start', weight='700'))
emit(T(25, 52, 'Cloud-Native Kubernetes  ·  GitOps  ·  eBPF  ·  Multi-Cloud', sz=12, fill='#48cae4', anchor='start'))
emit(R(852, 13, 100, 22, fill='#1e3a5f', stroke='#3b82f6', sw=1, rx=3))
emit(T(902, 28, 'CNCF STACK', sz=10, fill='#93c5fd'))
emit(R(960, 13, 60, 22, fill='#7c2d12', stroke='#f77f00', sw=1, rx=3))
emit(T(990, 28, 'eBPF', sz=10, fill='#fef3c7'))
emit(R(1028, 13, 120, 22, fill='#1e3a5f', stroke='#06d6a0', sw=1, rx=3))
emit(T(1088, 28, 'MULTI-CLOUD', sz=10, fill='#6ee7b7'))
emit(R(1156, 13, 26, 22, fill='#1e3a5f', stroke='#48cae4', sw=1, rx=3))
emit(T(1169, 28, 'v1', sz=10, fill='#caf0f8'))

EBPF = '#f77f00'

# ═══ LAYER 0: GITOPS (y=65, h=64) ═══════════════════════════════════
G = '#3b82f6'
emit(R(20, 65, 1160, 64, stroke=G, sw=2))
emit(T(30, 78, 'GITOPS FOUNDATION', sz=10, fill=G, anchor='start', weight='700'))
for label, x in [('ArgoCD',304),('Argo Workflows',426),('Argo Rollouts',548),('Argo Events',670),('Kargo',792)]:
    emit(C(x, 86, label, stroke=G, w=105))

for ax in [430, 600, 770]:
    emit(arr(ax, 129, ax, 144, G, 'arr-blue', '4,2'))

# ═══ LAYER 1: NETWORKING (y=144, h=95) ═══════════════════════════════
N = '#0891b2'
emit(R(20, 144, 1160, 95, stroke=N, sw=2))
emit(T(30, 157, 'NETWORKING', sz=10, fill=N, anchor='start', weight='700'))
emit(SL(28, 167, 'INGRESS · GATEWAY · CERT · DNS'))
for label, x, ebpf in [('Cilium',28,True),('K-Gateway',136,False),('Envoy-GW',244,False),
                        ('Traefik',352,False),('Cert-Mgr',460,False),('Ext-DNS',568,False)]:
    emit(C(x, 171, label, stroke=EBPF if ebpf else N))
emit(SL(28, 198, 'ACCESS · MESSAGING'))
for label, x in [('CF-Tunnel',28),('Tailscale VPN',136),('NATS',244)]:
    emit(C(x, 202, label, stroke=N))

for ax in [430, 600, 770]:
    emit(arr(ax, 239, ax, 254, N, 'arr-cyan'))

# ═══ LAYER 2: SECURITY (y=254, h=110) ════════════════════════════════
S = '#dc2626'
emit(R(20, 254, 1160, 110, stroke=S, sw=2))
emit(T(30, 267, 'SECURITY', sz=10, fill=S, anchor='start', weight='700'))
emit(SL(28,  277, 'IDENTITY'))
emit(SL(276, 277, 'POLICY'))
emit(SL(620, 277, 'RUNTIME'))
for label, x, ebpf in [('Authentik',28,False),('Dex',136,False),
                        ('Kyverno',276,False),('Kubewarden',384,False),('Kube-Bench',492,False),
                        ('Falco',620,True),('Tetragon',728,True)]:
    emit(C(x, 281, label, stroke=EBPF if ebpf else S))
emit(SL(28,  311, 'SECRETS'))
emit(SL(384, 311, 'SCANNING · ZERO-TRUST'))
for label, x in [('Vault',28),('Ext-Secrets',136),('Sealed-Secrets',244),
                  ('Trivy-Operator',384),('SBOM-Operator',492),('Paralus',600)]:
    emit(C(x, 315, label, stroke=S))

for ax in [430, 600, 770]:
    emit(arr(ax, 364, ax, 379, '#7c3aed', 'arr-purple'))

# ═══ LAYER 3: OBSERVABILITY (y=379, h=145) ═══════════════════════════
O = '#7c3aed'
emit(R(20, 379, 1160, 145, stroke=O, sw=2))
emit(T(30, 392, 'OBSERVABILITY', sz=10, fill=O, anchor='start', weight='700'))
emit(SL(28, 402, 'METRICS · VISUALIZATION'))
for label, x in [('Prometheus',28),('Alertmanager',136),('Mimir',244),
                  ('Grafana',352),('Grafana-Op',460),('SignOz',568)]:
    emit(C(x, 406, label, stroke=O))
emit(SL(28, 433, 'LOGGING · TRACING · PROFILING'))
for label, x, ebpf in [('Loki',28,False),('Fluentbit',136,False),('Vector',244,False),
                        ('Alloy',352,False),('Tempo',460,False),('Pyroscope',568,False),('Beyla',676,True)]:
    emit(C(x, 437, label, stroke=EBPF if ebpf else O))
emit(SL(28, 463, 'OPENTELEMETRY · SLO'))
for label, x in [('OTel-Operator',28),('OTel-Collector',136),('Pyrra',244),('Sloth',352)]:
    emit(C(x, 467, label, stroke=O))

for ax in [430, 600, 770]:
    emit(arr(ax, 524, ax, 539, '#06d6a0', 'arr-green'))

# ═══ LAYER 4: SYSTEM & DATA (y=539, h=108) ═══════════════════════════
D = '#059669'
emit(R(20, 539, 1160, 108, stroke=D, sw=2))
emit(T(30, 552, 'SYSTEM &amp; DATA', sz=10, fill=D, anchor='start', weight='700'))
emit(SL(28, 562, 'DATABASES · SEARCH · VECTOR'))
for label, x in [('CloudNativePG',28),('Dragonfly',136),('MariaDB',244),
                  ('ClickHouse',352),('Qdrant',460),('Meilisearch',568)]:
    emit(C(x, 566, label, stroke=D))
emit(SL(28, 592, 'SCALING · STORAGE · BACKUP'))
for label, x in [('KEDA',28),('Karpenter',136),('VPA',244),
                  ('Descheduler',352),('Longhorn',460),('Velero',568),('Kured',676)]:
    emit(C(x, 596, label, stroke=D))

for ax in [430, 600, 770]:
    emit(arr(ax, 647, ax, 662, '#f77f00', 'arr-orange'))

# ═══ LAYER 5: PLATFORM TOOLS (y=662, h=72) ════════════════════════════
P = '#d97706'
emit(R(20, 662, 1160, 72, stroke=P, sw=2))
emit(T(30, 675, 'PLATFORM TOOLS', sz=10, fill=P, anchor='start', weight='700'))
for label, x in [('OpenCost',28),('Homepage',136),('Port (IDP)',244),('K8sGPT',352),
                  ('Ollama',460),('Keep',568),('Robusta',676),('Litmus Chaos',784)]:
    emit(C(x, 683, label, stroke=P))

# ═══ LEGEND (y=745) ══════════════════════════════════════════════════
emit(R(20, 745, 555, 78, fill='#0d1f3c', stroke='#1e3a5f', sw=1))
emit(T(30, 759, 'LEGEND', sz=9, fill='#48cae4', anchor='start', weight='700'))
for lx, ly, clr, mid, dash, lbl in [
    (30,  774, '#3b82f6', 'arr-blue',   '4,2', 'GitOps sync (dashed)'),
    (210, 774, '#00b4d8', 'arr-cyan',   '',     'Layer data flow'),
    (380, 774, '#7c3aed', 'arr-purple', '',     'Telemetry flow'),
]:
    d = f' stroke-dasharray="{dash}"' if dash else ''
    emit(f'<line x1="{lx}" y1="{ly}" x2="{lx+30}" y2="{ly}" stroke="{clr}" stroke-width="1.5" marker-end="url(#{mid})"{d}/>')
    emit(T(lx+35, ly+4, lbl, sz=9, fill='#caf0f8', anchor='start'))
emit(R(30, 787, 100, 20, fill='#0d1f3c', stroke='#f77f00', sw=1))
emit(T(80, 801, 'Component', sz=9, fill='#caf0f8'))
emit(T(140, 801, '= eBPF kernel-instrumented', sz=9, fill='#fef3c7', anchor='start'))

# ═══ BLUEPRINT TITLE BLOCK ════════════════════════════════════════════
bx, by = 745, 745
emit(R(bx, by, 435, 80, fill='#0d1f3c', stroke='#00b4d8', sw=1))
emit(f'<line x1="{bx}" y1="{by+18}" x2="{bx+435}" y2="{by+18}" stroke="#00b4d8" stroke-width="0.5"/>')
emit(T(bx+217, by+13, 'SYSTEM ARCHITECTURE', sz=9, fill='#48cae4'))
emit(T(bx+217, by+40, 'PORTEFAIX PLATFORM', sz=15, fill='#ffffff', weight='700'))
emit(T(bx+217, by+57, 'GitOps · eBPF · CNCF · Multi-Cloud', sz=10, fill='#00b4d8'))
emit(T(bx+217, by+73, 'v1.0  ·  2026  ·  Apache 2.0', sz=9, fill='#48cae4'))

emit('</svg>')

out = '/Users/nicolas.lamirault/Projects/Portefaix/portefaix-website/portefaix-architecture.svg'
with open(out, 'w') as f:
    f.write('\n'.join(lines))
print(f'SVG written: {out}  ({len(lines)} lines)')
