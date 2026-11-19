$fn = 50;

difference() {
	union() {
		hull() {
			translate(v = [-47.0, 32.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [47.0, 32.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [-47.0, -32.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
			translate(v = [47.0, -32.0, 0]) {
				cylinder(h = 8.5, r = 5);
			}
		}
	}
	union() {
		translate(v = [-45.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-45.0, -15.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-45.0, 0.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-45.0, 15.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-45.0, 30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-30.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [0.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [15.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [30.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [45.0, -30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [45.0, -15.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [45.0, 0.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [45.0, 15.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [45.0, 30.0, -1]) {
			cylinder(h = 10.5, r = 3.25);
		}
		translate(v = [-45.0, -22.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-45.0, -7.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-45.0, 7.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-45.0, 22.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-37.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [7.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [22.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [37.5, -30.0, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [45.0, -22.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [45.0, -7.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [45.0, 7.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [45.0, 22.5, -1]) {
			cylinder(h = 10.5, r = 1.8);
		}
		translate(v = [-30.0, -23.0, 0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 7);
			}
		}
		translate(v = [-10.0, -23.0, 0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 7);
			}
		}
		translate(v = [10.0, -23.0, 0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 7);
			}
		}
		translate(v = [30.0, -23.0, 0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 137, r = 7);
			}
		}
	}
}
