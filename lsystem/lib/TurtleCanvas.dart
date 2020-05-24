import 'package:flutter/material.dart';

class TurtleCanvas extends StatefulWidget {
  final List<Path> paths;
  TurtleCanvas({Key key, this.paths}) : super(key: key);

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
          painter: TurtlePainter(this.widget.paths,this.offset),
          child: Column(),
        ),
      ),
    );
  }
}

class TurtlePainter extends CustomPainter {
  final List<Path> paths;
  final Offset offset;

  TurtlePainter(this.paths, this.offset);
  @override
  void paint(Canvas canvas, Size size) {
    for (var path in this.paths) {
      // Paint p = Paint()..color = line.color;
      Paint p = Paint()
        ..color = Colors.black
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2;
      canvas.drawPath(path.shift(offset), p);
    }
  }

  @override
  bool shouldRepaint(TurtlePainter old) {
    return old.offset != offset;
  }
}
