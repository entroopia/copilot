#include <QApplication>
#include <QPainter>
#include <QWidget>
#include <QPen>
#include <QtMath>

class StarWidget : public QWidget {
protected:
    void paintEvent(QPaintEvent *) override {
        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);
        int cx = width() / 2;
        int cy = height() / 2;
        int radius = qMin(width(), height()) * 0.4;

        // Draw circle
        QPen pen(Qt::black, 2);
        painter.setPen(pen);
        painter.drawEllipse(QPoint(cx, cy), radius, radius);

        // Draw first triangle
        pen.setColor(Qt::red);
        painter.setPen(pen);
        QPolygon triangle1;
        for (int i = 0; i < 3; ++i) {
            double angle = M_PI / 2 + i * 2 * M_PI / 3;
            int x = cx + radius * std::cos(angle);
            int y = cy - radius * std::sin(angle);
            triangle1 << QPoint(x, y);
        }
        painter.drawPolygon(triangle1);

        // Draw second triangle (rotated by 60 degrees)
        QPolygon triangle2;
        for (int i = 0; i < 3; ++i) {
            double angle = M_PI / 2 + M_PI / 6 + i * 2 * M_PI / 3;
            int x = cx + radius * std::cos(angle);
            int y = cy - radius * std::sin(angle);
            triangle2 << QPoint(x, y);
        }
        painter.drawPolygon(triangle2);
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    StarWidget w;
    w.resize(400, 400);
    w.setWindowTitle("6-Pointed Star in Circle");
    w.show();
    return app.exec();
}
