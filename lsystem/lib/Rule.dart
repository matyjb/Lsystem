class Rule {
  String what;
  String to;

  Rule(this.what, this.to);

  @override
  String toString() {
    return this.what + "=>" + this.to;
  }
}
