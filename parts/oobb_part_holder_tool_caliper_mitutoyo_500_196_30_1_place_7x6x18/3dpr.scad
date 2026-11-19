$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-47.0, 39.5, 0]) {
					cylinder(h = 9.0, r = 5);
				}
				translate(v = [47.0, 39.5, 0]) {
					cylinder(h = 9.0, r = 5);
				}
				translate(v = [-47.0, -39.5, 0]) {
					cylinder(h = 9.0, r = 5);
				}
				translate(v = [47.0, -39.5, 0]) {
					cylinder(h = 9.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-45.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, -22.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, -7.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, 7.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, 22.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, 37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-30.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-15.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [0.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [15.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [30.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, -37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, -22.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, -7.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, 7.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, 22.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [45.0, 37.5, -2]) {
			cylinder(h = 11.0, r = 3.25);
		}
		translate(v = [-45.0, -30.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-45.0, -15.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-45.0, 0.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-45.0, 15.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-45.0, 30.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-37.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-22.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [-7.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [7.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [22.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [37.5, -37.5, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [45.0, -30.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [45.0, -15.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [45.0, 0.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [45.0, 15.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [45.0, 30.0, -2]) {
			cylinder(h = 11.0, r = 1.8);
		}
		translate(v = [0.0, -32, 0]) {
			linear_extrude(height = 16) {
				polygon(points = [[-39, 0], [-39, 78], [39, 78], [39, 0]]);
			}
		}
	}
}
