import java.awt.*;
// �ܼ��� Ship�� �׸��� class ��
public class Ship {

	int x;
	int y;

	void draw(Graphics g) {
		g.drawOval(x, y, 240, 35);
	}
}
