$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-62.0, 32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [62.0, 32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [-62.0, -32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [62.0, -32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-60.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-45.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [45.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, -22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, 22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-52.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-37.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [37.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [52.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, -22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, 22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-41.0, -25, 0]) {
			linear_extrude(height = 8) {
				polygon(points = [[-14, 0], [-14, 70], [14, 70], [14, 0]]);
			}
		}
		translate(v = [-11.0, -25, 0.5]) {
			linear_extrude(height = 7) {
				polygon(points = [[-11.5, 0], [-11.5, 70], [11.5, 70], [11.5, 0]]);
			}
		}
		translate(v = [15.0, -25, 1.25]) {
			linear_extrude(height = 5.5) {
				polygon(points = [[-9, 0], [-9, 70], [9, 70], [9, 0]]);
			}
		}
		translate(v = [39.0, -25, 1.75]) {
			linear_extrude(height = 4.5) {
				polygon(points = [[-8, 0], [-8, 70], [8, 70], [8, 0]]);
			}
		}
	}
}

translate([140,0,0]) translate([0,0,3]) rotate([0,180,0]) {
$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-62.0, 32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [62.0, 32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [-62.0, -32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
				translate(v = [62.0, -32.0, 0]) {
					cylinder(h = 5.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-60.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, 30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-45.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [45.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, -30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, -15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 0.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 15.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [60.0, 30.0, -2]) {
			cylinder(h = 7.0, r = 3.25);
		}
		translate(v = [-60.0, -22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-60.0, 22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-52.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-37.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [37.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [52.5, -30.0, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, -22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, -7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, 7.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [60.0, 22.5, -2]) {
			cylinder(h = 7.0, r = 1.8);
		}
		translate(v = [-41.0, -25, -5.0]) {
			linear_extrude(height = 8) {
				polygon(points = [[-14, 0], [-14, 70], [14, 70], [14, 0]]);
			}
		}
		translate(v = [-11.0, -25, -4.5]) {
			linear_extrude(height = 7) {
				polygon(points = [[-11.5, 0], [-11.5, 70], [11.5, 70], [11.5, 0]]);
			}
		}
		translate(v = [15.0, -25, -3.75]) {
			linear_extrude(height = 5.5) {
				polygon(points = [[-9, 0], [-9, 70], [9, 70], [9, 0]]);
			}
		}
		translate(v = [39.0, -25, -3.25]) {
			linear_extrude(height = 4.5) {
				polygon(points = [[-8, 0], [-8, 70], [8, 70], [8, 0]]);
			}
		}
	}
}

}
