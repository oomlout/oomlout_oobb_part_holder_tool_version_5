$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-47.0, 17.0, 0]) {
					cylinder(h = 22.0, r = 5);
				}
				translate(v = [47.0, 17.0, 0]) {
					cylinder(h = 22.0, r = 5);
				}
				translate(v = [-47.0, -17.0, 0]) {
					cylinder(h = 22.0, r = 5);
				}
				translate(v = [47.0, -17.0, 0]) {
					cylinder(h = 22.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-45.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [-45.0, 0.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [-45.0, 15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [0.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [45.0, -15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [45.0, 0.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [45.0, 15.0, -2]) {
			cylinder(h = 24.0, r = 3.25);
		}
		translate(v = [-45.0, -7.5, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [-45.0, 7.5, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [-37.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [-22.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [-7.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [7.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [22.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [37.5, -15.0, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [45.0, -7.5, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [45.0, 7.5, -2]) {
			cylinder(h = 24.0, r = 1.8);
		}
		translate(v = [0.0, -9, 0]) {
			linear_extrude(height = 42) {
				polygon(points = [[-39, 0], [-39, 74], [39, 74], [39, 0]]);
			}
		}
	}
}
