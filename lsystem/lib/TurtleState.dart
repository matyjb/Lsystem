import 'package:flutter/material.dart';

class TurtleState {
  Offset pos;
  double rotation;

  TurtleState({posX = 0, posY = 0, this.rotation = 0}) {
    this.pos = Offset(posX, posY);
  }

  @override
  String toString() {
    return "(" +
        this.pos.dx.toString() +
        "," +
        this.pos.dy.toString() +
        "," +
        this.rotation.toString() +
        " deg)";
  }
}