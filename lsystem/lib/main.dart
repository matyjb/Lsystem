import 'package:flutter/material.dart';
import 'package:lsystem/Line.dart';
import 'package:lsystem/RightBar.dart';
import 'package:lsystem/Rule.dart';
import 'package:lsystem/TurtleCanvas.dart';

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

class TurtleManager extends StatefulWidget {
  List<Line> linesDrawn = [];

  TurtleManager({Key key}) : super(key: key);

  @override
  _TurtleManagerState createState() => _TurtleManagerState();
}

class _TurtleManagerState extends State<TurtleManager> {
  void onExecute(String axiom, List<Rule> rules){
    print("hello" + axiom);
  }

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
                child: RightBar(onExecute: this.onExecute),
              ),
            )
          ],
        ),
      ],
    );
  }
}