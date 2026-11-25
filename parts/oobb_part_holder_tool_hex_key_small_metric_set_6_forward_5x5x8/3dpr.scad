module rear() { translate([0,0,2]) rotate([0,180,0]) {
$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 4.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 4.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 4.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 4.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 6.0, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 6.0, r = 1.8);
		}
		translate(v = [-22.5, -1, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 1.55);
			}
		}
		translate(v = [-13.5, -5, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 1.8);
			}
		}
		translate(v = [-4.5, -7, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 1.95);
			}
		}
		translate(v = [4.5, -13, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 2.25);
			}
		}
		translate(v = [13.5, -19, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 2.75);
			}
		}
		translate(v = [22.5, -25, -1]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 3.25);
			}
		}
	}
}

} }
rear();
translate([80,0,0]) mirror([1,0,0]) rear();
