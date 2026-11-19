$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-17.0, 32.0, 0]) {
					cylinder(h = 3.25, r = 5);
				}
				translate(v = [17.0, 32.0, 0]) {
					cylinder(h = 3.25, r = 5);
				}
				translate(v = [-17.0, -32.0, 0]) {
					cylinder(h = 3.25, r = 5);
				}
				translate(v = [17.0, -32.0, 0]) {
					cylinder(h = 3.25, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [-15.0, 0.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [-15.0, 15.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [-15.0, 30.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [15.0, 0.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [15.0, 15.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [15.0, 30.0, -2]) {
			cylinder(h = 5.25, r = 3.25);
		}
		translate(v = [-15.0, -22.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [-15.0, -7.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [-15.0, 7.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [-15.0, 22.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [15.0, -22.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [15.0, -7.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [15.0, 7.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [15.0, 22.5, -2]) {
			cylinder(h = 5.25, r = 1.8);
		}
		translate(v = [0.0, -27.75, 0]) {
			linear_extrude(height = 4.5) {
				polygon(points = [[-8, 0], [-8, 110], [8, 110], [8, 0]]);
			}
		}
	}
}
