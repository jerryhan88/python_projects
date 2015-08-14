import java.awt.*;
import java.util.*;

public class Node implements Comparable<Node> {
	// Node�� �׸��� ���� ��ǥ x,y
	int x;
	int y;
	// �� Node ���� ���� �ľ��ϱ�
	int id = -1;
	// distance�� �ʱ�ȭ�� �̷��� �صξ�� ��Ȯ�� ShortestPathPlan�� �� �� ����
	double distance = Integer.MAX_VALUE;
	// Node�� Tractor�� �ִ��� ������ ���θ� �Ǵ���
	boolean occupied;
	// SPF�� �Ҷ� �����ؾ� �� (���� Node�� �ִ� ������ block�� ���) Node�� ǥ����
	boolean special;
	// ���� Node�� ����ϱ�
	Node prev = null;
	// ���� Node�� ����ϱ�
	Node next = null;
	// �� Node�� ���ִ� ������ �����
	Tractor nowNodeTracktor = null;
	// �� Node���� �ٸ� Node ����Ǿ� �ִ� edge���� ������ �ִ� Vector 
	Vector<Edge> edges = new Vector<Edge>();
	// �� Node�� open�� close�� ��Ÿ��  SPF class ���� SPFcore method���� �̿� ��
	enum NodeState {
		none, open, close
	};
	// Node�� ������ �� �ִ� ������ ���� ��
	enum destinationState {
		none, east, west
	}

	NodeState state = NodeState.none;
	destinationState nodeDirection = destinationState.none;

	Node() {
	}
	// NodeState�� ���¸� ������
	public void setState(NodeState ns) {
		state = ns;
	}
	// destinationState�� ���¸� ������
	public void setDirection(destinationState ds) {
		nodeDirection = ds;
	}
	// �� Node�� tractor�� ��� �Դٰ� ���� ��
	public void setOccupy(Tractor t) {
		occupied = true;
		nowNodeTracktor = t;
	}
	// Node���� tractor�� ���� �������� ����
	public void setNotOcuupy() {
		occupied = false;
		nowNodeTracktor = null;
	}
	
	public void addEdge(Node via) {
		Edge e = new Edge();
		e.setEdge(via);
		// edge�� ������ ���� �ֱ� ���� code��  Node���� ������ �ִ� id�� �̿��Ͽ� �װ��� �������� ������
		if (id - e.nextNode.id == -1) {
			e.setState(Edge.EdgeState.East);
		} else if (id - e.nextNode.id == 1) {
			e.setState(Edge.EdgeState.West);
		} else if (id - e.nextNode.id < -1) {
			e.setState(Edge.EdgeState.South);
		} else {
			e.setState(Edge.EdgeState.North);
		}
		// ������ �����ѵ� edges�� ������ ��
		edges.add(e);
	}
	// priorityQueue�� �̾����� code��  �� code�� ���Ͽ� distance�� ��ġ�� ���� ���� ���� �ٷ� return�� �� ����
	public int compareTo(Node n) {
		if (distance == n.distance) {
			return 0;
		} else if (distance > n.distance) {
			return 1;
		} else {
			return -1;
		}
	}
	// �� �׸��� �׸��� code
	void draw(Graphics g) {
		g.drawOval(x - 15, y - 15, 10, 10);

		for (int i = 0; i < edges.size(); i++) {
			Edge e = edges.get(i);
			drawEdge(g, e.nextNode);
		}
	}
	// edge�� �׸��� code�� ũ�� Line�� �׸��� �Ͱ� ȭ��ǥ���� �׸��� �ΰ��� ������
	void drawEdge(Graphics g, Node n1) {
		double ax = n1.x - x;
		double ay = n1.y - y;

		double la = Math.sqrt(ax * ax + ay * ay);

		double ux = ax / la;
		double uy = ay / la;

		int sx = x + (int) (ux * 5) - 10;
		int sy = y + (int) (uy * 5) - 10;
		int ex = n1.x - (int) (ux * 5) - 10;
		int ey = n1.y - (int) (uy * 5) - 10;

		double px = -uy;
		double py = ux;
		// Node�� Node ���̸� ������ �̾���
		g.drawLine(sx, sy, ex, ey);
		// �̾��� Node�� ȭ��ǥ����
		g.drawLine(ex, ey, ex - (int) (ux * 5) + (int) (px * 3), ey
				- (int) (uy * 5) + (int) (py * 3));
		g.drawLine(ex, ey, ex - (int) (ux * 5) - (int) (px * 3), ey
				- (int) (uy * 5) - (int) (py * 3));
	}
}
