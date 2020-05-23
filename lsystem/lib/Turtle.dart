import 'dart:math';

import 'package:flutter/material.dart';

class Turtle {
  Offset pos;
  double rotation;
  double stepSize = 10;
  double turningAngle = 90;

  Turtle({posX = 10, posY = 10, this.rotation = 0}) {
    this.pos = Offset(posX, posY);
  }

  Turtle clone() {
    Turtle t = Turtle(posX: this.pos.dx,posY: this.pos.dy,rotation: this.rotation);
    t.stepSize = this.stepSize;
    t.turningAngle = this.turningAngle;
    return t;
  }

  void moveForward(){
    double cosine = cos(this.rotation * pi / 180.0);
    double sine = sin(this.rotation * pi / 180.0);
    double x = cosine * 0 - sine * this.stepSize;
    double y = cosine * this.stepSize + sine * 0;
    this.pos += Offset(x,y);
  }

  void rotateLeft(){
    this.rotation += this.turningAngle;
    
    if (this.rotation > 180)
      this.rotation -= 360;
  }


  void rotateRight(){
    this.rotation -= this.turningAngle;

    if (this.rotation < -180)
      this.rotation += 360;
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