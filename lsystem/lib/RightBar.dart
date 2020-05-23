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
            RulesInputList(onRulesChange: (newRules) {
              this.rules = newRules;
            }),
            Slider(
              value: this.n.toDouble(),
              label: this.n.toString() + " times",
              min: 0,
              max: 10,
              divisions: 10,
              onChanged: (double value) {
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
              onChanged: (double value) {
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
              onChanged: (double value) {
                this.setState(() {
                  step = value;
                });
              },
            ),
            RaisedButton(
              onPressed: () {
                this.widget.onExecute(
                    this.axiom, this.rules, this.n, this.step, this.angle);
              },
              child: Text("Execute"),
            )
          ],
        ),
      ),
    );
  }
}

class RulesInputList extends StatefulWidget {
  final Function onRulesChange;
  RulesInputList({Key key, this.onRulesChange}) : super(key: key);

  @override
  _RulesInputListState createState() => _RulesInputListState();
}

class _RulesInputListState extends State<RulesInputList> {
  List<Rule> rules = [];
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        for (Rule r in this.rules)
          Row(
            children: [
              Flexible(
                child: Container(
                  width: 30,
                  child: TextField(
                    controller: TextEditingController()..text = r.what,
                    onChanged: (text) {
                      r.what = text;
                      this.setState(() {});
                      this.widget.onRulesChange(this.rules);
                    },
                  ),
                ),
              ),
              Flexible(
                child: Container(
                  width: 250,
                  child: TextField(
                    controller: TextEditingController()..text = r.to,
                    onChanged: (text) {
                      r.to = text;
                      this.setState(() {});
                      this.widget.onRulesChange(this.rules);
                    },
                  ),
                ),
              ),
              IconButton(
                icon: Icon(Icons.remove),
                color: Colors.red,
                onPressed: () {
                  rules.remove(r);
                  this.setState(() {});
                  this.widget.onRulesChange(this.rules);
                },
              ),
            ],
          ),
        Row(
          children: [
            Expanded(
              child: RaisedButton.icon(
                onPressed: () {
                  rules.add(Rule("", ""));
                  this.setState(() {});
                },
                color: Colors.blue,
                icon: Icon(Icons.add),
                label: Text("Add rule"),
              ),
            ),
          ],
        )
      ],
    );
  }
}
