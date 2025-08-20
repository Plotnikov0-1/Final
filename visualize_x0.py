import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx


def build_graph():
    graph = nx.DiGraph()
    edges = [
        ("Idea", "Hypothesis"),
        ("Hypothesis", "Experiment"),
        ("Experiment", "Conclusion"),
        ("Conclusion", "Idea"),
    ]
    graph.add_edges_from(edges)
    return graph


def main():
    G = build_graph()
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        edgecolors="black",
        node_size=2000,
        arrows=True,
    )
    plt.title("X0 Graph Visualization")
    plt.savefig("x0_graph.png")


if __name__ == "__main__":
    main()
