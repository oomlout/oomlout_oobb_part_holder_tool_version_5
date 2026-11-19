$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
			}
		}
		translate(v = [80, 0, -1]) {
			hull() {
				translate(v = [-32.0, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [32.0, 32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [-32.0, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
				translate(v = [32.0, -32.0, 0]) {
					cylinder(h = 15.0, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-30.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-30.0, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-30.0, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-30.0, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-30.0, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-15.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [0.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [15.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [30.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [30.0, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [30.0, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [30.0, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [30.0, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [-30.0, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-30.0, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-30.0, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-30.0, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-22.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [-7.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [7.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [22.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [30.0, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [30.0, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [30.0, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [30.0, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [0.0, -23.75, 0]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-23.5, 0], [-23.5, 160], [-6.5, 160], [-6.5, 0]]);
			}
		}
		translate(v = [11.0, -25, 14]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 96, r = 14);
			}
		}
		translate(v = [50.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [50.0, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [50.0, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [50.0, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [50.0, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [65.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [80.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [95.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [110.0, -30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [110.0, -15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [110.0, 0.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [110.0, 15.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [110.0, 30.0, -2]) {
			cylinder(h = 17.0, r = 3.25);
		}
		translate(v = [50.0, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [50.0, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [50.0, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [50.0, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [57.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [72.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [87.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [102.5, -30.0, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [110.0, -22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [110.0, -7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [110.0, 7.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [110.0, 22.5, -2]) {
			cylinder(h = 17.0, r = 1.8);
		}
		translate(v = [80.0, -23.75, -15.0]) {
			linear_extrude(height = 27.5) {
				polygon(points = [[-23.5, 0], [-23.5, 160], [-6.5, 160], [-6.5, 0]]);
			}
		}
		translate(v = [91.0, -25, -1.0]) {
			rotate(a = [-90, 0, 0]) {
				cylinder(h = 96, r = 14);
			}
		}
	}
}
