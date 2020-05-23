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
  List<Rule> rules = [];

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border(left: BorderSide(color: Colors.grey, width: 2)),
      ),
      child: Column(
        children: [
          Center(
            child: Container(
              child: Text("Program",
                  style: TextStyle(
                      color: Colors.teal, fontWeight: FontWeight.bold)),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              onChanged: (text){
                this.setState(() {
                  axiom = text;
                });
              },
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Axiom',
              ),
            ),
          ),
          RaisedButton(
            onPressed: () => this.widget.onExecute(this.axiom,[]),
            child: Text("Execute"),
          )
        ],
      ),
    );
  }
}
