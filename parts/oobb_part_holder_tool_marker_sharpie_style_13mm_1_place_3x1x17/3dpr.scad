$fn = 50;

difference() {
	union() {
		hull() {
			translate(v = [-17.0, 2.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [17.0, 2.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [-17.0, -2.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [17.0, -2.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
		}
	}
	union() {
		translate(v = [-15.0, 0.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [0.0, 0.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [15.0, 0.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-7.5, 0.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [7.5, 0.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [0.0, -68.5, 0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 7);
			}
		}
	}
}
