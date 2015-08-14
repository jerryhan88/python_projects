import java.util.*;

public class SPF {
	// Graph class�� Node���� ������ Vector
	Vector<Node> Nodes = new Vector<Node>();
	// ���⼭ PriorityQueue�� �ڽ��� ���� Node���� distance �� ���� ���� ���� return �ǵ��� �Ǿ� ����
	PriorityQueue<Node> openNodes = new PriorityQueue<Node>();
	// ShorthestPathFinding�� ���� ���θ� ������ ���� ������
	boolean success = true;

	SPF() {
	}

	// Graph class���� ���ǵ� Node���� �����ϴ� method
	public void addNode(Node n) {
		Nodes.add(n);
	}

	// ShortestPathFinding �̶�� method�� ���� ���� ���� Node���� ���¸� �ʱ�ȭ ��Ŵ
	public void reset() {
		for (int i = 0; i < Nodes.size(); i++) {
			Node clearNode = Nodes.get(i);
			clearNode.state = Node.NodeState.none;
			clearNode.distance = Integer.MAX_VALUE;
			clearNode.prev = null;
			clearNode.next = null;
		}
		openNodes.clear();
		success = true;
	}

	// Dijkstra �˰����� Ǫ�� Method
	public void ShortestPathFinding(Node start, Node end) {
		// ó���� ���� Node�� �Է¹��� �� Node ��ü�� reset ��Ű�� ������
		reset();
		Node startNode = null;
		Node endNode = null;
		// ������� �������� Yard Tractor ���� ���ִ� ������ ����� �۾� ��
		switch (start.nodeDirection) {
		// Yard Tractor�� �ٶ󺸴� �������� ����� �ؾ���
		case east:
			// ���� nodeDirection�� east�� ��� ���������� ��ĭ�� ���� ��
			startNode = Nodes.get(start.id + 1);
			start.special = true;
			break;
		case west:
			// �׸��� nodeDirection�� west�� ��� �������� ��ĭ�� ���� ��
			startNode = Nodes.get(start.id - 1);
			start.special = true;
			break;
		default:
			// �� ������ ���� ���
			// �� ���� ������� �������� �ƴ� Node���� ���ο� PathPlan�� �ϴ� ��쿡 �����
			startNode = start;
			break;
		}
		// ���� �ִ� start�� nodeDirection�� ���� �Ͱ� ���� ��ġ��
		// start�� nodeDirection�� ������ ���̰� �ִٸ� end�� special�̶�� value�� ���� �����ν� end��
		// PathPlan�� �Ҷ� ������ �ִ� ���� ������
		// special ������ ���漳���� �Ʒ��� �ִ� SPFcore ��� method���� �� �� ����
		switch (end.nodeDirection) {
		case east:
			// east�� ��� �� �ٷ� ������ endNode�� �ȴ�
			endNode = Nodes.get(end.id - 1);
			end.special = true;
			break;
		case west:
			endNode = Nodes.get(end.id + 1);
			end.special = true;
			break;
		default:
			break;
		}
		// ���⼭ �߿��Ѱ��� �Է� ���� start�� end�� �ƴ� �� ����(start�� ��=startNode), �� ����(end��
		// ��=endNode) Node���� Dijkstra �˰����� ǰ
		SPFcore(startNode, endNode);

		if (success) {
			// SPFcore�� ���������� ����� ���(startNode�� endNode���� distance�� update ����
			// ���)�� �����
			// �ϴ� start�� end�� special�� �ʱ�ȭ ��Ų��
			if (start.special || end.special) {
				start.special = false;
				end.special = false;
			}
			// ó���� �ǵ���� start�� end������ �ִܰŸ��� ���ҷ��� startNode�� endNode�� start�� end��
			// prev�� next�� �̿��Ͽ� �̾� �־��
			if (start != startNode) {
				// Tractor�� ������� �������� �ƴ� ��� �� �۾��� �ʿ� ����
				startNode.prev = start;
				start.next = startNode;
			}
			end.prev = endNode;
			endNode.next = end;

			Node tmp = end;
			// SPFcore�� ���� prev�� ���� �Ǿ� �ִ� Node���� next�� �ѹ� �� ���� ��Ŵ
			while (true) {
				tmp.prev.next = tmp;
				tmp = tmp.prev;
				if (tmp == start)
					break;
			}
			// Console�� SPFcore�� ������� ��� ��Ŵ
			System.out.print(start.id + " -> ");
			tmp = start;
			while (tmp.next != null) {
				tmp = tmp.next;
				System.out.print(tmp.id);
				if (tmp.next != null) {
					System.out.print(" -> ");
				}
			}
			System.out.println();
		}
	}

