$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-17.0, 32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [17.0, 32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [-17.0, -32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [17.0, -32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 0.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 0.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, -22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, -7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, 7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, 22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, -22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, -7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, 7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, 22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [0.0, -16.25, 0]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-8.5, 0], [-8.5, 160], [8.5, 160], [8.5, 0]]);
			}
		}
	}
}

translate([50,0,0]) translate([0,0,12.75]) rotate([0,180,0]) {
$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-17.0, 32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [17.0, 32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [-17.0, -32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
				translate(v = [17.0, -32.0, 0]) {
					cylinder(h = 14.75, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, -15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 0.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, 30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, -15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 0.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 15.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [15.0, 30.0, -2]) {
			cylinder(h = 16.75, r = 3.25);
		}
		translate(v = [-15.0, -22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, -7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, 7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-15.0, 22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, -22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, -7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, 7.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [15.0, 22.5, -2]) {
			cylinder(h = 16.75, r = 1.8);
		}
		translate(v = [0.0, -16.25, -14.75]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-8.5, 0], [-8.5, 160], [8.5, 160], [8.5, 0]]);
			}
		}
	}
}

}
