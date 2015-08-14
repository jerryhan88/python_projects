import java.awt.*;
import java.util.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Graph extends JComponent implements ActionListener {
	private static final long serialVersionUID = -4160057866273543810L;
	// �������� random�ϰ� �����ϱ� ����
	Random r = new Random(1);
	// 9���� block �׸���
	Block[] b = new Block[9];
	// 3���� ship �׸���
	Ship[] sh = new Ship[3];
	// ���ο� 48��, ���η� 27���� Node�� �ΰ� ����
	Node n[] = new Node[27 * 48];
	// tractor���� �����ϴ� Vector ��
	Vector<Tractor> tractorGroup = new Vector<Tractor>();
	// ������� �������� ������ Node���� ����
	Vector<Node> possibleNode = new Vector<Node>();
	// ShortestPathFinding�� ����
	SPF Spf = new SPF();
	// Ÿ�̸� ��, �ùķ��̼��� �ӵ��� ���� ��
	final int timerDelay = 1;

	Graph() {
		for (int i = 0; i < b.length; i++) { // Block 9�� �׸���
			b[i] = new Block();
			b[i].x = (i % 3) * (240/* Block ���� */+ 80) + 50;
			b[i].y = (i / 3) * (60/* Block ���� */+ 40) + 50;
		}
		for (int i = 0; i < sh.length; i++) { // ship 3�� �׸���
			sh[i] = new Ship();
			sh[i].x = (i % 3) * (240/* Ship ���� */+ 80) + 50;
			sh[i].y = 15 + 20 * 36 + 10 - 20 * 3 - 20 * 3 - 20 * 3;
		}

		for (int i = 0; i < n.length; i++) {
			n[i] = new Node(); // Node �׸���
			n[i].x = (i % 48) * (10/* Node ���� */+ 10/* Edge */) + 30;
			n[i].y = (i / 48) * (10 + 10) + 30;
		}
		// SPF���� ShortestPathPlan�� ���� Node���� Vector �ȿ� �� �־� ��
		// ����� id�� ���� ������ �ָ鼭 �ٸ��ϵ��� �����ϰ� ��
		for (int i = 0; i < n.length; i++) {
			Spf.addNode(n[i]);
			n[i].id = i;
		}
		// ���⼭ ���ʹ� Node���� edge�� �̾��ִ� �۾���
		// ���� ���κ��� ����!
		for (int i = 0; i < n.length; i++) {
			if ((i >= 0 && i < 2 * 48) || (i >= 5 * 48 && i < 7 * 48)
					|| (i >= 10 * 48 && i < 12 * 48)
					|| (i >= 15 * 48 && i < 17 * 48)) {
				if (i % 48 == 47)
					continue;
				// ������ west�� �κе�
				n[i + 1].addEdge(n[i]);
			}
			if ((i >= 17 * 48 && i < 21 * 48)) {
				if (i % 48 == 47)
					continue;
				// �� ������
				n[i + 1].addEdge(n[i]);
				n[i].addEdge(n[i + 1]);
			}

			if (i >= 23 * 48 && i < 27 * 48) {
				if (i % 48 == 47)
					continue;
				// ������ east�� Node��
				n[i].addEdge(n[i + 1]);
			}
		}
		for (int i = 2; i < 15; i++) {
			// ���� �� �� �κ� or block ���̿� �ִ� edge�� ����� ����
			if (i == 5 || i == 6 || i == 10 || i == 11)
				continue;
			n[i * 48].addEdge(n[i * 48 + 1]);
			n[i * 48 + 1].addEdge(n[i * 48]);
			n[i * 48 + 14].addEdge(n[i * 48 + 15]);
			n[i * 48 + 15].addEdge(n[i * 48 + 14]);
			n[i * 48 + 16].addEdge(n[i * 48 + 17]);
			n[i * 48 + 17].addEdge(n[i * 48 + 16]);
			n[i * 48 + 30].addEdge(n[i * 48 + 31]);
			n[i * 48 + 31].addEdge(n[i * 48 + 30]);
			n[i * 48 + 32].addEdge(n[i * 48 + 33]);
			n[i * 48 + 33].addEdge(n[i * 48 + 32]);
			n[i * 48 + 46].addEdge(n[i * 48 + 47]);
			n[i * 48 + 47].addEdge(n[i * 48 + 47]);
		}
		for (int i = 0; i < 47; i++) {
			// QC�� ���� �ڸ� ��ó�� �ִ� Node�� ����� ����
			if (i == 2 || i == 3 || i == 4 || i == 5 || i == 11 || i == 12
					|| i == 13 || i == 14 || i == 15 || i == 22 || i == 23
					|| i == 24 || i == 25 || i == 32 || i == 33 || i == 34
					|| i == 35 || i == 42 || i == 43 || i == 44 || i == 45)
				continue;
			n[48 * 21 + i].addEdge(n[48 * 21 + 1 + i]);
			n[48 * 21 + 1 + i].addEdge(n[48 * 21 + i]);
			n[48 * 22 + i].addEdge(n[48 * 22 + 1 + i]);
			n[48 * 22 + 1 + i].addEdge(n[48 * 22 + i]);
		}

		// ���� addEdge
		for (int i = 0; i < 15; i++) {
			// 15��° �̳��� �ִ� Node�� �� �Ʒ� �Ǵ� �� ������ ����� Node�� ���� ���ڸ�
			// �ٷ� �Ʒ��� addEdge ���� ��� �Ʒ��� ���ϴ� ������
			n[48 * i].addEdge(n[48 * (i + 1)]);
			n[48 * i + 1].addEdge(n[48 * (i + 1) + 1]);
			n[48 * i + 14].addEdge(n[48 * (i + 1) + 14]);
			n[48 * i + 15].addEdge(n[48 * (i + 1) + 15]);
			// �̰� ���� ��� �� ������
			n[48 * (i + 1) + 16].addEdge(n[48 * i + 16]);
			n[48 * (i + 1) + 17].addEdge(n[48 * i + 17]);
			n[48 * i + 30].addEdge(n[48 * (i + 1) + 30]);
			n[48 * i + 31].addEdge(n[48 * (i + 1) + 31]);
			n[48 * (i + 1) + 32].addEdge(n[48 * i + 32]);
			n[48 * (i + 1) + 33].addEdge(n[48 * i + 33]);
			n[48 * (i + 1) + 46].addEdge(n[48 * i + 46]);
			n[48 * (i + 1) + 47].addEdge(n[48 * i + 47]);
		}
		for (int i = 0; i < 5; i++) {
			// block�� QC ������ ���� ����� edge����
			n[48 * (15 + i)].addEdge(n[48 * (16 + i)]);
			n[48 * (15 + i) + 1].addEdge(n[48 * (16 + i) + 1]);
			n[48 * (16 + i) + 46].addEdge(n[48 * (15 + i) + 46]);
			n[48 * (16 + i) + 47].addEdge(n[48 * (15 + i) + 47]);
		}
		for (int i = 2; i < 46; i++) {
			// block�� ���� or block ������ ���� edge��
			n[i].addEdge(n[i + 48]);
			n[i + 48].addEdge(n[i]);
			n[i + 48 * 5].addEdge(n[i + 48 * 6]);
			n[i + 48 * 6].addEdge(n[i + 48 * 5]);
			n[i + 48 * 10].addEdge(n[i + 48 * 11]);
			n[i + 48 * 11].addEdge(n[i + 48 * 10]);
			n[i + 48 * 15].addEdge(n[i + 48 * 16]);
			n[i + 48 * 16].addEdge(n[i + 48 * 15]);
			n[i + 48 * 16].addEdge(n[i + 48 * 17]);
			n[i + 48 * 17].addEdge(n[i + 48 * 16]);
			n[i + 48 * 17].addEdge(n[i + 48 * 18]);
			n[i + 48 * 18].addEdge(n[i + 48 * 17]);
			n[i + 48 * 18].addEdge(n[i + 48 * 19]);
			n[i + 48 * 19].addEdge(n[i + 48 * 18]);
			n[i + 48 * 19].addEdge(n[i + 48 * 20]);
			n[i + 48 * 20].addEdge(n[i + 48 * 19]);
		}

		for (int i = 48 * 23; i < 48 * 26; i++) {
			// ���� �Ʒ��ʿ� �ִ� edge���� ���Ϸ� ���� ��Ŵ
			n[i].addEdge(n[i + 48]);
			n[i + 48].addEdge(n[i]);
		}

		for (int i = 0; i < 48; i++) {
			// QC�� �������� �α��� edge�� ���� ����
			if (i == 3 || i == 4 || i == 5 || i == 12 || i == 13 || i == 14
					|| i == 15 || i == 23 || i == 24 || i == 25 || i == 33
					|| i == 34 || i == 35 || i == 43 || i == 44 || i == 45)
				continue;
			n[i + 48 * 20].addEdge(n[i + 48 * 21]);
			n[i + 48 * 21].addEdge(n[i + 48 * 20]);
			n[i + 48 * 21].addEdge(n[i + 48 * 22]);
			n[i + 48 * 22].addEdge(n[i + 48 * 21]);
			n[i + 48 * 22].addEdge(n[i + 48 * 23]);
			n[i + 48 * 23].addEdge(n[i + 48 * 22]);
		}

		for (int i = 0; i < 11; i++) {
			// block �ʿ��� tractor ���� �������� �Ǵ� Node�� ������ ��
			possibleNode.add(n[48 + 2 + i]);
			possibleNode.add(n[48 + 18 + i]);
			possibleNode.add(n[48 + 34 + i]);
			possibleNode.add(n[48 * 5 + 2 + i]);
			possibleNode.add(n[48 * 5 + 18 + i]);
			possibleNode.add(n[48 * 5 + 34 + i]);
			possibleNode.add(n[48 * 6 + 2 + i]);
			possibleNode.add(n[48 * 6 + 18 + i]);
			possibleNode.add(n[48 * 6 + 34 + i]);
			possibleNode.add(n[48 * 10 + 2 + i]);
			possibleNode.add(n[48 * 10 + 18 + i]);
			possibleNode.add(n[48 * 10 + 34 + i]);
			possibleNode.add(n[48 * 11 + 2 + i]);
			possibleNode.add(n[48 * 11 + 18 + i]);
			possibleNode.add(n[48 * 11 + 34 + i]);
			possibleNode.add(n[48 * 15 + 2 + i]);
			possibleNode.add(n[48 * 15 + 18 + i]);
			possibleNode.add(n[48 * 15 + 34 + i]);
		}
		// ������ Node�� ������ ����� (�׷��� ������ ������Ű�� ���� �Ǵ� ��� ������ ���� �� �� ����)
		for (int j = 0; j < possibleNode.size(); j++) {
			possibleNode.get(j).setDirection(Node.destinationState.west);
		}
		// QC �Ʒ��� �ִ� Node�� ����!! ���� ���ʰ� �������� tractor�� ������ ����Ͽ� �� �־�� ��
		for (int i = 48 * 23; i < 48 * 27; i++) {
			if (i % 48 == 0 || i % 48 == 47)
				continue;
			possibleNode.add(n[i]);
			n[i].setDirection(Node.destinationState.east);
		}
		// tractor ���� �ϳ��� �߰� ��Ŵ
		tractorGroup.add(new Tractor(n[48 * 23 + 6], n[48 * 6 + 24],
				Color.blue, 0));
		tractorGroup.add(new Tractor(n[48 + 23], n[48 * 26 + 18], Color.GREEN,
				1));
		tractorGroup.add(new Tractor(n[48 * 5 + 23], n[48 * 26 + 18 + 3],
				Color.orange, 2));
		tractorGroup.add(new Tractor(n[48 * 11 + 24], n[48 * 26 + 30],
				Color.pink, 3));
		tractorGroup.add(new Tractor(n[48 * 11 + 44], n[48 * 26 + 46],
				Color.magenta, 4));
		tractorGroup.add(new Tractor(n[48 * 24 + 23], n[48 * 5 + 40],
				Color.YELLOW, 5));
		tractorGroup
				.add(new Tractor(n[48 * 25 + 24], n[48 + 2], Color.blue, 6));
		tractorGroup.add(new Tractor(n[48 * 25 + 23], n[48 + 18], Color.GREEN,
				7));
		tractorGroup.add(new Tractor(n[48 * 5 + 40], n[48 * 25 + 18 + 3],
				Color.blue, 8));
		tractorGroup.add(new Tractor(n[48 * 6 + 24], n[48 * 24 + 17],
				Color.pink, 9));
		tractorGroup.add(new Tractor(n[48 * 25 + 2], n[48 * 6 + 6], Color.RED,
				10));
		tractorGroup.add(new Tractor(n[48 * 25 + 30], n[48 + 8], Color.GREEN,
				11));
		tractorGroup.add(new Tractor(n[48 * 26 + 21], n[48 * 10 + 9],
				Color.orange, 12));
		tractorGroup.add(new Tractor(n[48 * 26 + 40], n[48 * 15 + 8],
				Color.pink, 13));
		tractorGroup.add(new Tractor(n[48 * 25 + 3], n[48 * 11 + 24],
				Color.RED, 14));
		tractorGroup.add(new Tractor(n[48 * 26 + 40], n[48 + 40], Color.GREEN,
				15));
		tractorGroup.add(new Tractor(n[48 * 25 + 23], n[48 * 5 + 24],
				Color.orange, 16));
		tractorGroup.add(new Tractor(n[48 * 24 + 34], n[48 * 11 + 42],
				Color.pink, 17));
		tractorGroup.add(new Tractor(n[48 * 10 + 10], n[48 * 24 + 30],
				Color.RED, 18));
		tractorGroup.add(new Tractor(n[48 + 4], n[48 * 24 + 31], Color.magenta,
				19));
		// �����Ҷ� ù ��° PathPlanning
		for (int i = 0; i < tractorGroup.size(); i++) {
			Tractor tr = tractorGroup.get(i);
			Node start = tr.start;
			Node end = tr.end;
			Spf.ShortestPathFinding(start, end);
			tr.savePath(start, end);
		}
		// Ÿ�̸� �ޱ�
		new javax.swing.Timer(timerDelay, this).start();
	}
	// tractor�� ���� �ִ� ��ġ�� ������ Node�� ���¸� ���� method��
	// tractor�� �����ϴ� �˰��� ���ؼ��� �Ŀ�����Ʈ �ڷῡ�� ã�� ���� ��
	private void seeNextNode(Tractor t) {
		Node nowNode = t.Path.get(t.Path.size() - 1);
		Node nextNode = t.Path.get(t.Path.size() - 2);

		if (!nextNode.occupied) {
			// �ƹ��͵� ���ٸ� ������ ������
			t.state = Tractor.tractorState.move;
		} else {
			// �ϴ� ���� Node�� tractor�� �ҷ� ����
			Tractor nextNodeTracktor = tractorGroup
					.get(nextNode.nowNodeTracktor.number);

			switch (nextNodeTracktor.state) {
			case move:
				t.state = Tractor.tractorState.wait;
				break;

			case wait:
				Tractor T1 = t;
				Tractor T2 = nextNodeTracktor;
				Node T1NowNode = T1.Path.get(T1.Path.size() - 1);
				Node T1NextNode = T1.Path.get(T1.Path.size() - 2);
				Node T2NowNode = T2.Path.get(T2.Path.size() - 1);
				Node T2NextNode = T2.Path.get(T2.Path.size() - 2);

				if (T1NowNode == T2NextNode && T1NextNode == T2NowNode) {
					T2.tmpCount++;
					if (T1.tmpCount == 1) {
						T1NextNode.special = true;
						Spf.ShortestPathFinding(T1NowNode, T1.end);
						T1NextNode.special = false;

						t.state = Tractor.tractorState.move;
						t.tmpCount = 0;
						if (Spf.success) {
							T1.savePath(T1NowNode, T1.end);
							T1.state = Tractor.tractorState.move;
						} else {
							T1.state = Tractor.tractorState.block;
						}
						break;
					}
					t.state = Tractor.tractorState.wait;
				}
				t.state = Tractor.tractorState.wait;
				break;
			default:
				if (nextNodeTracktor.state == Tractor.tractorState.stop) {
					t.state = Tractor.tractorState.wait;
				} else {
					nextNode.special = true;
					Spf.ShortestPathFinding(nowNode, t.end);
					nextNode.special = false;

					if (Spf.success) {
						t.savePath(nowNode, t.end);
						t.state = Tractor.tractorState.move;
					} else {
						t.state = Tractor.tractorState.block;
					}
				}
				break;
			}
		}
	}

	public void actionPerformed(ActionEvent e) {
		for (int i = 0; i < tractorGroup.size(); i++) {
			Tractor t = tractorGroup.get(i);
			Node nowNode = t.Path.lastElement();

			if (t.Path.size() == 1) {
				t.state = Tractor.tractorState.stop;
			}

			switch (t.state) {
			case stop:
				t.stopTime++;
				if (t.stopTime == 10) {
					t.stopTime = -1;
					Node newStart = t.end;
					Node newTarget = null;

					do {
						int z = r.nextInt(possibleNode.size());
						newTarget = possibleNode.get(z);
					} while (newTarget == newStart);

					Spf.ShortestPathFinding(t.end, newTarget);
					if (Spf.success) {
						t.savePath(newStart, newTarget);
						t.state = Tractor.tractorState.move;
					} else {
						t.state = Tractor.tractorState.block;
						t.saveStartEnd(newStart, newTarget);
						break;
					}
					seeNextNode(t);
				}
				break;

			case block:
				if (t.Path.size() == 1) {
					Spf.ShortestPathFinding(nowNode, t.end);
					if (Spf.success) {
						t.savePath(nowNode, t.end);
						t.state = Tractor.tractorState.move;
					} else {
						t.state = Tractor.tractorState.block;
						break;
					}
				} else {
					Tractor tmpTracktor = t;
					Node nextNode = t.Path.get(t.Path.size() - 2);
					nextNode.special = true;
					Spf.ShortestPathFinding(nowNode, t.end);
					nextNode.special = false;

					if (Spf.success) {
						t.savePath(nowNode, t.end);
						if (t.Path.size() >= tmpTracktor.Path.size()) {
							t = tmpTracktor;
						}
						t.state = Tractor.tractorState.move;
					} else {
						t.state = Tractor.tractorState.block;
						break;
					}
				}
				seeNextNode(t);
				break;

			default:
				seeNextNode(t);
				break;
			}

			if (t.state == Tractor.tractorState.move) {
				Node tmp = nowNode;
				t.Path.get(t.Path.size() - 2).setOccupy(t);
				t.Path.remove(t.Path.size() - 1);
				tmp.setNotOcuupy();
			}
			repaint();
		}
	}
	// �׸��� �׸��� ����
	public void paintComponent(Graphics g) {
		// ship�ʿ� �ִ� Line
		g.drawLine(15, 15 + 20 * 36 - 20 * 3 - 20 * 3 - 20 * 3, 15 + 20 * 48,
				15 + 20 * 36 - 20 * 3 - 20 * 3 - 20 * 3);
		for (int i = 0; i < n.length; i++) {
			// QC ��ó�� ����� �� Node�� ó��  �׸��� ������ �� �׸���
			if (((i >= 48 * 21 + 3 && i <= 48 * 21 + 5)
					|| (i >= 48 * 21 + 12 && i <= 48 * 21 + 15)
					|| (i >= 48 * 21 + 23 && i <= 48 * 21 + 25)
					|| (i >= 48 * 21 + 33 && i <= 48 * 21 + 35) || (i >= 48 * 21 + 43 && i <= 48 * 21 + 45))
					|| ((i >= 48 * 22 + 3 && i <= 48 * 22 + 5)
							|| (i >= 48 * 22 + 12 && i <= 48 * 22 + 15)
							|| (i >= 48 * 22 + 23 && i <= 48 * 22 + 25)
							|| (i >= 48 * 22 + 33 && i <= 48 * 22 + 35) || (i >= 48 * 22 + 43 && i <= 48 * 22 + 45)))
				continue;
			n[i].draw(g);
		}
		for (int i = 0; i < sh.length; i++) {
			sh[i].draw(g);
		}
		for (int i = 0; i < tractorGroup.size(); i++) {
			tractorGroup.get(i).drawPath(g);
		}
		for (int i = 0; i < b.length; i++) {
			b[i].draw(g);
		}
	}

}
