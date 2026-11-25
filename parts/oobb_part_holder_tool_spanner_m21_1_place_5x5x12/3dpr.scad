$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 6.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 6.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 6.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 6.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 8.0, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 8.0, r = 1.8);
		}
		translate(v = [0.0, -25, 0]) {
			linear_extrude(height = 10) {
				polygon(points = [[-22, 0], [-22, 140], [22, 140], [22, 0]]);
			}
		}
	}
}
