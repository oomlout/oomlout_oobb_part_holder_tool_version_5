$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [0.0, -23.75, 0]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-23.5, 0], [-23.5, 160], [-6.5, 160], [-6.5, 0]]);
			}
		}
		translate(v = [15.0, -25, 18]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 57, r = 3.85);
			}
		}
		translate(v = [15.0, 32, 18]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 30, r = 5.5);
			}
		}
		translate(v = [15.0, 62, 18]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 17, r = 6.5);
			}
		}
		translate(v = [15.0, 79, 18]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 18);
			}
		}
	}
}

translate([80,0,0]) translate([0,0,17]) rotate([0,180,0]) {
$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 19.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 21.0, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 21.0, r = 1.8);
		}
		translate(v = [0.0, -23.75, -19.0]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-23.5, 0], [-23.5, 160], [-6.5, 160], [-6.5, 0]]);
			}
		}
		translate(v = [15.0, -25, -1.0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 57, r = 3.85);
			}
		}
		translate(v = [15.0, 32, -1.0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 30, r = 5.5);
			}
		}
		translate(v = [15.0, 62, -1.0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 17, r = 6.5);
			}
		}
		translate(v = [15.0, 79, -1.0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 100, r = 18);
			}
		}
	}
}

}
