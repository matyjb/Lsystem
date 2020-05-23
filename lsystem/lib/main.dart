import 'package:flutter/material.dart';
import 'package:lsystem/Line.dart';
import 'package:lsystem/RightBar.dart';
import 'package:lsystem/Rule.dart';
import 'package:lsystem/TurtleCanvas.dart';
import 'package:lsystem/Turtle.dart';

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
  TurtleManager({Key key}) : super(key: key);

  @override
  _TurtleManagerState createState() => _TurtleManagerState();
}

class _TurtleManagerState extends State<TurtleManager> {
  List<Line> linesDrawn = [];

  String recursiveFindAndReplace(String substring, List<Rule> rules, int n) {
    if (n <= 0) return substring;

    List<String> outputString = [];
    int i = 0;
    while (i < substring.length) {
      bool didApplyRule = false;
      for (Rule r in rules) {
        if (substring.substring(i).startsWith(r.what)) {
          i += r.what.length;
          didApplyRule = true;
          outputString.add(recursiveFindAndReplace(r.to, rules, n - 1));
        }
      }

      if (!didApplyRule) {
        outputString.add(substring[i]);
        i++;
      }
    }
    return outputString.join();
  }

  List<Line> getLines(String s, Turtle turtle) {
    List<Turtle> stack = [];
    List<Line> result = [];

    for (int i = 0; i < s.length; i++) {
      switch (s[i]) {
        case "F":
          Offset oldPos = turtle.pos;
          turtle.moveForward();
          Offset newPos = turtle.pos;
          result.add(Line(oldPos, newPos));
          break;
        case "f":
          turtle.moveForward();
          break;
        case "+":
          turtle.rotateLeft();
          break;
        case "-":
          turtle.rotateRight();
          break;
        case "[":
          stack.add(turtle.clone());
          break;
        case "]":
          turtle = stack.removeLast();
          break;
        default:
          break;
      }
    }
    return result;
  }

  void onExecute(String axiom, List<Rule> rules, int n, double stepSize, double turningAngle) {
    // hilbert curve example
    // String a = "A";
    // List<Rule> r = <Rule>[Rule("A", "-BF+AFA+FB-"), Rule("B", "+AF-BFB-FA+")];
    String s = recursiveFindAndReplace(axiom, rules, n);

    Turtle turtle = Turtle();
    turtle.stepSize = stepSize;
    turtle.turningAngle = turningAngle;
    List<Line> lines = getLines(s, turtle);
    this.setState(() {
      linesDrawn = lines;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(child: TurtleCanvas(lines: linesDrawn)),
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
