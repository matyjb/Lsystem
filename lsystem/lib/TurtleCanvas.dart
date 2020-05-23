
import 'package:flutter/material.dart';
import 'package:lsystem/Line.dart';

class TurtleCanvas extends StatelessWidget {
  final List<Line> lines;
  TurtleCanvas({Key key, this.lines}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      painter: TurtlePainter(this.lines),
      child: Column(),
    );
  }
}

class TurtlePainter extends CustomPainter {
  final List<Line> lines;

  TurtlePainter(this.lines);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = Colors.red;
    final paint2 = Paint()..color = Colors.white;
    canvas.drawRect(
        Rect.fromPoints(Offset(0, 0), Offset(size.width, size.height)),
        paint);
    canvas.drawRect(
        Rect.fromPoints(Offset(5, 5), Offset(size.width-5, size.height-5)),
        paint2);

    for (var line in this.lines) {
      Paint p = Paint()..color = line.color;
      canvas.drawLine(line.p0, line.p1, p);
    }
  }

  @override
  bool shouldRepaint(TurtlePainter old) {
    return false;
  }
}