	// priorityQueue�� ����Ǿ� �ִ� Node�� �߿� distance�� ���� ���� Node �� return �ǰ� ��
	public Node getMinVertex() {
		Node v_min = (Node) openNodes.poll();

		return v_min;
	}

	// ������ Node���� distance�� update��Ű�� method
	private void updateDistance(Node start, Node nextNode, Edge e) {
		double tmpDist;
		// �Ϲ����� Dijkstra�� �ٸ��� ���⼱ turn�� �Ҷ� ����ġ�� �� �����ν� ������ Tractor�� turn�� ���� �ʵ��� ��
		if (start.prev == null) {
			// start�� prev�� ���⿡ �ʿ��� code��
			tmpDist = start.distance + 1;
		} else {
			// ���� Node edge�� ����� ������ Node�� edge ������ �������� ������ ���� ������ ����ġ�� �� �����
			Edge prevEdge = null;
			
			for (int j = 0; j < start.prev.edges.size(); j++) {
				if (start.prev.edges.get(j).nextNode == start) {
					prevEdge = start.prev.edges.get(j);
				}
			}
			if (prevEdge.state == e.state) {
				tmpDist = start.distance + 1;
			} else {
				tmpDist = start.distance + 1.1;
			}
		}
		// nextNode�� distance�� prev�� update ��Ų��
		if (tmpDist < nextNode.distance) {
			nextNode.distance = tmpDist;
			nextNode.prev = start;
		}
	}

	// Dijkstra �˰����� �ٽ��� �Ǵ� �κ�
	private Node SPFcore(Node startNode, Node endNode) {
		Node start = startNode;
		start.distance = 0;
		do {
			// Dijkstra�� �⺻�� ���� Node�� close ��Ŵ
			start.setState(Node.NodeState.close);
			for (int i = 0; i < start.edges.size(); i++) {
				Node nextNode = start.edges.get(i).nextNode;
				// �ѹ� open ��Ų Node�� �ѹ��� close Ȥ�� open ��Ű�� ���� ����
				// nextNode�� �ٸ� Yard Tractor�� �ִ� ��� �� Node�� ����
				if (nextNode.special || nextNode.state != Node.NodeState.none)
					continue;
				nextNode.setState(Node.NodeState.open);
				// open�� Node���� priorityQueue�� ��� ��
				openNodes.add(nextNode);

				Edge e = start.edges.get(i);
				// ���� Node���� ���� Node�� distance�� update �ϵ��� ��
				// ����! �� code�� openNodes �ȿ� �ִ� Node�� update ��Ű���� �Ǿ� ����
				updateDistance(start, nextNode, e);
			}
			// openNodes�ȿ� �ִ� Node�� distance�� ���� ���� Node�� start�� ����
			start = getMinVertex();
			if (start == endNode) {
				// while ������ ��� ���� ��Ű�� start�� endNode�� ���� ���� while ������ ����
				break;
			} else if (start == null) {
				// SPFcore�� ���ϴ� start�� end���� update�� �� ��Ű�� ���
				if (Math.abs(startNode.id - endNode.id) != 1) {
					// �� �߿����� �ٷ� ���� Node�� ���� ���� �ƴ϶�� success�� false ���� Tractor��
					// block ��Ų��
					success = false;
				}
				break;
			}
		} while (true);
		return start;
	}
}