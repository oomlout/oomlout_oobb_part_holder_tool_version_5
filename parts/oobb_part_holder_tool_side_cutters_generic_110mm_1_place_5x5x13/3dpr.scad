$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 6.5, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 6.5, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 6.5, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 6.5, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 8.5, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 8.5, r = 1.8);
		}
		translate(v = [0.0, -24.5, 0]) {
			linear_extrude(height = 11) {
				polygon(points = [[-11.5, 0], [-11.5, 35], [-33, 60], [-42, 110], [42, 110], [33, 60], [11.5, 35], [11.5, 0]]);
			}
		}
	}
}
