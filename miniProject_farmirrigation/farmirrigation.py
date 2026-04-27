import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# -------------------------------
# DATA STRUCTURES
# -------------------------------

class Field:
    def __init__(self, fid, crop, area, water_req):
        self.id = fid
        self.crop = crop
        self.need = area * water_req


class Source:
    def __init__(self, sid, capacity):
        self.id = sid
        self.capacity = capacity


class Network:
    def __init__(self):
        self.fields = {}
        self.sources = {}
        self.pipes = {}

    def add_field(self, f):
        self.fields[f.id] = f

    def add_source(self, s):
        self.sources[s.id] = s

    def add_pipe(self, src, fld, dist):
        self.pipes[(src, fld)] = dist

    def loss(self, distance):
        return min(distance * 0.0005, 0.3)


# -------------------------------
# ALGORITHMS
# -------------------------------

def algo_greedy(network):
    plan = {}
    for src_id, src in network.sources.items():
        remaining = src.capacity
        pipes = [(fid, d) for (s, fid), d in network.pipes.items() if s == src_id]
        pipes.sort(key=lambda x: x[1])

        for fld_id, dist in pipes:
            need = network.fields[fld_id].need
            loss = network.loss(dist)
            total = need / (1 - loss)

            if remaining >= total:
                plan[(src_id, fld_id)] = need
                remaining -= total
    return plan


def algo_priority(network):
    plan = {}
    priority = {'rice': 10, 'wheat': 9, 'vegetables': 8, 'corn': 7}

    fields = sorted(network.fields.values(), key=lambda f: -priority.get(f.crop, 5))
    remaining = {s: network.sources[s].capacity for s in network.sources}

    for field in fields:
        for (src_id, fld_id), dist in network.pipes.items():
            if fld_id == field.id:
                need = field.need
                loss = network.loss(dist)
                total = need / (1 - loss)

                if remaining[src_id] >= total:
                    plan[(src_id, fld_id)] = need
                    remaining[src_id] -= total
                    break
    return plan


def algo_efficient(network):
    plan = {}
    for src_id, src in network.sources.items():
        remaining = src.capacity
        pipes = [(fid, d) for (s, fid), d in network.pipes.items() if s == src_id]
        pipes.sort(key=lambda x: network.loss(x[1]))

        for fld_id, dist in pipes:
            need = network.fields[fld_id].need
            loss = network.loss(dist)
            total = need / (1 - loss)

            if remaining >= total:
                plan[(src_id, fld_id)] = need
                remaining -= total
    return plan


# -------------------------------
# CALCULATIONS
# -------------------------------

def calc(network, plan):
    if not plan:
        return 0, 0, 0

    allocated = sum(plan.values())
    loss_total = 0

    for (src, fld), dist in network.pipes.items():
        if (src, fld) in plan:
            loss = network.loss(dist)
            loss_total += plan[(src, fld)] * loss

    total = allocated + loss_total
    efficiency = (allocated / total) * 100 if total else 0

    return efficiency, allocated, loss_total


# -------------------------------
# GRAPH VISUALIZATION 🔥
# -------------------------------

def draw_graph(network):
    G = nx.DiGraph()

    # Add nodes
    for s in network.sources:
        G.add_node(s, color='blue')

    for f in network.fields:
        G.add_node(f, color='green')

    # Add edges
    for (src, fld), dist in network.pipes.items():
        G.add_edge(src, fld, weight=dist)

    pos = nx.spring_layout(G)
    colors = [G.nodes[n]['color'] for n in G.nodes]

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    ax.set_title("Irrigation Network Graph")
    return fig


# -------------------------------
# UI
# -------------------------------

def main():
    st.set_page_config(page_title="Farm Irrigation", layout="wide")

    st.title("💧 Farm Irrigation Optimizer")
    st.markdown("### Smart Water Allocation using Algorithms")

    # Sidebar inputs
    st.sidebar.header("⚙ Controls")

    well_cap = st.sidebar.slider("Well Capacity", 10000, 100000, 50000)
    tank_cap = st.sidebar.slider("Tank Capacity", 10000, 100000, 30000)

    st.sidebar.subheader("➕ Add Custom Field")

    crop = st.sidebar.selectbox("Crop", ["rice", "wheat", "vegetables", "corn"])
    area = st.sidebar.slider("Area", 1, 10, 3)
    water_req = st.sidebar.slider("Water per unit", 1000, 10000, 5000)

    # Build network
    net = Network()
    net.add_source(Source("Well-1", well_cap))
    net.add_source(Source("Tank-1", tank_cap))

    # Default fields
    net.add_field(Field("F1", "rice", 5, 8000))
    net.add_field(Field("F2", "wheat", 3, 5000))
    net.add_field(Field("F3", "vegetables", 2, 6000))

    # User field
    net.add_field(Field("F_User", crop, area, water_req))

    # Pipes
    net.add_pipe("Well-1", "F1", 50)
    net.add_pipe("Well-1", "F2", 200)
    net.add_pipe("Tank-1", "F3", 80)
    net.add_pipe("Tank-1", "F_User", 120)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌐 Network")
        st.pyplot(draw_graph(net))

    if st.button("Run Simulation 🚀"):

        g = calc(net, algo_greedy(net))
        p = calc(net, algo_priority(net))
        e = calc(net, algo_efficient(net))

        results = {
            "Greedy": g,
            "Priority": p,
            "Efficient": e
        }

        with col2:
            st.subheader("📊 Results")

            for name, (eff, alloc, loss) in results.items():
                st.write(f"{name} → {eff:.2f}% efficiency")

            fig, ax = plt.subplots()
            ax.bar(results.keys(), [v[0] for v in results.values()])
            ax.set_title("Efficiency Comparison")

            st.pyplot(fig)


if __name__ == "__main__":
    main()