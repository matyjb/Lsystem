import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
        body: TurtleManager(),
      ),
    );
  }
}

class TurtleState {
  double posX;
  double posY;
  double rotation;

  TurtleState({this.posX = 0, this.posY = 0, this.rotation = 0});

  @override
  String toString() {
    return "(" +
        this.posX.toString() +
        "," +
        this.posY.toString() +
        "," +
        this.rotation.toString() +
        " deg)";
  }
}

class TurtleManager extends StatefulWidget {
  TurtleState turtleState = TurtleState();
  List<TurtleState> stack = [];

  TurtleManager({Key key}) : super(key: key);

  @override
  _TurtleManagerState createState() => _TurtleManagerState();
}

class _TurtleManagerState extends State<TurtleManager> {
  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(child: TurtleCanvas(lines: [])),
        Column(
          children: [
            Expanded(
              child: Container(
                width: 300,
                child: RightBar(turtleState: this.widget.turtleState),
              ),
            )
          ],
        ),
      ],
    );
  }
}

class RightBar extends StatelessWidget {
  final TurtleState turtleState;
  const RightBar({Key key, this.turtleState}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border(
          left: BorderSide(color: Colors.grey,width: 2)
        ),
      ),
      child: Column(
        children: [
          Center(
            child: Container(
              child: Text(this.turtleState.toString(),
                  style:
                      TextStyle(color: Colors.teal, fontWeight: FontWeight.bold)),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Axiom',
              ),
            ),
          ),
          RaisedButton(
            onPressed: () {},
            child: Text("Execute"),
          )
        ],
      ),
    );
  }
}

class Line {
  double p0x;
  double p0y;
  double p1x;
  double p1y;

  Line(this.p0x, this.p0y, this.p1x, this.p1y);
}

class TurtleCanvas extends StatelessWidget {
  final List<Line> lines;
  TurtleCanvas({Key key, this.lines}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      painter: TurtlePainter(this.lines),
      child: Expanded(child: Container()),
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
  }

  @override
  bool shouldRepaint(TurtlePainter old) {
    return false;
  }
}
