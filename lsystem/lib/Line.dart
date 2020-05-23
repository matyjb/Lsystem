import 'package:flutter/material.dart';

class Line {
  Offset p0;
  Offset p1;
  Color color;

  Line(this.p0, this.p1, {this.color = Colors.black});

  Line.fromCoords(double p0x,double p0y,double p1x,double p1y, {this.color = Colors.black}) {
    this.p0 = Offset(p0x, p0y);
    this.p1 = Offset(p1x, p1y);
  }
}
