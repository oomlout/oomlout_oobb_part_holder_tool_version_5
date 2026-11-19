$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-17.0, 32.0, 0]) {
					cylinder(h = 3.75, r = 5);
				}
				translate(v = [17.0, 32.0, 0]) {
					cylinder(h = 3.75, r = 5);
				}
				translate(v = [-17.0, -32.0, 0]) {
					cylinder(h = 3.75, r = 5);
				}
				translate(v = [17.0, -32.0, 0]) {
					cylinder(h = 3.75, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [-15.0, 0.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [-15.0, 15.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [-15.0, 30.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [15.0, 0.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [15.0, 15.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [15.0, 30.0, -2]) {
			cylinder(h = 5.75, r = 3.25);
		}
		translate(v = [-15.0, -22.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [-15.0, -7.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [-15.0, 7.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [-15.0, 22.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [15.0, -22.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [15.0, -7.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [15.0, 7.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [15.0, 22.5, -2]) {
			cylinder(h = 5.75, r = 1.8);
		}
		translate(v = [0.0, -27.25, 0]) {
			linear_extrude(height = 5.5) {
				polygon(points = [[-9, 0], [-9, 120], [9, 120], [9, 0]]);
			}
		}
	}
}
