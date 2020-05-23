import 'package:flutter/material.dart';

class Line {
  Offset p0;
  Offset p1;
  Color color;

  Line(p0x, p0y, p1x, p1y, {this.color = Colors.black}) {
    this.p0 = Offset(p0x, p0y);
    this.p1 = Offset(p1x, p1y);
  }
}
