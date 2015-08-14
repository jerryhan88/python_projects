import java.util.*;
import java.awt.*;

public class Tractor {
	Node start;
	Node end;
	// ShortestPathFinding�� �� ������� ������ Vector��
	Vector<Node> Path = new Vector<Node>();
	
	Color pathColor;
	// Tracktor�� ��ȣ�� ��Ƶ� value
	int number;
	// stop�� ���¿��� 1�� �����ϴ� 10�� �Ǹ� ��߽�Ű�� ���� value
	int stopTime = 0;
	// ���� ���� �޷����� ������ �� Tractor�� active�ϰ� �޸��� ���� �����ϱ� ���� value
	int tmpCount = 0;
	// Tracktor�� ���µ��� ��Ÿ��
	enum tractorState {
		move, wait, block, stop
	};
	
	tractorState state = tractorState.move;

	public Tractor(Node start, Node end, Color pathColor, int num) {
		this.start = start;
		this.end = end;
		this.pathColor = pathColor;
		this.number = num;
	}
	// Ȥ�ö� stop���¿��� �ٷ� block�� �Ǵ� tracktor���� ���� method�� �׷� ��Ȳ�� ���������� start�� end�� ����ص�
	public void saveStartEnd(Node start, Node end) {
		this.start = start;
		this.end = end;
	}
	
	public void savePath(Node newS, Node newE) {
		// Path �ʱ�ȭ �ʼ� ��
		Path.clear();
		this.start = newS;
		this.end = newE;
		Node v = newE;
		// end���� �����Ͽ� end�� prev ���迡 �ִ� Node���� ���� ���� ���� ��Ŵ
		while (true) {
			Path.add(v);
			if(v == start) {
				break;
			}
			v = v.prev;
		}
	}

	void drawPath(Graphics g) {
		// �������� �׸��� code
		g.setColor(Color.CYAN);
		g.fillOval(end.x - 15, end.y - 15, 10, 10);
		// Path.size()�� ��� ���ϱ� ������ �����̴°� ó�� ���̰� �� �� �� �ְ� �����ִ� code
		Node first = Path.lastElement();
		g.setColor(pathColor);
		g.fillOval(first.x - 15, first.y - 15, 10, 10);

		for (int i = Path.size()-1; i > 0; i--) {
			Path.get(i).drawEdge(g, Path.get(i -1));
		}
	}
}
