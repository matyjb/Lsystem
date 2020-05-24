import 'package:flutter/material.dart';
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
  List<Path> pathsDrawn = [];

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

  List<Path> getLines(String s, Turtle turtle) {
    List<Turtle> stack = [];
    List<Path> paths = [Path()];

    for (int i = 0; i < s.length; i++) {
      switch (s[i]) {
        case "F": case "G":
          Offset oldPos = turtle.pos;
          turtle.moveForward();
          Offset newPos = turtle.pos;
          paths.last.moveTo(oldPos.dx, oldPos.dy);
          paths.last.lineTo(newPos.dx, newPos.dy);
          break;
        case "f":
          turtle.moveForward();
          paths.add(Path());
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
          paths.add(Path());
          break;
        default:
          break;
      }
    }
    // return result;
    return paths;
  }

  void onExecute(String axiom, List<Rule> rules, int n, double stepSize, double turningAngle) {
    // hilbert curve example
    // String a = "A";
    // List<Rule> r = <Rule>[Rule("A", "-BF+AFA+FB-"), Rule("B", "+AF-BFB-FA+")];
    String s = recursiveFindAndReplace(axiom, rules, n);

    Turtle turtle = Turtle();
    turtle.stepSize = stepSize;
    turtle.turningAngle = turningAngle;
    // List<Line> lines = getLines(s, turtle);
    List<Path> paths = getLines(s, turtle);
    this.setState(() {
      // linesDrawn = lines;
      pathsDrawn = paths;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(child: TurtleCanvas(paths: pathsDrawn)),
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
