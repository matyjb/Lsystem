import 'package:flutter/material.dart';
import 'package:lsystem/Rule.dart';

class RightBar extends StatefulWidget {
  final Function onExecute;

  const RightBar({Key key, this.onExecute}) : super(key: key);

  @override
  _RightBarState createState() => _RightBarState();
}

class _RightBarState extends State<RightBar> {
  String axiom = "";
  int n = 0;
  double step = 10;
  double angle = 90;
  List<Rule> rules = [];

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border(left: BorderSide(color: Colors.grey, width: 2)),
      ),
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Center(
              child: Container(
                margin: EdgeInsets.symmetric(horizontal: 2),
                child: Text("Program",
                    style: TextStyle(
                        color: Colors.teal, fontWeight: FontWeight.bold)),
              ),
            ),
            TextField(
              onChanged: (text) {
                this.setState(() {
                  axiom = text;
                });
              },
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Axiom',
              ),
            ),
            Slider(
              value: this.n.toDouble(),
              label: this.n.toString() + " times",
              min: 0,
              max: 10,
              divisions: 10,
              onChanged: (double value){
                this.setState(() {
                  n = value.toInt();
                });
              },
            ),
            Slider(
              value: this.angle,
              label: this.angle.toInt().toString() + " degrees",
              min: -180,
              max: 180,
              divisions: 180,
              onChanged: (double value){
                this.setState(() {
                  angle = value;
                });
              },
            ),
            Slider(
              value: this.step,
              label: this.step.toInt().toString() + " steps",
              min: 0,
              max: 150,
              divisions: 150,
              onChanged: (double value){
                this.setState(() {
                  step = value;
                });
              },
            ),
            RaisedButton(
              onPressed: () => this.widget.onExecute(
                  this.axiom, <Rule>[], this.n, this.step, this.angle),
              child: Text("Execute"),
            )
          ],
        ),
      ),
    );
  }
}
