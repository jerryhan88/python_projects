
public class Edge {
	// �� Node�� edge�� �̾��� ���� Node
	Node nextNode;
	
	enum EdgeState {
		none, East, West, South, North
	};
	
	EdgeState state = EdgeState.none;
	
	public void setState(EdgeState ns) {
		state = ns;
	}

	void setEdge(Node via) {
		this.nextNode = via;
	}
}
