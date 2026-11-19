$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-62.0, 32.0, 0]) {
					cylinder(h = 7.5, r = 5);
				}
				translate(v = [62.0, 32.0, 0]) {
					cylinder(h = 7.5, r = 5);
				}
				translate(v = [-62.0, -32.0, 0]) {
					cylinder(h = 7.5, r = 5);
				}
				translate(v = [62.0, -32.0, 0]) {
					cylinder(h = 7.5, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-60.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-60.0, -15.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-60.0, 0.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-60.0, 15.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-60.0, 30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-45.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [45.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [60.0, -30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [60.0, -15.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [60.0, 0.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [60.0, 15.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [60.0, 30.0, -2]) {
			cylinder(h = 9.5, r = 3.25);
		}
		translate(v = [-60.0, -22.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-60.0, -7.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-60.0, 7.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-60.0, 22.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-52.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-37.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [37.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [52.5, -30.0, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [60.0, -22.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [60.0, -7.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [60.0, 7.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [60.0, 22.5, -2]) {
			cylinder(h = 9.5, r = 1.8);
		}
		translate(v = [-46.875, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
		translate(v = [-28.125, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
		translate(v = [-9.375, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
		translate(v = [9.375, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
		translate(v = [28.125, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
		translate(v = [46.875, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 6.5);
			}
		}
	}
}
