
import 'package:flutter/material.dart';

class RightBar extends StatelessWidget {
  const RightBar({Key key}) : super(key: key);

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
              child: Text("Program",
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