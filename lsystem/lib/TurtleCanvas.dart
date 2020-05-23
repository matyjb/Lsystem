import 'package:flutter/material.dart';
import 'package:lsystem/Line.dart';

class TurtleCanvas extends StatefulWidget {
  final List<Line> lines;
  TurtleCanvas({Key key, this.lines}) : super(key: key);

  @override
  _TurtleCanvasState createState() => _TurtleCanvasState();
}

class _TurtleCanvasState extends State<TurtleCanvas> {
  Offset offset = Offset(0, 0);
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onPanUpdate: (DragUpdateDetails details) {
        this.setState(() {
          offset += details.delta;
        });
      },
      child: ClipRect(
        child: CustomPaint(
          painter: TurtlePainter(this.widget.lines,this.offset),
          child: Column(),
        ),
      ),
    );
  }
}

class TurtlePainter extends CustomPainter {
  final List<Line> lines;
  final Offset offset;

  TurtlePainter(this.lines, this.offset);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = Colors.red;
    final paint2 = Paint()..color = Colors.white;
    canvas.drawRect(
        Rect.fromPoints(Offset(0, 0), Offset(size.width, size.height)), paint);
    canvas.drawRect(
        Rect.fromPoints(Offset(5, 5), Offset(size.width - 5, size.height - 5)),
        paint2);

    for (var line in this.lines) {
      Paint p = Paint()..color = line.color;
      canvas.drawLine(line.p0 + offset, line.p1 + offset, p);
    }
  }

  @override
  bool shouldRepaint(TurtlePainter old) {
    return old.offset != offset;
    // return false;
  }
}
