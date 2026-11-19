$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-24.5, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [24.5, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [-24.5, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [24.5, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-22.5, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-22.5, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-22.5, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-22.5, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [22.5, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [22.5, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [22.5, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [22.5, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-22.5, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-22.5, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-22.5, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-22.5, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [22.5, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [22.5, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [22.5, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [22.5, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [0.0, -25, 14]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 96, r = 14);
			}
		}
	}
}
