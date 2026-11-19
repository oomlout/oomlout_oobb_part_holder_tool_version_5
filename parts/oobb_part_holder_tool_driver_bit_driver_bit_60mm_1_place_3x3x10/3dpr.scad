$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-17.0, 17.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [17.0, 17.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [-17.0, -17.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [17.0, -17.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-15.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-15.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [0.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [15.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [15.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-15.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-15.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-7.5, -15.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [7.5, -15.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [15.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [15.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [0.0, -10, 4]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 60, r = 4);
			}
		}
	}
}
